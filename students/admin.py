from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_Name','student_Email', 'student_Phone_Number', 'student_Nationality']