from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    full_name= models.CharField(max_length=100)
    phone = models.IntegerField()
    courses= models.CharField(max_length=100)
    subjects= models.CharField(max_length=100)
    tution_desc=models.CharField(max_length=200)
    tution_location= models.CharField(max_length=100)
    preferred_timing= models.CharField(max_length=100)
    preferred_tutor = models.CharField(max_length=200)
    fee_offered = models.CharField(max_length=100)
    tution_type = models.CharField(max_length=200)
    pincode = models.IntegerField()
    city= models.CharField(max_length=100)
    locality= models.CharField(max_length=100)
    posted_on = models.DateField(auto_now=True)

class Teacher(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    full_name= models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age= models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    locality= models.CharField(max_length=100)
    landmark= models.CharField(max_length=100,null=True,blank=True)
    address= models.CharField(max_length=200)
    phone= models.CharField(max_length=100)
    pincode = models.IntegerField()
    category= models.CharField(max_length=100,null=True,blank=True)
    courses= models.CharField(max_length=100)
    subjects= models.CharField(max_length=100)
    qualification = models.CharField(max_length= 100)
    college = models.CharField(max_length = 100,null=True,blank=True)
    university= models.CharField(max_length=100,null=True,blank=True)
    experience= models.CharField(max_length=100)
    hourly_price= models.CharField(max_length=100)
    preferred_timing= models.CharField(max_length=100)
    about_me= models.CharField(max_length=200)
    profile_img = models.ImageField(upload_to='profile/',null=True,blank=True)
   
