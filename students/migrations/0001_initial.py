# Generated by Django 4.2.4 on 2023-09-03 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentName', models.CharField(max_length=30)),
                ('studentEmail', models.EmailField(max_length=254)),
                ('studentPhoneNumber', models.CharField(max_length=12)),
                ('studentNationality', models.CharField(max_length=20)),
            ],
        ),
    ]
