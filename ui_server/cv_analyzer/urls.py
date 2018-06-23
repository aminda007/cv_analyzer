"""cv_analyzer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
# from django.urls import url
from . import views
from django.urls import path
# from django.conf.urls import url



urlpatterns = [

    path(r'', views.LoginPageView.as_view()),
    path(r'dashboard', views.DashboardView.as_view()),
    path(r'home', views.home),
    path(r'cv-linkedin', views.cvLinkedIn, name='cv_linked_in'),
    path(r'delete', views.delete_file, name='resume_delete'),
    path(r'delete-cv', views.delete_file_cv, name='cv_delete'),
    path(r'upload', views.upload_file, name='resume_upload'),
    path(r'upload-cv', views.upload_file_cv, name='cv_upload'),
    path(r'delete-all', views.delete_all),
    path(r'delete-all-cv', views.delete_all_cv),
    path(r'analysis', views.analysis),
    path(r'qa', views.qa, name='q_a'),
    path(r'interview', views.interview, name='interview_qa'),
    path(r'qa-train', views.qna_train),
    path(r'add-skills', views.add_skills, name='skills_add'),
    path(r'add-skill', views.add_skill, name='skill_add'),
    path(r'delete-skill', views.delete_skill, name='skill_delete'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

