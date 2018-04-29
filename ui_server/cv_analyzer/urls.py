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
    # url(r'^$', views.HomePageView.as_view()),
    path(r'', views.LoginPageView.as_view()),
    path(r'dashboard', views.DashboardView.as_view()),
    path(r'home', views.home),
    path(r'cv-template', views.cvTemplate),
    path(r'cv-linkedin', views.cvLinkedIn, name='cv_linked_in'),
    # path(r'upload', views.upload_file),
    path(r'delete', views.delete_file, name='resume_delete'),
    path(r'delete-cv', views.delete_file_cv, name='cv_delete'),
    # path(r'delete', views.delete_file, name='resume_delete'),
    path(r'upload', views.upload_file, name='resume_upload'),
    path(r'upload-cv', views.upload_file_cv, name='cv_upload'),
    path(r'delete-all', views.delete_all),
    path(r'delete-all-cv', views.delete_all_cv),
    path(r'analysis', views.analysis),
    # path(r'delete-all', views.delete_all, name='resume_delete_all'),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # path(r'dashboard', views.HomePageView.as_view()),
