from datetime import *
from translate import Translator
import requests
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

bot = Bot(token="5271842964:AAFS-iFQnxH2EqCZDKSweWqbdXUQPKysh4I", parse_mode="HTML")
dp = Dispatcher(bot)
butto1 = InlineKeyboardButton("Bugun", callback_data='bugun')
butto2 = InlineKeyboardButton("Ertaga", callback_data='ertaga')
butto3 = InlineKeyboardButton("Eng yaqin masjidni aniqlash.", callback_data="masjid", url="https://namozvaqti.uz/qibla")
button1 = InlineKeyboardMarkup(row_width=2).add(butto1, butto2, butto3)
city = "Tashkent"


@dp.callback_query_handler(text_contains="bugun")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    today_time = datetime.today().now()
    p = open("images/prayer.jpg", "rb")
    today = today_time + timedelta(minutes=15)
    data = requests.get(f"https://api.pray.zone/v2/times/today.json?city={city}&school=9").json()
    bomdod = data['results']["datetime"][0]['times']["Fajr"]
    quyosh_ch = data['results']["datetime"][0]['times']["Sunrise"]
    peshin = data['results']["datetime"][0]['times']["Dhuhr"]
    asr = data['results']["datetime"][0]['times']["Asr"]
    shom = data['results']["datetime"][0]['times']["Maghrib"]
    xufton = data['results']["datetime"][0]['times']["Isha"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"Bomdod: {bomdod} 🌑    |Quyosh: {quyosh_ch} 🌒\nPeshin: {peshin} 🌕       "
                                 f"|Asr: {asr} 🌔\nShom: {shom} 🌑 "
                                 f"        |Xufton: {xufton} 🌚")


@dp.callback_query_handler(text_contains="eratag")
async def ertaga(call: CallbackQuery):
    await call.answer(cache_time=60)
    p = open("images/erta.jpg", "rb")
    today = datetime.today() + timedelta(days=1)
    data = requests.get(f"https://api.pray.zone/v2/times/day.json?city={city}&date={today}&school=9").json()
    tim = data['results']["datetime"][0]["date"]['gregorian']
    times1 = data['results']["datetime"][0]['times']
    bomdod = data['results']["datetime"][0]['times']["Fajr"]
    quyosh_ch = data['results']["datetime"][0]['times']["Sunrise"]
    peshin = data['results']["datetime"][0]['times']["Dhuhr"]
    asr = data['results']["datetime"][0]['times']["Asr"]
    shom = data['results']["datetime"][0]['times']["Maghrib"]
    xufton = data['results']["datetime"][0]['times']["Isha"]

    await bot.send_photo(call.message.chat.id, p,
                         caption=f"Bomdod: {bomdod} 🌑    |Quyosh: {quyosh_ch} 🌒\nPeshin: {peshin} 🌕       "
                                 f"|Asr: {asr} 🌔\nShom: {shom} 🌑 "
                                 f"        |Xufton: {xufton} 🌚")


@dp.message_handler(commands="start")
async def start(message: Message):
    p = open("images/images.jpeg", "rb")
    await bot.send_photo(message.chat.id, p,
                         caption="Assalomu alaykum siz Nomoz vaqtlar botidan foydalanmoqdasiz.\n"
                                 "Bu botdan foydalanish juda ham osson va qulay !\n"
                                 "Kerak bo'lgan shahar nomini yozing va Nomoz vaqtlarini"
                                 " bilib oling.\n"
                                 "Masjidning belgisi ☪️")


@dp.message_handler()
async def tek(message: Message):
    button = InlineKeyboardButton("Shahar nomini tekshirish.", url="https://prayertimes.date/api/docs/cities")
    but = InlineKeyboardMarkup().add(button)
    try:
        city = message.text.capitalize()
        translat = Translator(from_lang="uz", to_lang="en")
        city = translat.translate(city)
        data = requests.get(f"https://api.pray.zone/v2/times/today.json?city={city}&school=9").json()
        if data:
            await message.answer(f"{city} shahri uchun nomoz vaqtlarini \nbilish uchun pasdagi tugmalarni birini\n"
                                 f"tanlang.", reply_markup=button1)
    except Exception as i:
        print(i)
        await message.answer("Shahar nomini tekshiring", reply_markup=but)


if __name__ == '__main__':
    executor.start_polling(dp)
