from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

types = {
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
    zodiacs = list(zodiac_dict)
    """
    <ol>
        <li>aries</li>
        <li>taurus</li>
        <li>gemini</li>
        <li>cancer</li>
        <li>leo</li>
        <li>virgo</li>
        <li>libra</li>
        <li>scorpio</li>
        <li>sagittarius</li>
        <li>capricorn</li>
        <li>aquarius</li>
        <li>pisces</li>
    </ol>
    """
    li_elements = ''
    for sign in zodiacs:
        redirect_path = reverse('horoscope-name', args=[sign])
        li_elements += f"<li> <a href='{redirect_path}'>{sign.title()} </a> </li>"
    response = f"""
    <ul>
        {li_elements}
    </ul>
    """
    return HttpResponse(response)


def zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    data = {
        'description_zodiac': description,
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def zodiac_by_number(request, sign_zodiac_number: int):
    zodiacs = list(zodiac_dict)
    if int(sign_zodiac_number) > len(zodiacs):
        return HttpResponseNotFound(f'Номера {sign_zodiac_number} нету')
    name_zodiac = zodiacs[sign_zodiac_number - 1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)


def type(request):
    """
    <ol>
        <li>Fire</li>
        <li>Earth</li>
        <li>Air</li>
        <li>Water</li>
    </ol>
    """
    li_elements = ''
    for sign in types.keys():
        redirect_path = sign.lower()
        li_elements += f"<li> <a href='{redirect_path}'>{sign.title()} </a> </li>"
    response = f"""
        <ul>
            {li_elements}
        </ul>
        """
    return HttpResponse(response)


def sign_zodiac_element(request, sign_zodiac_element: str):
    if sign_zodiac_element in types:
        li_elements = ''
        zodiac_list = types[sign_zodiac_element]
        for zodiac in zodiac_list:
            li_elements += f"<li> <a href='{zodiac.lower()}'>{zodiac.title()} </a> </li>"
        response = f"""
            <ul>
                {li_elements}
            </ul>
            """
        return HttpResponse(li_elements)
    else:
        if sign_zodiac_element in zodiac_dict:
            redirect_url = reverse('horoscope-name', args=(sign_zodiac_element,))
            return HttpResponseRedirect(redirect_url)
        return HttpResponseNotFound(f'Элемента {sign_zodiac_element} нету')

def zodiac_by_date(request, month, day):
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
            return HttpResponseNotFound('Ошибка ввода')
    else:
        return HttpResponseNotFound('Ошибка ввода')

