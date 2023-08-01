from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from dataclasses import dataclass

zodiac_dict = {
     'aries': 'Aries is the first sign of the zodiac, planet Mars (March 21 to April 20).',
     'taurus': 'Taurus is the second sign of the zodiac, the planet Venus (April 21 to May 21).',
     'gemini': 'Gemini is the third sign of the zodiac, planet Mercury (May 22 to June 21).',
     'cancer': 'Cancer is the fourth sign of the zodiac, the Moon (June 22 to July 22).',
     'leo': 'Leo is the fifth sign of the zodiac, the sun (July 23 to August 21).',
     'virgo': 'Virgo is the sixth sign of the zodiac, planet Mercury (August 22 to September 23).',
     'libra': 'Libra is the seventh sign of the zodiac, planet Venus (September 24 to October 23).',
     'scorpio': 'Scorpio is the eighth sign of the zodiac, the planet Mars (October 24 to November 22).',
     'sagittarius': 'Sagittarius is the ninth sign of the zodiac, planet Jupiter (November 23 to December 22).',
     'capricorn': 'Capricorn is the tenth sign of the zodiac, planet Saturn (December 23 to January 20).',
     'aquarius': 'Aquarius is the eleventh sign of the zodiac, planets Uranus and Saturn (Jan 21 to Feb 19).',
     'pisces': 'Pisces is the twelfth sign of the zodiac, planet Jupiter (February 20 to March 20).',
}

elements_dict = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'water': ['cancer', 'scorpio', 'pisces'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
}

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
    #li_elements += f"<li> <a href='{redirect_path}'>{sign.title()} </a> </li>"
    zodiacs = list(zodiac_dict)
    context = {
        'zodiacs': zodiacs,
        'zodiac_dict': zodiac_dict,
    }
    return render(request, 'horoscope/index.html', context=context)


def zodiac(request, sign_zodiac: str):
    """ Function for show zodiacs. """
    description = zodiac_dict.get(sign_zodiac)
    zodiacs = list(zodiac_dict)
    data = {
        'description_zodiac': description,
        'name_zodiac': sign_zodiac,
        'zodiacs': zodiacs,
        'sign_name': description.split()[0]
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def zodiac_by_number(request, sign_zodiac_number: int):
    """ Function for search zodiacs with help number.
    For example - /horoscope/5/"""
    zodiacs = list(zodiac_dict)
    if int(sign_zodiac_number) > len(zodiacs):
        return HttpResponseNotFound(f'Номера {sign_zodiac_number} нету')
    name_zodiac = zodiacs[sign_zodiac_number - 1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)


def elements(request):
    """ Function for show elements.
    /horoscope/elements/ """
    zodiacs = list(zodiac_dict)
    # li_elements += f"<li> <a href='{redirect_path}'>{sign.title()} </a> </li>"
    data = {
        'elements_dict': elements_dict,
        'zodiacs': zodiacs,
    }
    return render(request, 'horoscope/elements.html', context=data)


def sign_zodiac_element(request, sign_zodiac_element: str):
    """ Function for zodiac search about elements."""
    if sign_zodiac_element in elements_dict:
        zodiacs_list = elements_dict[sign_zodiac_element]
        data = {
            'name': sign_zodiac_element,
            'zodiacs': zodiacs_list,
        }
        return render(request, 'horoscope/info_zodiac_element.html', context=data)
    else:
        return HttpResponseNotFound(f'There is no element - {sign_zodiac_element}')


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
