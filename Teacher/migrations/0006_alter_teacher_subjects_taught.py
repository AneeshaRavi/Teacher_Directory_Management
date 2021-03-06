# Generated by Django 4.0.5 on 2022-06-16 11:21

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0005_alter_teacher_subjects_taught'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='Subjects_taught',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Malayalam', 'Malayalam'), ('English', 'English'), ('Computer Science', 'Computer Science'), ('History', 'History'), ('Mathematics', 'Mathematics'), ('Arabic', 'Arabic'), ('Physics', 'Physics'), ('Biology', 'Biology'), ('Chemistry', 'Chemistry'), ('Geography', 'Geography')], max_length=250),
        ),
    ]
