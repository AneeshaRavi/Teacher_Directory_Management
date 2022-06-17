from distutils.command.upload import upload
from pickle import TRUE
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField
# Create your models here.


class Teacher(models.Model):
    SUBJECT_CHOICES =(
    ("Malayalam", "Malayalam"),
    ("English", "English"),
    ("Computer Science", "Computer Science"),
    ("History", "History"),
    ("Mathematics", "Mathematics"),
    ("Arabic", "Arabic"),
    ("Physics", "Physics"),
    ("Biology", "Biology"),
    ("Chemistry", "Chemistry"),
    ("Geography", "Geography"),
)
    First_Name=models.CharField(max_length=250,null=False,blank=False)
    Last_Name=models.CharField(max_length=250,null=False,blank=False)
    Profile_Picture=models.ImageField(upload_to='images',null=True, blank=True)
    Email_Address=models.EmailField(unique=True,null=False,blank=False)
    Phone_Number = PhoneNumberField(unique = True, null = False, blank = False)
    Room_Number=models.CharField(max_length=10,null=False,blank=False)
    # Subjects_taught=models.(max_length=250,null=False,blank=False)
    Subjects_taught=MultiSelectField(max_length=250, choices=SUBJECT_CHOICES,null=False,blank=False)
    

