# Generated by Django 4.0.5 on 2022-06-17 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0013_alter_teacher_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='Profile_Picture',
            field=models.ImageField(upload_to='images'),
        ),
    ]
