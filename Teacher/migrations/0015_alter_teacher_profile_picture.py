# Generated by Django 4.0.5 on 2022-06-17 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0014_alter_teacher_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='Profile_Picture',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
