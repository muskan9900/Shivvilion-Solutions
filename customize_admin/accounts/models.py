from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import AdminUserManager


class AdminUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)

    # vertical structure
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="children",
    )

    is_super_admin = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    roles=models.ManyToManyField("Role",blank=True,related_name="admins")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AdminUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    def clean(self):
        #  Only one super admin
        if self.is_super_admin:
            qs = AdminUser.objects.filter(is_super_admin=True)
            if self.pk:
                qs = qs.exclude(pk=self.pk)
            if qs.exists():
                raise ValidationError("Only one Super Admin is allowed.")

        # validations
        # Super admin must have no parent
        if self.is_super_admin and self.parent_id is not None:
            raise ValidationError("Super Admin cannot have a parent.")

        # Sub admin must have a parent
        if not self.is_super_admin and self.parent_id is None:
            raise ValidationError("Sub Admin must have a parent.")

        # Self-parent check
        if self.pk and self.parent_id == self.pk:
            raise ValidationError("An admin cannot be their own parent.")

        # Prevent cycles (parent cannot be your descendant)
        if self.pk and self.parent is not None:
            if self.parent.is_descendant_of(self):
                raise ValidationError("Invalid parent (cycle detected).")

    #  Vertical helpers methods
    def get_ancestors(self):
        ancestors = []
        node = self.parent
        while node is not None:
            ancestors.append(node)
            node = node.parent
        return ancestors

    def is_descendant_of(self, admin):
        if admin is None:
            return False
        node = self.parent
        while node is not None:
            if node.pk == admin.pk:
                return True
            node = node.parent
        return False

    def can_manage(self, target_admin):
        if target_admin is None:
            return False
        if self.is_super_admin:
            return True
        if self.pk == target_admin.pk:
            return True
        return target_admin.is_descendant_of(self)
    
    # horizontal helper methods
        # """get_permission_codes()→  WHAT I CAN DO
        #    has_perm_code()→  CAN I DO THIS?
        # """
        # has_perm_code() depends on get_permission_codes().

    def get_permission_codes(self):
        # it returns set of permission codes the admin has via roles
        #  eg {'admin.create' , 'reports.view' }
        if self.is_super_admin:
            # super admin is treated as all permissions
            return("*") # this is marked as all permissions 
        
        qs =(Permission.objects.filter(roles__admins=self).values_list("code", flat=True) .distinct()
             )
        return set(qs)
    
    def has_perm_code(self,code:str)->bool:
        # checks if admin has a specific permission code 
        if self.is_super_admin:
            return True
        return code in self.get_permission_codes()


# horizontal structure 
# permission and role models 

class Permission(models.Model):
    # permissions are single action
    # example code='admin.create'

    code=models.CharField(max_length=100,unique=True)
    label=models.CharField(max_length=150)

    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code}"


class Role(models.Model):
    # roles are bundles of permissions
    # example name='Finance Admin'

    name=models.CharField(max_length=80,unique=True)
    permissions=models.ManyToManyField(Permission,blank=True,related_name="roles")

    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"




# shell testing code
# ----- for vertical hierarchy----
# 1) Create Super Admin (only once)
# super_admin = AdminUser.objects.create_user(
#     email="super@example.com",
#     password="super123",
#     is_super_admin=True,
#     is_staff=True,
#     is_superuser=True,
#     parent=None
# )

# 2) Create sub admins under Super Admin
# a = AdminUser.objects.create_user(email="a@example.com", password="a123", parent=super_admin) (created)
# b = AdminUser.objects.create_user(email="b@example.com", password="b123", parent=super_admin)

# 3) Create deeper level under A
# a1 = AdminUser.objects.create_user(email="a1@example.com", password="a1123", parent=a)

#  TEST vertical helpers 
# a1.get_ancestors()  # should show [a, super_admin]
# a1.is_descendant_of(a)          # True
# a1.is_descendant_of(super_admin)# True
# a1.is_descendant_of(b)          # False

# a.can_manage(a1)  # True
# a.can_manage(b)   # False
# super_admin.can_manage(b)  # True


# ---- to count the number of childrens in each super admin
# from accounts.models import AdminUser

# for u in AdminUser.objects.filter(is_super_admin=True):
#     print(u.email, "children:", u.children.count())

# ---- to check how many super admins are there
# from accounts.models import AdminUser

# qs = AdminUser.objects.filter(is_super_admin=True).values("id", "email", "is_staff", "is_superuser", "parent_id", "created_at")
# for row in qs:
#     print(row)

# ---- to verify admins 
# from accounts.models import AdminUser
# print(AdminUser.objects.filter(is_super_admin=True).values("id","email"))
# print("count:", AdminUser.objects.filter(is_super_admin=True).count())  

# ---- horizontal structure

# from accounts.models import AdminUser, Role, Permission

# Create permissions
# p1 = Permission.objects.create(code="admins.create", label="Create sub admins")
# p2 = Permission.objects.create(code="admins.view", label="View admins")
# p3 = Permission.objects.create(code="reports.view", label="View reports")

# Create role and assign permissions
# finance = Role.objects.create(name="Finance Admin")
# finance.permissions.add(p3)

# manager = Role.objects.create(name="Sub Admin Manager")
# manager.permissions.add(p1, p2)

# pick a sub admin
# a = AdminUser.objects.get(email="a@example.com")

# assign roles to admin A
# a.roles.add(finance, manager)

# test
# print(a.has_perm_code("admins.create"))  # True
# print(a.has_perm_code("reports.view"))   # True
# print(a.has_perm_code("posts.create"))   # False

# --------------- only if the above doesnt work---------------#
# recheck with the following queries becuase add() in django returns none
# a = AdminUser.objects.get(email="a@example.com")

# print("Roles on a:", list(a.roles.values_list("name", flat=True)))
# print("Finance perms:", list(Role.objects.get(name="Finance Admin").permissions.values_list("code", flat=True)))
# print("Manager perms:", list(Role.objects.get(name="Sub Admin Manager").permissions.values_list("code", flat=True)))



