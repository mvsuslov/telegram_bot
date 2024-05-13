import requests

def api_func_wth(city, api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        #print(data)
        temper = data.get('main').get('temp')
        humidity = data.get('main').get('humidity')
        speed = data.get('wind').get('speed')
        return temper, humidity, speed
    else:
        return None