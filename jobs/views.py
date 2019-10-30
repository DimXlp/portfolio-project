from django.shortcuts import render

from .models import Job # added 41

"""
    Added by me.
    Homepage is inside Job app
    because the Jobs are being shown
    in the Homepage
"""

def home(request):
    jobs = Job.objects # added, gets all the jobs from the db and turns them to python objects
    return render(request, 'jobs/home.html', {'jobs': jobs});
