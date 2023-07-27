from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
# def leo(request):
#     return HttpResponse('Знак зодиака - лев')
#
# def scorpio(request):
#     return HttpResponse('Знак зодиака - скорпион')
#
# def aries(request):
#     return HttpResponse('Знак зодиака - овен')
#
# def taurus(request):
#     return  HttpResponse('Знак зодиака - телец')
#
# def gemini(request):
#     return  HttpResponse('Знак зодиака - близнецы')
#
# def cancer(request):
#     return  HttpResponse('Знак зодиака - рак')
#
# def virgo(request):
#     return HttpResponse('Знак зодиака - дева')
#
# def libra(request):
#     return  HttpResponse('Знак зодиака - весы')
#
# def sagittarius(request):
#     return HttpResponse('Знак зодиака - стрелец')
#
# def capricorn(request):
#     return HttpResponse('Знак зодиака - козерог')
#
# def aquarius(request):
#     return HttpResponse('Знак зодиака - водолей')
#
# def pisces(request):
#     return HttpResponse('Знак зодиака - рыбы')

def zodiac(request, sign_zodiac):
    if sign_zodiac == 'leo':
        return HttpResponse('Знак зодиака - лев')
    elif sign_zodiac == 'scorpio':
        return HttpResponse('Знак зодиака - скорпион')
    elif sign_zodiac == 'pisces':
        return HttpResponse('Знак зодиака - рыбы')
    elif sign_zodiac == 'aquarius':
        return HttpResponse('Знак зодиака - водолей')
    elif sign_zodiac == 'capricorn':
        return HttpResponse('Знак зодиака - козерог')
    elif sign_zodiac == 'sagittarius':
        return HttpResponse('Знак зодиака - стрелец')
    elif sign_zodiac == 'libra':
        return HttpResponse('Знак зодиака - весы')
    elif sign_zodiac == 'virgo':
        return HttpResponse('Знак зодиака - дева')
    elif sign_zodiac == 'cancer':
        return HttpResponse('Знак зодиака - рак')
    elif sign_zodiac == 'gemini':
        return HttpResponse('Знак зодиака - близнецы')
    elif sign_zodiac == 'taurus':
        return HttpResponse('Знак зодиака - телец')
    elif sign_zodiac == 'aries':
        return HttpResponse('Знак зодиака - овен')
    else:
        return HttpResponseNotFound(f'Неизвестный знак зодиака - {sign_zodiac}')