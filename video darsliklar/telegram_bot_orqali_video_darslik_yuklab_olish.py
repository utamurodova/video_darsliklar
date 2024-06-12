from aiogram import Bot, Dispatcher, executor, types
import logging
from config import token

logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)
dp = Dispatcher(bot)

kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Python')
btn2 = types.KeyboardButton('Java')
btn3 = types.KeyboardButton('C++')
btn4 = types.KeyboardButton('C#')
btn5 = types.KeyboardButton('JavaScript')

kb.add(btn1, btn2, btn3, btn4, btn5)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('HI! Welcome to Free Coding education bot\n Please select course', reply_markup=kb)

@dp.message_handler()
async def handle_text(message: types.Message):
    if message.text == 'Python':
        await bot.send_message(message.from_user.id, 'https://www.youtube.com/watch?v=_f8cpjAz0sw&list=PLOvS2OkP87tSfos3rmPAhg9FqFDhbOcr1')
    elif message.text == 'Java':
        await bot.send_message(message.from_user.id, 'https://www.youtube.com/watch?v=ZBJ4O93zFIg&list=PLE5dup5lL_x4Mtj20EGmH0EpbZew3EQDD')
    elif message.text == 'C++':
        await bot.send_message(message.from_user.id, 'https://www.youtube.com/watch?v=2BlETkdYFJk&list=PLY4N-4FJdZQCzjRxjFfHQ57xAYvKmk2Yo')
    elif message.text == 'C#':
        await bot.send_message(message.from_user.id, 'https://youtu.be/GhQdlIFylQ8?si=7TbFMUFR4OwlQe_o')
    elif message.text == 'JavaScript':
        await bot.send_message(message.from_user.id, 'https://www.youtube.com/watch?v=zJuDsji3IbE&list=PLNS3PujVHR-ay0HpqbsPWccgEhJZk6K9u')
        await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)



