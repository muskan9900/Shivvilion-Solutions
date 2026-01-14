from django.db import models

# Create your models here.

class Resume(models.Model):
    Full_name= models.CharField(max_length=150)
    gender= models.CharField(max_length=10)
    date_of_birth = models.DateField()
    email= models.EmailField()
    current_address = models.CharField(max_length=300)
    city= models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    resume =models.FileField(upload_to='resumes/')

    def __str__(self):
        return f"{self.Full_name}"