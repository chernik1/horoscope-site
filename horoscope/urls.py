from django.contrib import admin
from django.urls import path, include
from horoscope import views

urlpatterns = [
    path('type/', views.type),
    path('type/<str:sign_zodiac_element>', views.sign_zodiac_element),
    path('', views.index, name='horoscope-index'),
    path('<int:sign_zodiac_number>/', views.zodiac_by_number),
    path('<str:sign_zodiac>/', views.zodiac, name = 'horoscope-name'),
    path('<int:month>/<int:day>', views.zodiac_by_date)
]
