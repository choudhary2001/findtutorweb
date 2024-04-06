from django.contrib import admin

# Register your models here.
from .models import Student, Teacher

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # Specify the fields to be displayed in the admin interface for Student
    list_display = ('user', 'full_name','phone')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    # Specify the fields to be displayed in the admin interface for Teacher
    list_display = ('user', 'pincode', 'full_name', 'address', 'profile_img')


    
