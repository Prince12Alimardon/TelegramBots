from telegram.ext import Updater, ConversationHandler, CommandHandler
from telegram.ext import MessageHandler, Filters
from funksiyalar import *


updater = Updater(token="Your Bot Token")
dispatcher = updater.dispatcher

conv_handler = ConversationHandler(
		entry_points=[CommandHandler('start', start)],
		states={
			1: [
				MessageHandler(Filters.regex('^(Andijon)$'), andijon),
				MessageHandler(Filters.regex('^(Buxoro)$'), buxoro),
				MessageHandler(Filters.regex("^(Farg'ona)$"), fargona),
				MessageHandler(Filters.regex('^(Jizzax)$'), jizzax),
				MessageHandler(Filters.regex('^(Namangan)$'), namangan),
				MessageHandler(Filters.regex('^(Navoiy)$'), navoiy),
				MessageHandler(Filters.regex('^(Qarshi)$'), qashqadaryo),
				MessageHandler(Filters.regex("^(Nukus)$"), qoraqalpogiston),
				MessageHandler(Filters.regex('^(Samarqand)$'), samarqand),
				MessageHandler(Filters.regex('^(Guliston)$'), sirdaryo),
				MessageHandler(Filters.regex('^(Termiz)$'), surxondaryo),
				MessageHandler(Filters.regex('^(Toshkent viloyati)$'), toshkent_viloyati),
				MessageHandler(Filters.regex('^(Toshkent Shaxri)$'), toshkent),
				MessageHandler(Filters.regex('^(Xorazm)$'), xorazm),
			]
        }, fallbacks = [MessageHandler(Filters.text,start)]
)

dispatcher.add_handler(conv_handler)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('admin', admin))
updater.start_polling()
print("bot ishlayabdi")
