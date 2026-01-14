from django.shortcuts import render,HttpResponse
from .forms import ResumeForm

# Create your views here.

def jobapply(request):
    if request.method =='POST':
        form = ResumeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Your Job Application is successful')
        
    else:
            form= ResumeForm()
            context={
                'form': form,
            }

            return render(request,'apply_form.html',context)

