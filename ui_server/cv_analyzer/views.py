# from urllib import request

from django.shortcuts import render
from django.views.generic import TemplateView
from django.template.response import TemplateResponse
from .import_data import *
from .pdf_sanner import scanPdf
from .init import get_linkedin_profile
from .selenium_scrapper import scrape_linkedin
from django.http import HttpResponseRedirect
from .models import UploadForm, Upload, Words
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .model_creater import update_model

# Create your views here.


def cvTemplate(request):
    scanPdf()
    return TemplateResponse(request, 'TemplateCVAnalyzer.html', {'name': importPersonalData()[0],
                                                        'email': importPersonalData()[1],
                                                        'linkedin': importPersonalData()[2],
                                                        'projects': importProjectData(),
                                                        'skills': importSkillsData(),
                                                        'score_programming': importScoreData()[0],
                                                        # 'score_software': importScoreData()[1],
                                                        'score_software': str((int(importScoreData()[1])+int(importScoreData()[0]))/2)[:-2],
                                                        'score_engineering': importScoreData()[2],
                                                        'score_finance': importScoreData()[3],
                                                        'score_management': importScoreData()[4],
                                                        'score_art': importScoreData()[5],
                                                        'score_total': importScoreData()[6],
                                                        })


def cvLinkedIn(request):
    # pro_url= 'https://www.linkedin.com/in/manura-jithmal-de-silva-988b385b/'
    # pro_url= 'https://www.linkedin.com/in/aminda-abeywardana-6aa8b845/'
    # pro_url= 'https://www.linkedin.com/in/chamodsamarajeewa/'
    # pro_url= 'https://www.linkedin.com/in/shatheesh-sohan-b9a0b4b8/'
    # pro_url= 'https://www.linkedin.com/in/mihiran-rajapaksha/'
    pro_url= 'https://www.linkedin.com/in/ksuthagar/'
    # pro_url= 'https://www.linkedin.com/in/anuradha-sithuruwan-a971b7126/'


    get_linkedin_profile(pro_url)
    scrape_linkedin(pro_url)

    return TemplateResponse(request, 'LinkedInAnalyzer.html', {'name': importPersonalDataLinkedIn()[0],
                                                        'occupation': importPersonalDataLinkedIn()[1],
                                                        'summary': importPersonalDataLinkedIn()[2],
                                                        'skills': importPersonalDataLinkedIn()[3],
                                                        'experience': importPersonalDataLinkedIn()[4],
                                                        'courses': importPersonalDataLinkedIn()[5],
                                                        'organizations': importPersonalDataLinkedIn()[6],
                                                        'projects': importProjectDataLinkedIn(),
                                                        'skills_endoresed': importSkillsLinkedIn(),
                                                        'score_software': str((int(importScoreDataLinkedIn()[1]) + int(
                                                           importScoreData()[0])) / 2)[:-2],
                                                        'score_engineering': importScoreDataLinkedIn()[2],
                                                        'score_finance': importScoreDataLinkedIn()[3],
                                                        'score_management': importScoreDataLinkedIn()[4],
                                                        'score_art': importScoreDataLinkedIn()[5],
                                                        'score_total': int(importScoreDataLinkedIn()[6])+int(import_endoresed_data()[0]),
                                                        })


# login view.
class LoginPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'SignIn.html', context=None)


# dashboard view.
class DashboardView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'Dashboard.html', context=None)


def upload_file(request):
    if request.method == "POST":
        resume = UploadForm(request.POST, request.FILES)
        if resume.is_valid():
            resume.save()
            file = resume.cleaned_data.get('resume')
            # docToDel = get_object_or_404(Upload, pk=len(Upload.objects.all()))
            # print("deleted_id " + docToDel.resume.url)
            # print(file.name)
            # print(file.file)
            update_model(file.file)
            # print(file.url)
            return HttpResponseRedirect(reverse('resume_upload'))
    else:
        resume = UploadForm()
    resumes = Upload.objects.all()
    # print(len(Upload.objects.all()))
    # return render(request, 'Upload.html', {'form': img, 'images': images})
    return TemplateResponse(request, 'Upload.html', {'form': resume, 'resumes': resumes})


def delete_file(request):
    # if request.method != 'POST':
    #     raise HTTP404
    if request.method == "POST":
        docId = request.POST.get('docfile', None)
        print("docid "+docId)
        docToDel = get_object_or_404(Upload, pk=docId)
        print("deleted_id "+docToDel.resume.url)
        docToDel.resume.delete()
        print()
        docToDel.delete()
        return HttpResponseRedirect(reverse('resume_upload'))
    else:
        resume = UploadForm()
    resumes = Upload.objects.all()
    # print()
    # return render(request, 'Upload.html', {'form': img, 'images': images})
    return TemplateResponse(request, 'Upload.html', {'form': resume, 'resumes': resumes})


def delete_all(request):
    # if request.method == "GET":
    #     for docToDel in Upload.objects.all():
    #         docToDel.resume.delete()
    #         docToDel.delete()
    #     Upload.objects.all().delete()
    #     return HttpResponseRedirect(reverse('resume_upload'))
    # else:
    #     resume = UploadForm()
    # resumes = Upload.objects.all()
    # return TemplateResponse(request, 'Upload.html', {'form': resume, 'resumes': resumes})
    for docToDel in Upload.objects.all():
        docToDel.resume.delete()
        # docToDel.delete()
    Upload.objects.all().delete()
    # for docToDel in Words.objects.all():
    #     docToDel.delete()
    Words.objects.all().delete()
    return HttpResponseRedirect(reverse('resume_upload'))


def home(request):
    return TemplateResponse(request, 'Home.html')