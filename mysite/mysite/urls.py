"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from polls import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "main"

urlpatterns = [
    path('bhuvancred/', views.bhuvancred, name='bhuvancred'),
    path('GetLearnerAssessments/', views.GetLearnerAssessments, name='GetLearnerAssessments'),
    path('getTeacherDetails/', views.getTeacherDetails, name='getTeacherDetails'),
    path('GetGroupSessionInfo/', views.GetGroupSessionInfo, name='GetGroupSessionInfo'),
    path('GetPeopleInformation/', views.GetPeopleInformation, name='GetPeopleInformation'),
    path('getCourseSessionMapping/', views.getCourseSessionMapping, name='getCourseSessionMapping'),
    path('GetLearnerAssessments/', views.GetLearnerAssessments, name='GetLearnerAssessments'),

    
    # path('samples/', views.samples, name='samples'),
    # path('employess/', views.employess, name='employess'),
    # # path('dropdown/', views.dropdown, name='dropdown'),
    #  path('generate-excel/', views.generate_excel, name='generate_excel'),
    # path('barchart/', views.barchart, name='barchart'),
    # path('register/', views.registration, name='register'),
    # path('latest/', views.latest, name='latest'),
    # path('users/<str:user_name>/', views.user_name, name='user-detail'),
    # path('users_name/<int:user_id>/', views.user_detail, name='user_name'),
    # path("test", views.test, name="test"), 
    # path("back", views.new_Sample, name=""), 
    # path('welcome/<str:name>/', views.welcome),
            
    # path("contact1", views.sample, name="contact1"),
    # path("contact", views.contact, name="contact"),
    # path("my-data", views.my_data, name="my-data"),
    # path("submit_form", views.submit_form, name="submit_form"),
    # path("error", views.error, name="error"),
    # path("reg/", views.reg, name="reg"),
    # # path("details", views.details, name="details"),
    # path("delete/<int:id>", views.delete, name="delete"),
    # # path("jsonres", views.send_dictionary, name="jsonres"),
]
# add at the last
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
