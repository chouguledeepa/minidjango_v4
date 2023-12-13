from django.shortcuts import render
from django.http import HttpResponse
from jobs.models import Portal


# Create your views here.

def welcome(request):
    return HttpResponse("<p>welcome to job applications</p>")


def portal_details(request):
    objs = Portal.objects.order_by("id")
    portals = []
    for obj in objs:
        portals.append(obj.name)
    final='=='.join(portals)
    return HttpResponse(f"<p>{final}</p>")

def job_description(request,job_id):
    return HttpResponse(f"<p>{job_id}::"
                        f"This job role require to have good candidate to have "
                        f" experience of django </p>")