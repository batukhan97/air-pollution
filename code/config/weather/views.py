from django.shortcuts import render
import requests
import datetime


def get_home_view(request):
    TOKEN = '5bf3894683ac16ad62b5b77119f6c058'
    LONGITUDE = '43.25'
    LATITUDE = '76.95'
    CURRENT_AIR_POLLUTION_URL = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={LATITUDE}&lon={LONGITUDE}&appid={TOKEN}'

    response = requests.get(CURRENT_AIR_POLLUTION_URL)

    labels = [x for x in response.json()['list'][0]['components']]
    data = [x[1] for x in response.json()['list'][0]['components'].items()]
    unix_timestamp = response.json()['list'][0]['dt']
    current_human_time = datetime.datetime.fromtimestamp(unix_timestamp)

    context = {
        'labels': labels,
        'data': data,
        'time': current_human_time
    }

    return render(request, 'weather/home.html', context)
