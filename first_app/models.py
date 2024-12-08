from django.db import models
from django.contrib.auth.models import AbstractUser , AbstractBaseUser , UserManager
from django.contrib.auth.models import PermissionsMixin

class mymanager(UserManager):
    pass

# Create your models here.
class User(AbstractBaseUser , PermissionsMixin):
    email = models.EmailField(unique = True)
    username = models.TextField(max_length = 150)
    Category = models.CharField(max_length = 65)
    is_patient = models.BooleanField(default = False)
    is_doctor = models.BooleanField(default = False)
    is_hospital = models.BooleanField(default = False)
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]
    phonenumber = models.CharField(max_length = 20 , default = "None")
    gender = models.CharField(max_length = 65 , null = True)
    age = models.IntegerField(default = 0)
    is_active = models.BooleanField(default = True)
    is_superuser = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    objects = mymanager()
    photo = models.ImageField(upload_to = "testing/" , default = "default.png")
    

class patient(models.Model):
   user = models.ForeignKey(User , on_delete = models.CASCADE , related_name = "patient_info")
class doctor(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE , related_name = "doctor_info")
    specialist = models.CharField(max_length = 200 , null = True)
    likes = models.IntegerField(default = 0)

class doctor_patient(models.Model):
    patient = models.ForeignKey(patient , on_delete = models.CASCADE , related_name = "my_doctors")
    doctors = models.ManyToManyField(doctor , related_name = "my_patients")

class doctor_patient_liked(models.Model):
    patient = models.ForeignKey(patient , on_delete = models.CASCADE , related_name = "liked_doctors")
    doctors = models.ManyToManyField(doctor , related_name = "liked_patients")


class doctors_advices(models.Model):
    doctor = models.ForeignKey(doctor , on_delete = models.CASCADE , related_name = "doctor_advices")
    advice = models.TextField()
    date = models.DateField(auto_now = True)
    
class patient_pending(models.Model):
    patient = models.ForeignKey(patient , on_delete = models.CASCADE , related_name = "patient_pendings")
    doctors = models.ManyToManyField(doctor  , related_name = "doctor_pendings")

class massage(models.Model):
    patient = models.ForeignKey(patient , on_delete=models.CASCADE , related_name = "patient_massages")
    doctor = models.ForeignKey(doctor , on_delete= models.CASCADE , related_name= "doctor_massages" )
    massage = models.TextField()
    date = models.DateField(auto_now_add= True)
    title = models.TextField(null = True)
    sender = models.ForeignKey(User , on_delete= models.CASCADE , related_name = "sender_massages" , null = True)