from django.contrib import admin
# Register your models here.

from jobs.models import Portal ,JobTitle,JobDescription,Applicant


admin.site.register(JobDescription) #djangodocs
admin.site.register(Applicant)
admin.site.register(Portal)
admin.site.register(JobTitle)