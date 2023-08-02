from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


def tab(request):
    return render(request, 'main_tab/main_tab.html')
