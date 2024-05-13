from aiogram import types


button1 = types.KeyboardButton(text='/start')
button2 = types.KeyboardButton(text='/stop')
button3 = types.KeyboardButton(text='/info')
button4 = types.KeyboardButton(text='/number')
button5 = types.KeyboardButton(text='/weather')
button6 = types.KeyboardButton(text='/image')

keyboard1 = [
    [button5, button6],
    [button4, button3],
    [button1, button2],

]


keyboard = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
