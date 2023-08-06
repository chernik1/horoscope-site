from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from .models import Zodiac
from first.settings import INTERNAL_IPS

main_urls = INTERNAL_IPS[0]
dict_month_day = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

zodiac_dict_by_data = {
    'aries': ('03.21', '04.20'),
    'taurus': ('04.21', '05.21'),
    'gemini': ('05.22', '06.21'),
    'cancer': ('06.22', '07.22'),
    'leo': ('07.23', '08.21'),
    'virgo': ('08.22', '09.23'),
    'libra': ('09.24', '10.23'),
    'scorpio': ('10.24', '11.22'),
    'sagittarius': ('11.23', '12.22'),
    'capricorn': ('12.23', '01.20'),
    'aquarius': ('01.21', '02.19'),
    'pisces': ('02.20', '03.20'),
}


def index(request):
    """ Function for menu."""
    zodiacs = Zodiac.objects.all()
    context = {
        'zodiacs': zodiacs,
        'main_urls': main_urls,
    }
    return render(request, 'horoscope/index.html', context=context)


def zodiac(request, sign_zodiac: str):
    """ Function for show zodiacs. """
    zodiac = get_object_or_404(Zodiac, name=sign_zodiac.title())
    zodiacs = Zodiac.objects.all()
    data = {
        'zodiac': zodiac,
        'zodiacs': zodiacs,
        'main_urls': main_urls,
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def zodiac_by_number(request, sign_zodiac_number: int):
    """ Function for search zodiacs with help number.
    For example - /horoscope/5/"""
    zodiacs = Zodiac.objects.all()
    if int(sign_zodiac_number) > len(zodiacs) or int(sign_zodiac_number) <= 0:
        return HttpResponseNotFound(f'Not number {sign_zodiac_number}')
    name_zodiac = Zodiac.objects.get(number=sign_zodiac_number)
    redirect_url = reverse('horoscope-name', args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)


def elements(request):
    """ Function for show elements.
    /horoscope/elements/ """
    zodiacs = Zodiac.objects.all()
    data = {
        'elements_list': ['Fire', 'Air', 'Earth', 'Water'],
        'zodiacs': zodiacs,
        'main_urls': main_urls,
    }
    return render(request, 'horoscope/elements.html', context=data)


def sign_zodiac_element(request, sign_element: str):
    """ Function for zodiac search about elements."""
    zodiac_element_list = []
    zodiacs = Zodiac.objects.all()
    for zodiac in zodiacs:
        if zodiac.element == sign_element.title():
            zodiac_element_list.append(zodiac.name)
    data = {
        'zodiacs_element_list': zodiac_element_list,
        'sign_element': sign_element,
        'zodiacs': zodiacs,
        'main_urls': main_urls,
    }
    return render(request, 'horoscope/info_zodiac_element.html', context=data)


def zodiac_by_date(request, month, day):
    """ Function for search zodiacs. horoscope/month/day/"""
    if month > 0 and month <= 12:
        if day > 0 and dict_month_day[month] >= day:
            for key in zodiac_dict_by_data.keys():
                if int(zodiac_dict_by_data[key][0].split('.')[0]) == month:
                    if int(zodiac_dict_by_data[key][0].split('.')[1]) >= day:
                        redirect_url = reverse('horoscope-name', args=(key,))
                        return HttpResponseRedirect(redirect_url)
                elif int(zodiac_dict_by_data[key][0].split('.')[0]) == month - 1:
                    if int(zodiac_dict_by_data[key][1].split('.')[1]) >= day:
                        redirect_url = reverse('horoscope-name', args=(key,))
                        return HttpResponseRedirect(redirect_url)
                else:
                    continue
        else:
            return HttpResponseNotFound('Input error.')
    else:
        return HttpResponseNotFound('Input error.')
