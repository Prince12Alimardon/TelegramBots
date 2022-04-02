import logging

from aiogram import bot, Dispatcher, executor, types, Bot

API_TOKEN = 'Your Bot token'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
ab = Dispatcher(bot)

@ab.message_handler(commands=['start', 'help'])
async def  send_welcome(message: types.Message):


    await message.reply("Prince12_botiga XUSH KELIBSIZ! ")

@ab.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(ab, skip_updates=True)
