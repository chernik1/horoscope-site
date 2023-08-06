from django.contrib import admin
from .models import Zodiac
from django.db.models import QuerySet
from django.contrib.auth.models import User


# Register your models here.

@admin.register(Zodiac)
class ZodiacAdmin(admin.ModelAdmin):
    list_display = ['name', 'photo', 'description', 'element']
    list_per_page = 12
    ordering = ['number']

