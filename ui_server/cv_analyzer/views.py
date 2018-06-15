# from urllib import request

from django.shortcuts import render
from django.views.generic import TemplateView
from django.template.response import TemplateResponse
from .import_data import *
from .pdf_sanner import scanPdf
from .init import get_linkedin_profile
from .selenium_scrapper import scrape_linkedin
from django.http import HttpResponseRedirect
from .models import UploadForm, Upload, Words, UploadFormCV, UploadCV, Skills
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .model_creater import update_model
from .model_scorer import score_resume
import json

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

    if request.method == "POST":
        docId = request.POST.get('docfile', None)
        profile = get_object_or_404(UploadCV, pk=docId)

        # pro_url= 'https://www.linkedin.com/in/manura-jithmal-de-silva-988b385b/'
        # pro_url= 'https://www.linkedin.com/in/aminda-abeywardana-6aa8b845/'
        # pro_url= 'https://www.linkedin.com/in/chamodsamarajeewa/'
        # pro_url= 'https://www.linkedin.com/in/shatheesh-sohan-b9a0b4b8/'
        # pro_url= 'https://www.linkedin.com/in/mihiran-rajapaksha/'
        # pro_url= 'https://www.linkedin.com/in/ksuthagar/'
        # pro_url= 'https://www.linkedin.com/in/anuradha-sithuruwan-a971b7126/'

        return TemplateResponse(request, 'LinkedInAnalyzer.html', {'name': profile.name,
                                                            'occupation': profile.occupation,
                                                            'summary': profile.summary,
                                                            'skills': profile.skills,
                                                            'experience': profile.experience,
                                                            'courses': profile.courses,
                                                            'organizations': profile.organizations,
                                                            'projects': json.loads(profile.projects),
                                                            'skills_endoresed': json.loads(profile.skills_endoresed),
                                                            'score_programming': profile.score_programming,
                                                            'score_software': profile.score_software,
                                                            'score_engineering': profile.score_engineering,
                                                            'score_finance': profile.score_finance,
                                                            'score_management': profile.score_management,
                                                            'score_art': profile.score_art,
                                                            'score_total': profile.score_total,
                                                            'pic_path': profile.pic_path,
                                                            'gpa' : profile.gpa
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
            update_model(file.file)
            return HttpResponseRedirect(reverse('resume_upload'))
    else:
        resume = UploadForm()
    resumes = Upload.objects.all()
    return TemplateResponse(request, 'Upload.html', {'form': resume, 'resumes': resumes})


def delete_file(request):
    # if request.method != 'POST':
    #     raise HTTP404
    if request.method == "POST":
        docId = request.POST.get('docfile', None)
        # print("docid "+docId)
        docToDel = get_object_or_404(Upload, pk=docId)
        # print("deleted_id "+docToDel.resume.url)
        docToDel.resume.delete()
        # print()
        docToDel.delete()
        return HttpResponseRedirect(reverse('resume_upload'))
    else:
        resume = UploadForm()
    resumes = Upload.objects.all()
    return TemplateResponse(request, 'Upload.html', {'form': resume, 'resumes': resumes})


def delete_all(request):
    for docToDel in Upload.objects.all():
        docToDel.resume.delete()
    Upload.objects.all().delete()
    Words.objects.all().delete()
    return HttpResponseRedirect(reverse('resume_upload'))


def home(request):
    return TemplateResponse(request, 'Home.html')


def upload_file_cv(request):
    if request.method == "POST":
        resume = UploadFormCV(request.POST, request.FILES)
        if resume.is_valid():
            file = resume.cleaned_data.get('resume_do')
            linked_in, score_value, gpa_value = score_resume(file.file)
            # print("linked in url in cv is - " + linked_in)
            pro_url_splitted = linked_in.split('/')
            if (len(pro_url_splitted[-1]) > 5):
                pro_url = 'https://www.linkedin.com/in/' + pro_url_splitted[-1]
            else:
                pro_url = 'https://www.linkedin.com/in/' + pro_url_splitted[-2]
            # if 'http' not in pro_url:
            #     pro_url = 'https://'+pro_url
            print("linked in url refactored is - " + pro_url)
            get_linkedin_profile(pro_url)
            scrape_linkedin(pro_url)
            print('DATA COLLECTION IS OVER !!!!!!!!!!!!!!!!!!!!!!!!')
            obj = resume.save(commit=False)
            obj.score = score_value
            obj.link_url = pro_url
            obj.gpa = gpa_value

            # 'score_software': str((int(importScoreDataLinkedIn()[1]) + int(
            #     importScoreData()[0])) / 2)[:-2],

            obj.name = importPersonalDataLinkedIn()[0]
            obj.occupation = importPersonalDataLinkedIn()[1]
            obj.summary = importPersonalDataLinkedIn()[2]
            obj.skills = importPersonalDataLinkedIn()[3]
            obj.experience = importPersonalDataLinkedIn()[4]
            obj.courses = importPersonalDataLinkedIn()[5]
            obj.organizations = importPersonalDataLinkedIn()[6]
            obj.projects = json.dumps(importProjectDataLinkedIn())
            obj.skills_endoresed = json.dumps(importSkillsLinkedIn())
            obj.score_endoresed = int(import_endoresed_data()[0])
            obj.score_programming = int(importScoreDataLinkedIn()[0])
            obj.score_software = int(importScoreDataLinkedIn()[1])
            obj.score_engineering = int(importScoreDataLinkedIn()[2])
            obj.score_finance = int(importScoreDataLinkedIn()[3])
            obj.score_management = int(importScoreDataLinkedIn()[4])
            obj.score_art = int(importScoreDataLinkedIn()[5])
            obj.score_total = get_total_score(score_value, gpa_value)
            obj.pic_path = "static/images/profile_pictures/" + pro_url[27:] + ".png"
            obj.save()
            # print(UploadCV.objects.all())
            return HttpResponseRedirect(reverse('cv_upload'))
    else:
        resume = UploadFormCV()
    resumes = UploadCV.objects.all()
    # resumes = UploadCV.objects.order_by('-upload_date')
    # print(UploadCV.objects.all())
    return TemplateResponse(request, 'UploadCV.html', {'form': resume, 'resumes': resumes})


def delete_file_cv(request):
    if request.method == "POST":
        docId = request.POST.get('docfile', None)
        # print("docid "+docId)
        docToDel = get_object_or_404(UploadCV, pk=docId)
        # print("deleted_id "+docToDel.resume_do.url)
        docToDel.resume_do.delete()
        docToDel.delete()
        return HttpResponseRedirect(reverse('cv_upload'))
    else:
        resume = UploadFormCV()
    resumes = UploadCV.objects.all()
    return TemplateResponse(request, 'UploadCV.html', {'form': resume, 'resumes': resumes})


def delete_all_cv(request):
    for docToDel in UploadCV.objects.all():
        docToDel.resume_do.delete()
        # docToDel.delete()
    UploadCV.objects.all().delete()
    return HttpResponseRedirect(reverse('cv_upload'))


def analysis(request):
    resumes = UploadCV.objects.order_by('-score')
    return TemplateResponse(request, 'Analysis.html', {'resumes': resumes})


def get_total_score(score,gpa):
    model_score = score/int(import_word_count()[0])*50
    endoresement_score = int(import_endoresed_data()[0])/100*10
    section_score = int(importScoreDataLinkedIn()[6])/100*20
    gpa_score = gpa/4.2*20
    print('model score is ' + str(model_score))
    print('endorsement score is ' + str(endoresement_score))
    print('section score is ' + str(section_score))
    print('gpa score is ' + str(gpa_score))
    print('total score is ' + str(model_score+endoresement_score+section_score+gpa_score))
    return int(model_score+endoresement_score+section_score+gpa_score)


def add_skills(request):
    skills_front_end = Skills.objects.filter(category='Front-end')
    skills_back_end = Skills.objects.filter(category='Back-end')
    skills_quality_assurance = Skills.objects.filter(category='Quality Assurance')
    skills_business_analysis = Skills.objects.filter(category='Business Analysis')
    skills_database = Skills.objects.filter(category='Database')
    return TemplateResponse(request, 'AddSkills.html', {'skills_front_end': skills_front_end,
                                                        'skills_back_end': skills_back_end,
                                                        'skills_quality_assurance': skills_quality_assurance,
                                                        'skills_business_analysis': skills_business_analysis,
                                                        'skills_database': skills_database})


def add_skill(request):
    if request.method == "POST":
        skill = request.POST.get('skill', None)
        category = request.POST.get('category', None)
        priority = request.POST.get('priority', None)
        obj_list = Skills.objects.filter(skill=skill)

        priority_class = ""
        if priority == "High":
            priority_class = "badge bgc-red-50 c-red-700 p-10 lh-0 tt-c badge-pill"
        elif priority == "Medium":
            priority_class = "badge bgc-green-50 c-green-700 p-10 lh-0 tt-c badge-pill"
        else:
            priority_class = "badge bgc-blue-50 c-blue-700 p-10 lh-0 tt-c badge-pill"

        if len(obj_list) > 0:
            print("do nothing")
        else:
            s = Skills(skill=skill, category=category, priority=priority, priority_class=priority_class)
            s.save()
        return HttpResponseRedirect(reverse('skills_add'))
    else:
        resume = UploadFormCV()
    resumes = UploadCV.objects.all()
    return TemplateResponse(request, 'UploadCV.html', {'form': resume, 'resumes': resumes})


def delete_skill(request):
    if request.method == "POST":
        doc_id = request.POST.get('id', None)
        doc_to_del = get_object_or_404(Skills, pk=doc_id)
        doc_to_del.delete()
        return HttpResponseRedirect(reverse('skills_add'))
    else:
        return HttpResponseRedirect(reverse('skills_add'))