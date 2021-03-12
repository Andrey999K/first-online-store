import telebot
from telebot.types import InputMediaPhoto

import config
import pymysql.cursors
from telebot import types

# import re
# import random

bot = telebot.TeleBot(config.TOKEN)


class Order:
    product = ""
    name = ""
    surname = ""
    phone = ""
    obtaining = ""


order = Order()

cursor = None

fl = True
while fl:
    try:
        connection = pymysql.connect(
            host='localhost',
            db='amster',
            user='root',
            password="",
            charset='utf8mb4'
        )
        cursor = connection.cursor()
        fl = False
    except:
        print("Повторная попытка соединения с базой данных.")



def getName(message):
    order.name = message.text
    print(message.text)
    sent = bot.send_message(message.chat.id, "Введите вашу фамилию:")
    print("Введите вашу фамилию:")
    bot.register_next_step_handler(sent, getSurname)


def getSurname(message):
    order.surname = message.text
    print(message.text)
    sent = bot.send_message(message.chat.id, "Введите ваш номер телефона:")
    print("Введите ваш номер телефона:")
    bot.register_next_step_handler(sent, getPhone)


def getPhone(message):
    order.phone = message.text
    print(message.text)
    keys = ["Самовывоз", "Доставка"]
    data = ["pickup", "delivery"]
    id = message.chat.id
    text = "Выберите способ получения:"
    print("Выберите способ получения:")
    sendKeyboard(keys=keys, data=data, id=id, text=text)


def addOrder(id):
    product = order.product
    name = order.name
    surname = order.surname
    phone = order.phone
    obtaining = order.obtaining
    query = "INSERT INTO orders (" \
            "id_product, name, surname, phone, obtaining" \
            ") VALUES (" \
            "{}, '{}', '{}', '{}', {}" \
            ")".format(product, name, surname, phone, obtaining)
    cursor.execute(query)
    connection.commit()
    bot.send_message(id, "Заказ успешно создан!")


# def getObtaining(message):
#     order.phone = message
#     sent = bot.send_message(message.chat.id, "Выберите способ получения:")
#     bot.register_next_step_handler(sent, getObtaining)

def sendKeyboard(keys, data, id, text, photo=None):
    markup_inline = types.InlineKeyboardMarkup()
    for index, item in enumerate(keys):
        elem = types.InlineKeyboardButton(text=item, callback_data=data[index])
        markup_inline.add(elem)

    if photo:
        img = open(photo, "rb")
        bot.send_photo(id, img, text, reply_markup=markup_inline, parse_mode="HTML", disable_notification=True)
        img.close()
    else:
        bot.send_message(
            id, text,
            reply_markup=markup_inline,
            disable_notification=True,
            parse_mode="HTML",
            disable_web_page_preview=True
        )

def productList(category, id):
    if category == "boxes":
        cursor.execute("SELECT * FROM products WHERE category = 1")
        data = cursor.fetchall()
        for item in data:
            text = item[1] + "\n<b>" + str(item[2]) + " ₽</b>"
            src = "../img/" + str(item[4]) + ".jpg"
            keyMass = ['Оформить заказ']
            dateMass = [item[3]]
            sendKeyboard(keys=keyMass, data=dateMass, text=text, id=id, photo=src)

    elif category == "bouquets":
        cursor.execute("SELECT * FROM products WHERE category = 2")
        data = cursor.fetchall()
        for item in data:
            text = item[1] + "\n<b>" + str(item[2]) + " ₽</b>"
            src = "../img/" + str(item[4]) + ".jpg"
            keyMass = ['Оформить заказ']
            dateMass = [item[3]]
            sendKeyboard(keys=keyMass, data=dateMass, text=text, id=id, photo=src)

    elif category == "balloons":
        cursor.execute("SELECT * FROM products WHERE category = 3")
        data = cursor.fetchall()
        for item in data:
            text = item[1] + "\n<b>" + str(item[2]) + " ₽</b>"
            src = "../img/" + str(item[4]) + ".jpg"
            keyMass = ['Оформить заказ']
            dateMass = [item[0]]
            sendKeyboard(keys=keyMass, data=dateMass, text=text, id=id, photo=src)



