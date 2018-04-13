# from urllib import request

from django.shortcuts import render
from django.views.generic import TemplateView
from django.db import models
from django.template.response import TemplateResponse
from .import_data import *
from .pdf_sanner import scanPdf

# Create your views here.
# class HomePageView(TemplateView):
    # template_name = 'Dashboard.html'
def dashboard(request):
    myString = "hello"
    scanPdf()
    # name = importPersonalData()[0]
    return TemplateResponse(request, 'Dashboard.html', {'name': importPersonalData()[0],
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


    # def get_context_data(self, **kwargs):
        # return render(request, 'Dashboard.html', {'h': h, 'varr': varr})
    # def get(self, request, **kwargs):
    #     return render(request, 'Dashboard.html', context=None)

    #


        # context = super(HomePageView, self).get_context_data(**kwargs)
        # here's the difference:
        # context['all_score'] = "aminda"
        # CompanyProfile.company_name = "csaxsa"
        # context['company_profiles'] = CompanyProfile.objects.all()
        # return context



class CompanyProfile(models.Model):
   company_name = models.CharField(max_length=25)

# login view.
class LoginPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'SignIn.html', context=None)
