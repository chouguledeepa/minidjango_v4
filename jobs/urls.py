from django.urls import path, re_path

from . import views

urlpatterns=[
    re_path(r"^wel*", views.welcome,name='welcome'),
    path("portal/",views.portal_details,name="details"),
    path("<int:job_id>/",views.job_description, name='JD')

]
