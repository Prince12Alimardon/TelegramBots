from aiogram import Bot, Dispatcher, types, executor
import requests
import json

btn = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn.add("USD-UZS", "RUB-UZS", "EURO-UZS", "CNY-UZS", "WON-UZS", "DINOR-UZS")

token = "Your Bot token"
bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def first(message: types.Message):
    rasm1 = open("exch.jpeg", "rb")
    cap =  "Assalomu-alaykum, Prince12 | Valyuta Ayirboshlash | Botiga Hush Kelibsiz!"
    await bot.send_photo(message.chat.id, rasm1, caption=cap, reply_markup=btn)


@dp.message_handler(content_types=["text"])
async def second(message: types.Message):
    global inputs, outputs, result, cap, rasm
    text = message.text
    if text == "USD-UZS":
        inputs = "USD"
        outputs = "UZS"
        rasm = open("USD.jpg", "rb")
        cap = "Dollarning So'mdagi qiymati 👇"
    if text == "RUB-UZS":
        inputs = "RUB"
        outputs = "UZS"
        rasm = open("RUBL.jpg", "rb")
        cap = "Rublning So'mdagi qiymatin 👇"
    if text == "EURO-UZS":
        inputs = "EUR"
        outputs = "UZS"
        rasm = open("EURO.jpg", "rb")
        cap = "EUROning So'mdagi qiymatin 👇"
    if text == "CNY-UZS":
        inputs = "CNY"
        outputs = "UZS"
        rasm = open("CNY.jpg", "rb")
        cap = "Xitoy Yenasining So'mdagi qiymatin 👇"
    if text == "DINOR-UZS":
        inputs = "KWD"
        outputs = "UZS"
        rasm = open("Dinor.jpg", "rb")
        cap = "Dinorning So'mdagi qiymatin 👇"
    if text == "WON-UZS":
        inputs = "KRW"
        outputs = "UZS"
        rasm = open("Won.jpg", "rb")
        cap = "Wonning So'mdagi qiymatin 👇"


    url = "https://v6.exchangerate-api.com/v6/5f6d43916b52307ea4aed1f3/latest/" + inputs
    responses = requests.get(url)
    rest = json.loads(responses.text)
    result = rest["conversion_rates"]["UZS"]
    if message.text.isdigit():
        print(int(message.text) * result)
        await bot.send_photo(message.chat.id, rasm, caption=cap)
        await bot.send_message(message.chat.id, int(message.text) * (result))


if __name__ == '__main__':
    executor.start_polling(dp)
