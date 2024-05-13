from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
import config

# Функция для отправки сообщения с кнопками выбора города
async def send_city_buttons(chat_id):
    markup = InlineKeyboardMarkup()
    cities = ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург', 'Казань', 'Челябинск'] # Список городов
    buttons = [InlineKeyboardButton(city, callback_data=f"weather_{city}") for city in cities]
    markup.add(*buttons)
    await bot.send_message(chat_id, "Выберите город для получения прогноза погоды:", reply_markup=markup)

# Функция для получения прогноза погоды
async def get_weather(city):
    api_key = config.openweathermap_api_key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        weather_description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        return f"Погода в городе {city}: {weather_description}. Температура: {temperature}°C"
    else:
        return "Не удалось получить данные о погоде. Пожалуйста, попробуйте еще раз."

# Обработчик нажатия на кнопку с городом
async def get_weather_callback(callback_query: types.CallbackQuery):
    city = callback_query.data.split('_')[1]
    weather_message = await get_weather(city)
    await callback_query.message.answer(weather_message)
