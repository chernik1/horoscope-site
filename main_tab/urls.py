from django.contrib import admin
from django.urls import path, include
from main_tab import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.tab),
]