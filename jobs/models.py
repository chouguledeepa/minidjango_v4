"""
Python manage.py shell

portal1 = Portal(name="naukri.com", description="famus job website")
portal1.save()

 from jobs.models import Portal
objs =Portal.objects.all()
 for obj in objs:
...     print(obj)
...
naukri.com famus job website
indeed.com NEW

//Particular to get obgects
Portal.objects.get(name="indeed.com")
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.utils import timezone


class Portal(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.CharField(max_length=250)


def __str__(self):
    return self.name


def launch(self):
    self.save()


class JobTitle(models.Model):
    title = models.CharField(max_length=250)
    last_updated = models.DateField(default=timezone.now)
    job_description = models.OneToOneField(
        "jobdescription",on_delete=models.CASCADE
    )
    portal = models.ForeignKey(Portal, on_delete=Portal)

    def __str__(self):
        return self.title + f"({self.portal})"


class JobDescription(models.Model):
    role = models.CharField(max_length=250)
    description_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.role


class Applicant(models.Model):
    name = models.CharField(max_length=240,default="")
    applied_for = models.ForeignKey(
        JobTitle, on_delete=models.CASCADE
    )
    cover_later = models.CharField(max_length=250)

    def __str__(self):
        return self.name
