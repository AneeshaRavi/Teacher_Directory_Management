from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from .views import Teacher_Profile_Update
urlpatterns=[
    path('Login',views.Login,name='Login'),
    path('', views.Teacher_detail, name='Teacher_detail'),
    path('teacher_add_sv/',views.teacher_add_sv,name='teacher_add_sv'),
    path('teacher_search/',views.teacher_search,name='teacher_search'),
    path('update/<int:pk>',Teacher_Profile_Update.as_view(),name='update'),

    
    
     
]
