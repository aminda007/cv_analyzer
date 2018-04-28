from django.db import models
from django.forms import ModelForm


class Upload(models.Model):
    resume = models.FileField(upload_to="resumes/")
    upload_date=models.DateTimeField(auto_now_add =True)

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
