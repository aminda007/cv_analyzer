from django.db import models
from django.forms import ModelForm


class Upload(models.Model):
    resume = models.FileField(upload_to="resumes/")
    upload_date = models.DateTimeField(auto_now_add=True)

# FileUpload form class.


class UploadForm(ModelForm):
    class Meta:
        model = Upload
        fields = ('resume',)


class Words(models.Model):
    word = models.CharField(max_length=50)
    count = models.IntegerField()

    def __str__(self):
        return self.word + ' ' + str(self.count)


class UploadCV(models.Model):
    resume_do = models.FileField(upload_to="resumes_do/")
    upload_date = models.DateTimeField(auto_now_add=True)
    link_url = models.CharField(max_length=150)
    score = models.IntegerField()
    gpa = models.FloatField()
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    summary = models.CharField(max_length=1000)
    skills = models.CharField(max_length=80)
    experience = models.CharField(max_length=200)
    courses = models.CharField(max_length=300)
    organizations = models.CharField(max_length=500)
    projects = models.CharField(max_length=5000)
    skills_endoresed = models.CharField(max_length=500)
    score_endoresed = models.IntegerField()
    score_programming = models.IntegerField()
    score_software = models.IntegerField()
    score_engineering = models.IntegerField()
    score_finance = models.IntegerField()
    score_management = models.IntegerField()
    score_art = models.IntegerField()
    score_total = models.IntegerField()
    pic_path = models.CharField(max_length=100)

    def __str__(self):
        return self.link_url + ' ' + str(self.score)
# FileUpload form class.


class UploadFormCV(ModelForm):
    class Meta:
        model = UploadCV
        fields = ('resume_do',)


class Skills(models.Model):
    skill = models.CharField(max_length=50)
    category = models.CharField(max_length=30)
    priority = models.CharField(max_length=10)
    priority_class = models.CharField(max_length=100)

    def __str__(self):
        return self.category + ' ' + str(self.count)