@bot.message_handler(commands=['start', 'help'])
def sendWelcome(message):
    # keyMass = ['Добавить праздник']
    # dateMass = ['celebration']
    # urls = ['']
    # sendKeyboard(keyMass, dateMass, urls, "Выберите действие", message.chat.id)
    # bot.send_message(
    #     message.chat.id,
    #     "<a href=\"https://t.me/luxur1a/\">Лебедь</a> лох",
    #     parse_mode="HTML",
    #     disable_web_page_preview=True)
    # if message.from_user.id == 734441979:
    #     keyMass = ['Добавить праздник']
    #     dateMass = ['celebration']
    #     urls = ['']
    #     sendKeyboard(keyMass, dateMass, urls, "Выберите действие", message.chat.id)
    # else:
    #     bot.reply_to(message, "Привет")
    # print(message)



    # keyMass = [data[0][1], data[1][1], data[2][1]]
    # dateMass = [data[0][3], data[1][3], data[2][3]]
    # sendKeyboard(keys=keyMass, data=dateMass, text="Выберите товар:", id=message.chat.id)


    keyMass = ['Коробки с цветами', 'Букеты', 'Шары']
    dateMass = ['boxes', 'bouquets', 'balloons']
    text = "Выбрите категорию:"
    sendKeyboard(keys=keyMass, data=dateMass, text=text, id=message.chat.id)
    # cursor.execute("SELECT * FROM products")
    # data = cursor.fetchall()

    # for item in data:
    #     text = item[1] + "\n<b>" + str(item[2]) + " ₽</b>"
    #     src = "../img/" + item[3] + ".jpg"
    #     # img = open(src, "rb")
    #     # bot.send_photo(message.chat.id, img, text, parse_mode="HTML", disable_notification=True)
    #     # img.close()
    #     keyMass = ['Оформить заказ']
    #     dateMass = [item[3]]
    #     sendKeyboard(keys=keyMass, data=dateMass, text=text, id=message.chat.id, photo=src)
    #     # bot.send_message(message.chat.id, text, parse_mode="HTML", disable_notification=True)


    # photoMass = []
    # keyMass = []
    # dateMass = []
    # for item in data:
    #     keyMass.append(item[1] + "  " + str(item[2]) + " ₽")
    #     dateMass.append(item[3])
    #     telebot.types.InputMediaPhoto(open("../img/" + item[3] + ".jpg", 'rb'))
    #     photoMass.append(telebot.types.InputMediaPhoto(open("../img/" + item[3] + ".jpg", 'rb')))
    # bot.send_media_group(message.chat.id, photoMass)
    # text = "Выберите товар:"
    # sendKeyboard(keys=keyMass, data=dateMass, text=text, id=message.chat.id)



@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == "yes":
        sent = bot.send_message(call.message.chat.id, "Введите ваше имя:")
        print("Введите ваше имя:")
        bot.register_next_step_handler(sent, getName)
    elif call.data == "pickup":
        order.obtaining = 0
        addOrder(call.message.chat.id)
    elif call.data == "delivery":
        order.obtaining = 1
        addOrder(call.message.chat.id)
    elif call.data == "boxes":
        productList(call.data, call.message.chat.id)
    elif call.data == "bouquets":
        productList(call.data, call.message.chat.id)
    elif call.data == "balloons":
        productList(call.data, call.message.chat.id)
    else:
        # if call.data == 'product':
        #     bot.send_message(call.message.chat.id, "")
        # bot.send_message(call.message.chat.id, call.data)
        query = "SELECT name FROM products WHERE id_product = {}".format(call.data)
        print(query)
        cursor.execute(query)
        name = cursor.fetchall()[0][0]
        print(name)
        keyMass = ['Да']
        dateMass = ["yes"]
        text = "Заказать \"{}\"?".format(name)
        order.product = call.data
        sendKeyboard(keys=keyMass, data=dateMass, text=text, id=call.message.chat.id)
        # bot.send_message(call.message.chat.id, "Заказать \"{}\"?".format(name))


#
# hello = ["Хай", "Хэлоу", "Приветствую", "Привет", "Приветик"
#                                                   "Салам", "Здарова"
#                                                            "Привеееееееееет", "Ку"
#          ]


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    print(message.chat.id)
    print(message.text)
    print("\n")
    # text = message.text.lower()
    # if text == 'салам':
    #     bot.reply_to(message, "алейкум)")
    # else:
    #     for hel in hello:
    #         if re.search(hel.lower(), text):
    #             n = random.randint(0, len(hello) - 1)
    #             bot.reply_to(message, hello[n] + ")")
    #             break


bot.polling(none_stop=True)
