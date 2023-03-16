from django.contrib import admin
from .models import *

@admin.register(Articles)
class SettingArticlesAdmin(admin.ModelAdmin):
    pass