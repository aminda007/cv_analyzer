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

    def __str__(self):
        return self.link_url + ' ' + str(self.score)
# FileUpload form class.


class UploadFormCV(ModelForm):
    class Meta:
        model = UploadCV
        fields = ('resume_do',)