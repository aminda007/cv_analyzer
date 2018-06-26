# from urllib import request

from django.shortcuts import render
from django.views.generic import TemplateView
from django.template.response import TemplateResponse
from .linked_in_scrapper import LinkedInScrapper
from .app_variables import AppVariables
from .import_data import *
from .selenium_scrapper import scrape_linkedin
from django.http import HttpResponseRedirect
from .models import UploadForm, Upload, Words, UploadFormCV, UploadCV, Skills, Questions
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .model_creater import update_model
from .model_scorer import score_resume
import json
from .answering import Answering
from .model_checker import ModelChecker

# show the summary of resume profile with scrapped linked in data
def cvLinkedIn(request):

    if request.method == "POST":
        docId = request.POST.get('docfile', None)
        profile = get_object_or_404(UploadCV, pk=docId)

        return TemplateResponse(request, 'LinkedInAnalyzer.html', {'name': profile.name,
                                                            'occupation': profile.occupation,
                                                            'summary': profile.summary,
                                                            'skills': profile.skills,
                                                            'experience': profile.experience,
                                                            'courses': profile.courses,
                                                            'organizations': profile.organizations,
                                                            'projects': json.loads(profile.projects),
                                                            'skills_endoresed': json.loads(profile.skills_endoresed),
                                                            'score_front_end': profile.score_front_end,
                                                            'score_back_end': profile.score_back_end,
                                                            'score_quality_assurance': profile.score_quality_assurance,
                                                            'score_business_analysis': profile.score_business_analysis,
                                                            'score_database': profile.score_database,
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
    if request.method == "POST":
        docId = request.POST.get('docfile', None)
        docToDel = get_object_or_404(Upload, pk=docId)
        docToDel.resume.delete()
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


def get_edu_score():
    edu = importPersonalDataLinkedIn()[5].strip().lower()
    print(edu)
    if edu in "doctor":
        edu_score = 0.4
    elif edu in "master":
        edu_score = 0.3
    elif edu in "bachelor":
        edu_score = 0.2
    else:
        edu_score = 0.1
    return edu_score


def upload_file_cv(request):
    if request.method == "POST":
        resume = UploadFormCV(request.POST, request.FILES)
        if resume.is_valid():
            file = resume.cleaned_data.get('resume_do')
            linked_in, score_value, gpa_value = score_resume(file.file)
            pro_url_splitted = linked_in.split('/')
            if (len(pro_url_splitted[-1]) > 5):
                pro_url = 'https://www.linkedin.com/in/' + pro_url_splitted[-1]
            else:
                pro_url = 'https://www.linkedin.com/in/' + pro_url_splitted[-2]
            print("linked in url refactored is - " + pro_url)
            LinkedInScrapper().scrape_one_profile(pro_url)
            if scrape_linkedin(pro_url):
                print('DATA COLLECTION IS OVER !!!!!!!!!!!!!!!!!!!!!!!!')
                obj = resume.save(commit=False)
                obj.score = score_value
                obj.link_url = pro_url
                obj.gpa = gpa_value
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
                obj.score_front_end = int(importScoreDataLinkedIn()[0])
                obj.score_back_end = int(importScoreDataLinkedIn()[1])
                obj.score_quality_assurance = int(importScoreDataLinkedIn()[2])
                obj.score_business_analysis = int(importScoreDataLinkedIn()[3])
                obj.score_database = int(importScoreDataLinkedIn()[4])
                obj.score_education = get_edu_score()
                obj.score_total = get_total_score(score_value, gpa_value, obj.score_education)
                obj.pic_path = "static/images/profile_pictures/" + pro_url[27:] + ".png"
                obj.save()
                return HttpResponseRedirect(reverse('cv_upload'))
    else:
        resume = UploadFormCV()

    resumes = UploadCV.objects.all()
    return TemplateResponse(request, 'UploadCV.html', {'form': resume, 'resumes': resumes})


def delete_file_cv(request):
    if request.method == "POST":
        docId = request.POST.get('docfile', None)
        docToDel = get_object_or_404(UploadCV, pk=docId)
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
    UploadCV.objects.all().delete()
    return HttpResponseRedirect(reverse('cv_upload'))


def analysis(request):
    resumes = UploadCV.objects.order_by('-score_total')
    return TemplateResponse(request, 'Analysis.html', {'resumes': resumes})


def get_total_score(score, gpa, edu_score):
    model_score = score*50
    endoresement_score = int(import_endoresed_data()[0])/100*10
    section_score = int(importScoreDataLinkedIn()[5])/100*30
    gpa_score = gpa/4.2*10
    edu_score = min(edu_score, 1)*10
    print('model score is ' + str(model_score))
    print('endorsement score is ' + str(endoresement_score))
    print('section score is ' + str(section_score))
    print('gpa score is ' + str(gpa_score))
    print('education score is ' + str(edu_score))
    print('total score is ' + str(model_score+endoresement_score+section_score+gpa_score+edu_score))
    return int(model_score+endoresement_score+section_score+gpa_score+edu_score)


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
        if priority == "Very High":
            priority_class = "badge bgc-red-50 c-red-700 p-10 lh-0 tt-c badge-pill"
        elif priority == "Medium":
            priority_class = "badge bgc-green-50 c-green-700 p-10 lh-0 tt-c badge-pill"
        else:
            priority_class = "badge bgc-blue-50 c-blue-700 p-10 lh-0 tt-c badge-pill"

        if len(obj_list) > 0:
            print("do nothing")
        else:
            if skill != '':
                s = Skills(skill=skill.lower(), category=category, priority=priority, priority_class=priority_class)
                s.save()
        return HttpResponseRedirect(reverse('skills_add'))
    else:
        return HttpResponseRedirect(reverse('skills_add'))


def delete_skill(request):
    if request.method == "POST":
        doc_id = request.POST.get('id', None)
        doc_to_del = get_object_or_404(Skills, pk=doc_id)
        doc_to_del.delete()
        return HttpResponseRedirect(reverse('skills_add'))
    else:
        return HttpResponseRedirect(reverse('skills_add'))



def qa(request):
    if request.method == "POST":
        question_context = request.POST.get('question_context', None)
        question = request.POST.get('question', None)
        true_answer = request.POST.get('true_answer', None)
        answering = Answering()
        answer = answering.get_answer(question_context, question)
        print("answer is: "+ answer)
        return TemplateResponse(request, 'qa.html', {'question_context': question_context, 'question': question, 'true_answer': true_answer, 'answer': answer})
    else:
        question_context = request.GET.get('question_context')
        question = request.GET.get('question')
        true_answer = request.GET.get('true_answer')
        return TemplateResponse(request, 'qa.html', {'question_context': question_context, 'question': question, 'true_answer': true_answer, 'answer': ""})


def qna_train(request):
    qalist = Answering().get_qna_list()
    return TemplateResponse(request, 'QnATrain.html', {'qalist': json.loads(qalist)})

def get_ttl_score():
    total = 0
    questions = Questions.objects.all()
    for i in questions:
        total = total + i.score
    return total/len(questions)


def interview(request):

    if request.method == "POST":
        AppVariables.q_count = 1 + AppVariables.q_count
        print("posting")
        context = request.POST.get('question_context', None)
        q = request.POST.get('question', None)
        # ta = request.POST.get('true_answer', None)
        a = request.POST.get('answer', None)
        answering = Answering()
        predicted_answer = answering.get_answer(context, q)
        score = ModelChecker().get_score(predicted_answer, a)
        ques = Questions(question_context=context, question=q, true_answer=predicted_answer, answer=a, score=score*100)
        ques.save()
        if AppVariables.q_count == 5:
            AppVariables.q_count = 0
            questions = Questions.objects.all()
            score_total = get_ttl_score()
            return TemplateResponse(request, 'AnswerAnalysis.html',{'questions': questions, 'score_total': score_total})
        else:
            question_context, question, true_answer = Answering().get_qna()
            return TemplateResponse(request, 'QnAInterview.html', {'question_context': question_context, 'question': question, 'true_answer': true_answer, 'answer': ""})


def select_category(request):
    Questions.objects.all().delete()
    AppVariables.q_count = 0
    return TemplateResponse(request, 'QnACategory.html', None)


def save_category(request):
    if request.method == "POST":
        category = request.POST.get('category', None)
        AppVariables.q_count = 0
        AppVariables.qna_category = category
        question_context, question, true_answer = Answering().get_qna()
        return TemplateResponse(request, 'QnAInterview.html', {'question_context': question_context, 'question': question, 'true_answer': true_answer, 'answer': ""})