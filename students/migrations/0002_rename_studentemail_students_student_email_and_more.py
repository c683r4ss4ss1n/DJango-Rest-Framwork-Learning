# Generated by Django 4.2.4 on 2023-09-03 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='studentEmail',
            new_name='student_Email',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='studentName',
            new_name='student_Name',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='studentNationality',
            new_name='student_Nationality',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='studentPhoneNumber',
            new_name='student_Phone_Number',
        ),
    ]
