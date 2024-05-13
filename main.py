import asyncio
import config
from aiogram import F, Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from weather import send_city_buttons, get_weather_callback
import logging
import random
from keyboards import keyboard
from api_code import api_func_img
from api_func_winth import api_func_wth

# Создаем глобальную переменную для флага
flag = 0

# Логирование
logging.basicConfig(level=logging.INFO)

# Объект бота и диспетчера
bot = Bot(token=config.token)
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def start(message: types.Message):
    global flag  # Используем глобальную переменную
    flag = 0
    await message.answer(f'Привет, {message.from_user.full_name}!', reply_markup=keyboard)

@dp.message(Command(commands=['stop']))
async def stop(message: types.Message):
    global flag  # Используем глобальную переменную
    flag = 0
    await message.answer(f'Пока, {message.from_user.full_name}!')

@dp.message(Command(commands=['info']))
async def info(message: types.Message):
    global flag  # Используем глобальную переменную
    flag = 0
    await message.answer(f'Привет! Я твой личный помощник. Вот что я могу:\n'+
    '  1. Показывать погоду в любом городе.\n'+
    '  2. Называть случайное число от 0 до 100.\n'+
    '  3. Показывать интересные картинки.\n\n'+
    'Просто отправь мне команду /weather, чтобы узнать погоду, /number для случайного числа или /image, чтобы увидеть картинку.'+ 
    'Давай начнем!')

@dp.message(Command(commands=['number']))
async def info(message: types.Message):
    global flag  # Используем глобальную переменную
    flag = 0
    number = random.randint(0, 100)
    await message.answer(f'Твое число: {number}!')    

@dp.message(Command(commands=['weather']))
async def info(message: types.Message):
    global flag  # Используем глобальную переменную
    flag = 1
    await message.answer(f'Напиши город, в котором показать погоду')    

@dp.message(Command(commands=['image']))
async def info(message: types.Message):
    global flag  # Используем глобальную переменную
    flag = 2    
    await message.answer(f'Напиши, какую картинку тебе показать') 


# Отправляем картинку только тогда, когда нажата кнопочка IMAGE
@dp.message(F.text)
async def msg(message: types.Message):
    if flag == 2:  # Проверяем, что переменная flag равна False
        message_text = message.text.lower()
        print(message_text)
        api_key = "KjzqQvq4aSX4bx6n9C6Q_opViuYaLfVR8l4Yk74Sqsg"  # Ваш API ключ
        image_url = api_func_img(message_text, api_key)
        await message.answer(f'Ищу тебе картинку', reply_markup=keyboard)
        await message.answer_photo(image_url)

    elif flag == 1:  # Проверяем, что переменная flag равна False
        message_text = message.text.lower()
        #print(message_text)
        api_key = "43ac134a4d362cd96a51421cb0d8cc9f"  # Ваш API ключ
        temper, humidity, speed = api_func_wth(message_text, api_key)

        await message.answer(f'Сейчас посмотрим, какая погода в городе {message_text}!', reply_markup=keyboard)
        await message.answer(f"Температура: {round(temper-273.15,1)} С, \nВлажность: {humidity}%, \nСкорость ветра: {speed} м/с")
       

async def main():
    # Отправляем сообщение с кнопкой запуска бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
