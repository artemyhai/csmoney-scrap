
from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN 


bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    start_buttons = ['🗡️ Ножи', '🧤 Перчатки', '🔫Снайперские винтовки']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    
    await message.answer('Выберите категорию', reply_markup=keyboard)

def main():
    executor.start_polling(dp)
    
    
if __name__ == '__main__':
    main()
    