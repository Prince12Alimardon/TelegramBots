from datetime import datetime, timedelta

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

from DB_helper import DBhelper
from Config import bot_token, DB_NAME

bugun, ertaga, Ttaqvim, mintaqa, duo = ("Bugun ⌛️", "Ertaga ⏳", "To'liq taqvim 📆", "MIntaqa 🇺🇿", "Duo 🤲")
main_button = ReplyKeyboardMarkup([
    [bugun], [ertaga, Ttaqvim], [mintaqa], [duo]
], resize_keyboard=True)

STATE_REGION = 1
STATE_CALENDAR = 2
user_region = dict()
db = DBhelper(DB_NAME)


def region_buttons():
    buttons = [
        [
            InlineKeyboardButton('Toshkent', callback_data='region_1'),
            InlineKeyboardButton('Andijon', callback_data='region_2')
        ],
        [
            InlineKeyboardButton('Buxoro', callback_data='region_3'),
            InlineKeyboardButton('Sirdaryo', callback_data='region_4')
        ],
        [
            InlineKeyboardButton('Samarqand', callback_data='region_5'),
            InlineKeyboardButton('Namangan', callback_data='region_6')
        ],
        [
            InlineKeyboardButton('Qashqadaryo', callback_data='region_10'),
            InlineKeyboardButton('Surxandaryo', callback_data='region_12')
        ],
        [
            InlineKeyboardButton('Navoiy', callback_data='region_7'),
            InlineKeyboardButton('Jizzax', callback_data='region_8')
        ],
        [
            InlineKeyboardButton("Farg'ona", callback_data='region_9'),
            InlineKeyboardButton('Xorazm', callback_data='region_13')
        ]
    ]
    return buttons


def start(update, context):
    user = update.message.from_user
    user_region[user.id] = None
    # button = region_buttons()
    mes = f"<b>Assalomu alekum </b> {user.first_name} " f"\n<b>Ramazon muborak Aziz Dindoshim 🌞.</b> " f"\n<b>Sizga qaysi mintaqa bo'yicha ma'lumot beray!</b>"
    update.message.reply_photo(photo=open("ramazonn.jpg", "rb"), caption=mes, parse_mode="HTML", reply_markup=InlineKeyboardMarkup(region_buttons()))
    return STATE_REGION


def inline_callback(update, context):
    try:
        query = update.callback_query
        query.message.delete()
        user_id = query.from_user.id
        user_region[user_id] = query.data
        data = str(query.data)
        user_region[user_id] = data[7:]
        query.message.reply_html(text=f"<b>Ramazon Taqvimi </b>", reply_markup=main_button)
        return STATE_CALENDAR

    except Exception as u:
        print(u)


def today(update, context):
    global today1
    try:
        user_id = update.message.from_user.id
        region_id = int(user_region[user_id])
        region = db.get_region(region_id)
        today1 = str(datetime.now().date())
        calendar = db.get_calendar_by_region(region_id, today1)
        message = f"<b>Ramazon</b> {today1}\n<b>{region['name']}</b> vaqti\n \nSaxarlik: <b>{calendar['fajr'][:5]}</b>"\
                  f"\nIftorlik: <b>{calendar['maghrib'][:5]}</b>"

        update.message.reply_photo(photo=open("ramazonn.jpg", "rb"), caption=message, parse_mode="HTML",
                                   reply_markup=main_button)
    except Exception as o:
        print(o)
        update.message.reply_html(f"<b>Ro'za hali boshlanmadi bugungi sana {today1}.</b>\n"
                                  f"<b>Ro'za boshlanish kuni 2022-04-02</b>.")


def tommorow(update, context):
    global today2
    try:
        user_id = update.message.from_user.id
        region_id = user_region[user_id]
        region = db.get_region(region_id)
        today2 = str(datetime.now().date() + timedelta(days=1))
        calendar = db.get_calendar_by_region(region_id, today2)
        print(today2)
        message = f"<b>Ertangi sana: </b> {today2}\n<b>{region['name']}</b> vaqti\n \nSaxarlik: <b>{calendar['fajr'][:5]}</b>\nIftorlik: " \
                  f"<b>{calendar['maghrib'][:5]}</b>"

        update.message.reply_photo(caption=message, photo=open("ramazonn.jpg", "rb"), parse_mode="HTML",
                                   reply_markup=main_button)
    except Exception as o:
        print(o)
        update.message.reply_html(f"<b>Ro'za hali boshlanmadi bugungi sana {today2}.</b>\n"
                                  f"<b>Ro'za boshlanish kuni 2022-04-02</b>.")


def month(update, context):
    global p
    user_id = update.message.from_user.id
    region_id = user_region[user_id]
    region = db.get_region(region_id)
    if region_id == "1":
        p = open("images/Toshkent1.png", "rb")
    elif region_id == "2":
        p = open("images/Andijon.png", "rb")
    elif region_id == "3":
        p = open("images/Buxoro.png", "rb")
    elif region_id == "4":
        p = open("images/Sirdaryo.png", "rb")
    elif region_id == "5":
        p = open("images/Samarqand.png", "rb")
    elif region_id == "6":
        p = open("images/Namangan.png", "rb")
    elif region_id == "7":
        p = open("images/Navoiy.png", "rb")
    elif region_id == "8":
        p = open("images/Jizzax.png", "rb")
    elif region_id == "9":
        p = open("images/Farg'ona.png", "rb")
    elif region_id == "10":
        p = open("images/Samarqand.png", "rb")
    elif region_id == "12":
        p = open("images/Surxandaryo.png", "rb")
    elif region_id == "13":
        p = open("images/Xorazm.png", "rb")
    message = f"<b>Ramazon</b> 2022\n<b>{region['name']}</b> vaqtlari"
    update.message.reply_photo(photo=p, caption=message, parse_mode="HTML",
                               reply_markup=main_button)


def select_region(update, context):
    buttons = region_buttons()
    update.message.reply_text("Qaysi mintaqa bo'yicha ma'lumot kerak?", reply_markup=InlineKeyboardMarkup(buttons))
    return STATE_REGION


def select_duo(update, context):
    update.message.reply_photo(photo=open("duo.jpg", "rb"), caption="<b>Ramazon oyida tutgan Ro'zalaringiz "
                                                                            "qabul bo'lsin "
                                                                            "va barchamizga Alloh taolo Sabr va Ajr bersin</b>",
                               parse_mode="HTML",
                               reply_markup=main_button)


def main():
    updater = Updater(bot_token, use_context=True)

    dispatche = updater.dispatcher

    # dispatche.add_handler(CommandHandler('start', start))

    # dispatche.add_handler(CallbackQueryHandler(inline_callback))

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            STATE_REGION: [CallbackQueryHandler(inline_callback)],
            STATE_CALENDAR: {
                MessageHandler(Filters.regex('^(' + bugun + ')$'), today),
                MessageHandler(Filters.regex('^(' + ertaga + ')$'), tommorow),
                MessageHandler(Filters.regex('^(' + Ttaqvim + ')$'), month),
                MessageHandler(Filters.regex('^(' + mintaqa + ')$'), select_region),
                MessageHandler(Filters.regex('^(' + duo + ')$'), select_duo)
            }
        },
        fallbacks=[CommandHandler('start', start)]
    )

    dispatche.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


main()
