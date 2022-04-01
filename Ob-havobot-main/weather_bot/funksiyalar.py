from bs4 import BeautifulSoup as BS
import requests
from tugmalar import hududlar_button


def start(update, context):
	user = update.message.from_user
	salom = f'Assalomu Aleykum {user.first_name} 🤝. uzbweather_bot ga xush kelibsiz !!! \n '\
			f' \nSizga foydamiz tegganidan xursandmiz😊. Iltimos hududni tanlang'
	update.message.reply_photo(photo=open('Hafta kuni  Sana  Saharlik  Iftorlik (3).png', 'rb'), caption=salom, reply_markup=hududlar_button)

	return 1


def andijon(update, context):
	r = requests.get('https://sinoptik.ua/погода-андижан')
	html = BS(r.content, 'html.parser')
	minimum = html.findAll("div", {"class": "min"})
	maximum = html.findAll("div", {"class": "max"})

	t_min = minimum[0].text
	t_max = maximum[0].text

	update.message.reply_text("Andijon belgilandi. Bugun Andijonda ob-havo 🌦👇:"+ '\n' + "Eng past daraja⬇️ :" + t_min +' ,'+ '\n' + "Eng yuqori daraja⬆️ :"+ t_max, reply_markup = hududlar_button)


def buxoro(update, context):

	r = requests.get('https://sinoptik.ua/погода-бухара')
	html = BS(r.content, 'html.parser')
	minimum = html.findAll("div", {"class": "min"})
	maximum = html.findAll("div", {"class": "max"})

	t_min = minimum[0].text
	t_max = maximum[0].text

	update.message.reply_text("Buxoro belgilandi. Bugun Buxoroda ob-havo 🌦👇:"+ '\n' + "Eng past daraja⬇️ :" + t_min +' , '+ '\n' + "Eng yuqori daraja⬆️ :"+ t_max, reply_markup = hududlar_button)


def fargona(update, context):

	r = requests.get('https://sinoptik.ua/погода-фергана')
	html = BS(r.content, 'html.parser')
	minimum = html.findAll("div", {"class": "min"})
	maximum = html.findAll("div", {"class": "max"})

	t_min = minimum[0].text
	t_max = maximum[0].text

	update.message.reply_text("Farg'ona belgilandi. Bugun Farg'onada ob-havo 🌦👇:"+ '\n' + "Eng past daraja⬇️ :" + t_min +','+ '\n' + "Eng yuqori daraja⬆️ :"+ t_max, reply_markup = hududlar_button)


def jizzax(update, context):

	r = requests.get('https://sinoptik.ua/погода-джизак')
	html = BS(r.content, 'html.parser')
	minimum = html.findAll("div", {"class": "min"})
	maximum = html.findAll("div", {"class": "max"})

	t_min = minimum[0].text
	t_max = maximum[0].text

	update.message.reply_text("Jizzax belgilandi. Bugun Jizzaxda ob-havo 🌦👇:"+ '\n' + "Eng past daraja⬇️ :" + t_min +','+ '\n' + "Eng yuqori daraja⬆️ :"+ t_max, reply_markup = hududlar_button)


def namangan(update, context):

	r = requests.get('https://sinoptik.ua/погода-наманган')
	html = BS(r.content, 'html.parser')
	minimum = html.findAll("div", {"class": "min"})
	maximum = html.findAll("div", {"class": "max"})

	t_min = minimum[0].text
	t_max = maximum[0].text

	update.message.reply_text("Namangan belgilandi. Bugun Namanganda ob-havo 🌦👇:"+ '\n' + "Eng past daraja⬇️ :" + t_min +','+ '\n' + "Eng yuqori daraja⬆️ :"+ t_max, reply_markup = hududlar_button)


def navoiy(update, context):

	r = requests.get('https://sinoptik.ua/погода-навои')
	html = BS(r.content, 'html.parser')
	minimum = html.findAll("div", {"class": "min"})
	maximum = html.findAll("div", {"class": "max"})

	t_min = minimum[0].text
	t_max = maximum[0].text

	update.message.reply_text("Navoiy belgilandi. Bugun Navoiyda ob-havo 🌦👇:"+ '\n' + "Eng past daraja⬇️ :" + t_min +','+ '\n' + "Eng yuqori daraja⬆️ :"+ t_max, reply_markup = hududlar_button)


def qashqadaryo(update, context):

	r = requests.get('https://sinoptik.ua/погода-карши')
	html = BS(r.content, 'html.parser')
	minimum = html.findAll("div", {"class": "min"})
	maximum = html.findAll("div", {"class": "max"})

	t_min = minimum[0].text
	t_max = maximum[0].text

	update.message.reply_text("Qashqadaryo belgilandi. Bugun Qashqadaryoda ob-havo 🌦👇:"+ '\n' + "Eng past daraja⬇️ :" + t_min +','+ '\n' + "Eng yuqori daraja⬆️ :"+ t_max, reply_markup = hududlar_button)


