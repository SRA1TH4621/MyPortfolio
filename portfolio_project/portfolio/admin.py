from django.contrib import admin
from .models import Project, Skill, ContactMessage

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(ContactMessage)