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
        return self.name + " " + self.description

    def launch(self):
        self.save()

class JobTitle(models.Model):
    title = models.CharField(max_length=250)
    last_updated = models.DateField(default=timezone.now)

    portal = models.ForeignKey(Portal, on_delete=Portal)
