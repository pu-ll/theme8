import requests

town = input()
try:
    url = 'https://api.weatherapi.com/v1/current.json?key=e4a510c30eec4bb29b0205452261311&q=' + town
    response = requests.get(url).json()

    #Построчный вывод текущей температуру и описание погоды
    print(f'Name: {response['location']['name']}, Country: {response['location']['country']}')
    print(f'Last Updated: {response['current']['last_updated']}')
    print(f'Temperature: {response['current']['temp_c']}°C')
    print(f'Condition: {response['current']['condition']['text']}')
    print(f'Wind: {round(response['current']['wind_kph'] * 1000 / 3600, 2)} m/s')
    print(f'Pressure: {round(response['current']['pressure_mb'] * 0.75006, 2)} mm Hg')
except KeyError:
    print('Не существует такого названия населенного пункта в базе')
