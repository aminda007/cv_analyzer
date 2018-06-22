from django.test import TestCase

# Create your tests here.

from .models import Words

for i in Words.objects.all():
    print(i)