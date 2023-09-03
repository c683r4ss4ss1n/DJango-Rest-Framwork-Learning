from django.db import models

# Create your models here.

class Students(models.Model):
    student_Name = models.CharField(max_length=30)
    student_Email = models.EmailField()
    student_Phone_Number = models.CharField(max_length=12)
    student_Nationality = models.CharField(max_length=20)