from django.shortcuts import render
from .models import Job
from apps.models import App


def home(request):
    jobs = Job.objects
    apps = App.objects
    return render(request, 'jobs/home.html', {'jobs': jobs, 'apps': apps})
