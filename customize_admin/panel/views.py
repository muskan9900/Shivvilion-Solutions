from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import AdminUser,Role
from core.decorators import permission_required_code
from .forms import CreateSubAdminForm


# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect("panel_dashboard")
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=authenticate(request,email=email,password=password)
        if user is not None and user.is_active:
            login(request,user)
            return redirect('panel_dashboard')
        messages.error(request,"invalid credentials or inactive account.")
        return redirect("panel_login")
    return render(request,"panel/login.html")

@login_required
def dashboard(request):
    return render(request,"panel/dashboard.html")
    
def logout_view(request):
    logout(request)
    return redirect("panel_login")

@login_required
@permission_required_code("admins.view")
def admin_list(request):
    # horizontal: must have 'admins.view'
    # vertical: show only subtree admins()

    user=request.user

    if user.is_super_admin:
        admins= AdminUser.objects.all().order_by("created_at")
    else:
        all_admins= AdminUser.objects.all().order_by("created_at")
        admins=[a for a in all_admins if user.can_manage(a)]
    return render(request,"panel/admin_list.html",{"admins":admins})


@login_required
@permission_required_code("admins.create")
def admin_create(request):
    if request.method == "POST":
        form = CreateSubAdminForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            #  decide parent
            if request.user.is_super_admin:
                selected_parent = form.cleaned_data.get("parent_id")  
                parent = selected_parent if selected_parent else request.user
            else:
                parent = request.user

            # use parent variable NOT request.user(as request.user belongs to super admin)
            new_admin = AdminUser.objects.create_user(
                email=email,
                password=password,
                parent=parent,
                is_super_admin=False,
                is_staff=False,
                is_superuser=False,
            )

            # adding default role
            default_role = Role.objects.filter(name="Sub Admin Manager").first()
            if default_role:
                new_admin.roles.add(default_role)

            messages.success(request, f"Sub Admin created: {new_admin.email} (parent: {parent.email})")
            return redirect("panel_admin_list")

        # if invalid, re-render with errors
        return render(request, "panel/admin_create.html", {"form": form})

    # GET
    form = CreateSubAdminForm()
    return render(request, "panel/admin_create.html", {"form": form})
