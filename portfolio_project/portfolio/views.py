from django.shortcuts import render, redirect
from django.http import FileResponse
from .models import Project, Skill, ContactMessage
from django.http import FileResponse, Http404
from django.conf import settings
import os

ALERT_MESSAGE = "🚀 Welcome to my AI-powered Portfolio! 👨‍💻✨ Let's build the future together! 💡"

def home(request):
    return render(request, 'home.html', {'alert': ALERT_MESSAGE})

def about(request):
    return render(request, 'about.html', {'alert': ALERT_MESSAGE})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects, 'alert': ALERT_MESSAGE})

def skills(request):
    skills = Skill.objects.all()
    return render(request, 'skills.html', {'skills': skills, 'alert': ALERT_MESSAGE})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        ContactMessage.objects.create(name=name, email=email, message=message)
        return render(request, 'contact.html', {'alert': ALERT_MESSAGE, 'success': True})
    return render(request, 'contact.html', {'alert': ALERT_MESSAGE})

def resume(request):
    file_path = os.path.join(settings.BASE_DIR, 'portfolio/static/resume/sravanth-kumar-resume-main.pdf')
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    else:
        raise Http404("Resume not found.")