
import json
from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN 
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
from main import collect_data
import time


bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    start_buttons = ['🗡️ Ножи', '🧤 Перчатки']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    
    await message.answer('Выберите категорию', reply_markup=keyboard)


@dp.message_handler(Text(equals='🗡️ Ножи'))
async def get_discount_knives(message: types.Message):
    await message.answer('Немножко нужно подождать...')

    collect_data(cat_type=2)
    
    with open('result.json') as file:
        data = json.load(file)
        
    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
            f'{hbold("Скидка: ")}{item.get("discount")}%\n' \
            f'{hbold("Цена: ")}${item.get("price")}🔥'
        
        if index%20 == 0:
            time.sleep(3)
        
        await message.answer(card)  
        
@dp.message_handler(Text(equals='🧤 Перчатки'))
async def get_discount_gloves(message: types.Message):
    await message.answer('Немножко нужно подождать...')

    collect_data(cat_type=13)
    
    with open('result.json') as file:
        data = json.load(file)
        
    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
            f'{hbold("Скидка: ")}{item.get("discount")}%\n' \
            f'{hbold("Цена: ")}${item.get("price")}🔥'
        
        if index%20 == 0:
            time.sleep(3)
        
        await message.answer(card)               

def main():
    executor.start_polling(dp)
    
    
if __name__ == '__main__':
    main()
    
    
# start 1