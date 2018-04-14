# from urllib import request

from django.shortcuts import render
from django.views.generic import TemplateView
from django.db import models
from django.template.response import TemplateResponse
from .import_data import *
from .pdf_sanner import scanPdf

# Create your views here.


def cvTemplate(request):
    scanPdf()
    return TemplateResponse(request, 'TemplateCVAnalyzer.html', {'name': importPersonalData()[0],
                                                        'email': importPersonalData()[1],
                                                        'linkedin': importPersonalData()[2],
                                                        'languages': importLanguageData(),
                                                        'libraries': importLibrariesData(),
                                                        'frameworks': importFrameworksData(),
                                                        'database': importDatabaseData(),
                                                        'mobile': importMobile(),
                                                        'ides': importIDE(),
                                                        'version_control': importVersionData(),
                                                        'os': importOSData(),
                                                        'projects': importProjectData(),
                                                        })


def cvLinkedIn(request):
    scanPdf()
    return TemplateResponse(request, 'LinkedInAnalyzer.html', {'name': importPersonalData()[0],
                                                        'email': importPersonalData()[1],
                                                        'linkedin': importPersonalData()[2],
                                                        'languages': importLanguageData(),
                                                        'libraries': importLibrariesData(),
                                                        'frameworks': importFrameworksData(),
                                                        'database': importDatabaseData(),
                                                        'mobile': importMobile(),
                                                        'ides': importIDE(),
                                                        'version_control': importVersionData(),
                                                        'os': importOSData(),
                                                        'projects': importProjectData(),
                                                        })


# login view.
class LoginPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'SignIn.html', context=None)


# dashboard view.
class DashboardView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'Dashboard.html', context=None)
