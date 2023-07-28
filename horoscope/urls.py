from django.contrib import admin
from django.urls import path, include
from horoscope import views

urlpatterns = [
    path('<int:sign_zodiac_number>/', views.zodiac_by_number),
    path('<str:sign_zodiac>/', views.zodiac),
]