def qoraqalpogiston(update, context):

	r = requests.get('https://sinoptik.ua/погода-нукус')
	html = BS(r.content, 'html.parser')
	minimum = html.findAll("div", {"class": "min"})
	maximum = html.findAll("div", {"class": "max"})

	t_min = minimum[0].text
	t_max = maximum[0].text

	update.message.reply_text("Qoraqalpog'iston belgilandi. Bugun Qoraqalpog'istonda ob-havo 🌦👇:"+ '\n' + "Eng past daraja⬇️ :" + t_min +','+ '\n' + "Eng yuqori daraja⬆️ :"+ t_max, reply_markup = hududlar_button)


def samarqand(update, context):

	r = requests.get('https://sinoptik.ua/погода-самарканд')
	html = BS(r.content, 'html.parser')
	minimum = html.findAll("div", {"class": "min"})
	maximum = html.findAll("div", {"class": "max"})

	t_min = minimum[0].text
	t_max = maximum[0].text

	update.message.reply_text("Samarqand belgilandi. Bugun Samarqandda ob-havo 🌦👇:"+ '\n' + "Eng past daraja⬇️ :" + t_min +','+ '\n' + "Eng yuqori daraja⬆️ :"+ t_max, reply_markup = hududlar_button)


def sirdaryo(update, context):

	r = requests.get('https://sinoptik.ua/погода-сырдарья')
	html = BS(r.content, 'html.parser')
	minimum = html.findAll("div", {"class": "min"})
	maximum = html.findAll("div", {"class": "max"})

	t_min = minimum[0].text
	t_max = maximum[0].text

	update.message.reply_text("Sirdaryo belgilandi. Bugun Sirdaryoda ob-havo 🌦👇:"+ '\n' + "Eng past daraja⬇️ :" + t_min +','+ '\n' + "Eng yuqori daraja⬆️ :"+ t_max, reply_markup = hududlar_button)


def surxondaryo(update, context):

	r = requests.get('https://sinoptik.ua/погода-термез')
	html = BS(r.content, 'html.parser')
	minimum = html.findAll("div", {"class": "min"})
	maximum = html.findAll("div", {"class": "max"})

	t_min = minimum[0].text
	t_max = maximum[0].text

	update.message.reply_text("Surxondaryo belgilandi. Bugun Surxondaryoda ob-havo 🌦👇:"+ '\n' + "Eng past daraja⬇️ :" + t_min +','+ '\n' + "Eng yuqori daraja⬆️ :"+ t_max, reply_markup = hududlar_button)


def toshkent_viloyati(update, context):
	r = requests.get('https://sinoptik.ua/погода-кибрай')
	html = BS(r.content, 'html.parser')
	minimum = html.findAll("div", {"class": "min"})
	maximum = html.findAll("div", {"class": "max"})

	t_min = minimum[0].text
	t_max = maximum[0].text

	update.message.reply_text("Toshkent viloyati belgilandi. Bugun Toshkent viloyatida ob-havo 🌦👇:"+ '\n' + "Eng past daraja⬇️ :" + t_min +','+ '\n' + "Eng yuqori daraja⬆️ :"+ t_max, reply_markup =hududlar_button)


def toshkent(update, context):
	r = requests.get('https://sinoptik.ua/погода-ташкент')
	html = BS(r.content, 'html.parser')
	minimum = html.findAll("div", {"class": "min"})
	maximum = html.findAll("div", {"class": "max"})

	t_min = minimum[0].text
	t_max = maximum[0].text

	update.message.reply_text("Buxoro belgilandi. Bugun Toshkent shahrida ob-havo 🌦👇:"+ '\n' + "Eng past daraja⬇️ :" + t_min +','+ '\n' + "Eng yuqori daraja⬆️ :"+ t_max, reply_markup = hududlar_button)


def xorazm(update, context):
	r = requests.get('https://weather.rambler.ru/v-urgenche')
	html = BS(r.content, 'html.parser')
	minimum = html.findAll("div", {"class": "min"})
	maximum = html.findAll("div", {"class": "max"})

	t_min = minimum[0].text
	t_max = maximum[0].text

	update.message.reply_text("Xorazm belgilandi. Bugun Xorazmda ob-havo 🌦👇:"+ '\n' + "Eng past daraja⬇️ :" + t_min +','+ '\n' + "Eng yuqori daraja⬆️ :"+ t_max, reply_markup = hududlar_button)


def help_command(update, context):
	update.message.reply_text("Yordam uchun @Alimardon_Boqijonov ga murojaat qiling .")


def admin(update, context):
	update.message.reply_text("Admin👨🏻‍💻 bilan bog'lanish - @Alimardon_boqijonov ")