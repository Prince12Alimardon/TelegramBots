import logging
import wikipedia

from aiogram import bot, Dispatcher, executor, types, Bot

API_TOKEN = '5048286428:AAG-cSlC3AMYXR-Okn2_KHqaVtvT93ho7J8'
wikipedia.set_lang('uz')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
ab = Dispatcher(bot)

@ab.message_handler(commands=['start','help'])
async def send_welcome(message: types.Message):


    await message.reply("Assalomu-alaykum \n" 'Prince12 | WikipediaBotga XUSH KELIBSIZ! ')

@ab.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid ma'lumot topilmadi. Iltimos qayta uruninng!")

if __name__ == '__main__':
    executor.start_polling(ab, skip_updates=True)