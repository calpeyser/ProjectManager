from django.contrib import admin
from project_manager.models import User, Project, Label


admin.site.register(User)
admin.site.register(Project)
admin.site.register(Label)
