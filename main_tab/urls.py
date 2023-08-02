from django.contrib import admin
from django.urls import path, include
from main_tab import views
urlpatterns = [
    path('', views.tab),
]