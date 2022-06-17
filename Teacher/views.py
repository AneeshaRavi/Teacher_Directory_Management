from typing_extensions import Self
import django
from django import forms
from django.shortcuts import render,redirect
from .models import Teacher
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .forms import TeacherAdd_Form,EditTeacher_Profile
from django.http import HttpResponse, JsonResponse
from django.views.generic import UpdateView
from django.urls import reverse_lazy
# Create your views here.

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Teacher_detail')
        else:
            messages.success(request,("There Was An Error Logging In, Try Again....."))
            return redirect('Login')

    return render(request,'Login.html')

def Teacher_detail(request):
    context = {}
    fm = TeacherAdd_Form()
    tchr_dtls = Teacher.objects.all()
    context = {'show':tchr_dtls,'teacher_add_form':fm}
    return render(request, 'TeacherDetails.html',context)

def teacher_add_sv(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax and request.method == "POST":
        fm = TeacherAdd_Form(request.POST,request.FILES) 
        image=request.POST.get('Profile_Picture')
        
        print(image)
        print(fm)
        print("form data : ",fm)
        if fm.is_valid():
            subject=request.POST.getlist('Subjects_taught')
            length=len(subject)
            if length > 5:
                 return JsonResponse({"notfound":"notfound"})

            fm.save()
            return JsonResponse({"Sucess": True}, status=200)
        else:
            print("Error : ",fm.errors)
            return JsonResponse({"error": fm.errors}, status=400)
            
    return JsonResponse({"error": ""}, status=400)



def teacher_search(request):
    if request.GET.get('teacher_text'):
        tchr_txt = request.GET.get('teacher_text')
        search_result = Teacher.objects.filter(Last_Name__startswith=tchr_txt).values()
        if search_result.exists():
            return JsonResponse({"data": list(search_result)})
        else:
            return JsonResponse({"notfound": "notfound"})
    else:
        pass

class Teacher_Profile_Update(UpdateView):
    model=Teacher
    template_name='Teacher_Profile_Edit.html'
    form_class=EditTeacher_Profile
    success_url=reverse_lazy('Teacher_detail')