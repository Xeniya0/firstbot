from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import random
from second import TOKEN, cats, video_cats, video_notes

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🖇 Меню")
    btn2 = types.KeyboardButton("😻 Фото котик")
    btn3 = types.KeyboardButton("😸 Видео котик")
    btn4 = types.KeyboardButton("😽 Котик-кружочек")
    markup.add(btn1, btn2, btn3, btn4)
    await bot.send_message(message.chat.id, text="Привет, Я бот-кот", reply_markup=markup)

@dp.message_handler()
async def process_help_command(message: types.Message):
    if message.text == "🖇 Меню":
        await message.reply('тыкай кнопки')
    elif message.text == "😻 Фото котик":
        await bot.send_photo(message.from_user.id, photo=open(random.choice(cats), 'rb'))
    elif message.text == "😸 Видео котик":
        await bot.send_video(message.from_user.id, video=open(random.choice(video_cats), 'rb'))
    elif message.text == "😽 Котик-кружочек":
        await bot.send_video_note(message.from_user.id, video_note=open(random.choice(video_notes), 'rb'))
    else:
        message.text = message.text.capitalize()
        if message.text == 'Хуй':
            await bot.send_message(message.from_user.id, "сам такой")
        elif message.text == 'Бот':
            await bot.send_message(message.from_user.id, "че нада")
        elif message.text == 'Пошел нахуй':
            await bot.send_message(message.from_user.id, "сам пошел нахуй")
        else:
            await bot.send_message(message.from_user.id, message.text)


# @dp.message_handler()
# async def echo_message(message: types.Message):
#     message.text = message.text.capitalize()
#     if message.text == 'Хуй':
#         await bot.send_message(message.from_user.id, "сам такой")
#     elif message.text == 'Бот':
#         await bot.send_message(message.from_user.id, "че нада")
#     elif message.text == 'Пошел нахуй':
#         await bot.send_message(message.from_user.id, "сам пошел нахуй")
#     else:
#         await bot.send_message(message.from_user.id, message.text)








if __name__ == '__main__':
    executor.start_polling(dp)