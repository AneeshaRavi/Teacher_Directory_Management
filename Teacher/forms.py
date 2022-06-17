from pyexpat import model
from django import forms
from dataclasses import fields
from django.forms import ModelForm
from Teacher.models import Teacher

class TeacherAdd_Form(forms.ModelForm):
    
    class Meta:
        model = Teacher
        fields=('First_Name','Last_Name','Profile_Picture','Email_Address','Phone_Number','Room_Number','Subjects_taught')
        widgets ={
            'First_Name':forms.TextInput(attrs={'class':'form-control'}),
            'Last_Name':forms.TextInput(attrs={'class':'form-control'}),
            'Email_Address':forms.EmailInput(attrs={'class':'form-control'}),
            'Phone_Number':forms.TextInput(attrs={'class':'form-control'}),
            'Room_Number':forms.TextInput(attrs={'class':'form-control'}),
           
           
        }
        def __init__(self,*args,**kwargs):
            super(TeacherAdd_Form,self).__init__(*args,**kwargs)
        
        def __init__(self, *args, **kwargs):
            super(TeacherAdd_Form, self).__init__(*args, **kwargs)
            self.fields['Profile_Picture'].required = False

class EditTeacher_Profile(forms.ModelForm):
    class Meta:
        model=Teacher
        fields=('First_Name','Last_Name','Profile_Picture','Email_Address','Phone_Number','Room_Number','Subjects_taught')
        widgets ={
            'First_Name':forms.TextInput(attrs={'class':'form-control'}),
            'Last_Name':forms.TextInput(attrs={'class':'form-control'}),
            'Email_Address':forms.EmailInput(attrs={'class':'form-control'}),
            'Phone_Number':forms.TextInput(attrs={'class':'form-control'}),
            'Room_Number':forms.TextInput(attrs={'class':'form-control'}),
           
           
        }