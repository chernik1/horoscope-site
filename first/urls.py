"""
URL configuration for first project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from horoscope import views

urlpatterns = [
    path('horoscope/<sign_zodiac>/', views.zodiac),
    # path('admin/', admin.site.urls),
    # path('horoscope/leo/', views.leo),
    # path('horoscope/scorpio/', views.scorpio),
    # path('horoscope/aries/', views.aries),
    # path('horoscope/taurus/', views.taurus),
    # path('horoscope/gemini/', views.gemini),
    # path('horoscope/cancer/', views.cancer),
    # path('horoscope/virgo/', views.virgo),
    # path('horoscope/libra/', views.libra),
    # path('horoscope/sagittarius/', views.sagittarius),
    # path('horoscope/capricorn/', views.capricorn),
    # path('horoscope/aquarius/', views.aquarius),
    # path('horoscope/pisces/', views.pisces),
]
