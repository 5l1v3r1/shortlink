# IRAN CYBER SECURITY GROUP

from telebot import types
from time import ctime
from colorama import Fore, Style
from json import loads
from os import system
from os import name
from requests import get
import database
import config
import telebot
import sys



bot = telebot.TeleBot(config.TOKEN)

def cleaner():
    if name == "nt":
        system("cls")

    else:
        system("clear")

cleaner()
print("{}>>> {} Robot Started {}[{}{}{}]{} <<<".format(Fore.GREEN, Fore.BLUE,
 Fore.YELLOW, Fore.RED, ctime(), Fore.YELLOW, Fore.GREEN))

print("{} Bot Username ~> {}{}\n{} Bot Id ~> {}{}\n{} Bot Name ~> {}{}{}".format(Fore.RED,
 Fore.BLUE, bot.get_me().username, Fore.RED, Fore.BLUE, bot.get_me().id,
 Fore.RED, Fore.BLUE, bot.get_me().first_name, Style.RESET_ALL))


def short_link(link):
    req = get("https://api-ssl.bitly.com/v3/shorten?access_token=f2d0b4eabb524aaaf22fbc51ca620ae0fa16753d&longUrl={}".format(link)).text
    js = loads(req)
    link = js['data']['url']
    return link

@bot.message_handler(content_types=["text"])
def robot(message):
    if message.text == "/start":

        if message.from_user.id in config.ADMIN_ID:
            markup = types.InlineKeyboardMarkup()
            a = types.InlineKeyboardButton("Iran Cyber Security Group", url="https://iran-cyber.net")
            b = types.InlineKeyboardButton("Safe Data Hosting Co", url="https://safe-data.ir")
            markup.add(a)
            markup.add(b)
            bot.send_message(message.chat.id, "Yay, Admin 😎🌹\nSend me your Link", reply_markup=markup)

        else:

            if database.check_user(message.from_user.id) == "New_User":
                markup = types.InlineKeyboardMarkup()
                a = types.InlineKeyboardButton("En", callback_data="En")
                b = types.InlineKeyboardButton("Fa", callback_data="Fa")
                markup.add(a, b)
                bot.send_message(message.chat.id, "سلام [{}](tg://user?id={})\nبه ربات کوتاه کننده لینک ایران سایبر خوش آمدید\nزبان خود را انتخاب کنید\n➖➖➖➖➖➖\nHi [{}](tg://user?id={})\nWelcome to IRan Cyber Shortlink Bot\nSelect Your Language".format(message.from_user.first_name, message.from_user.id, message.from_user.first_name, message.from_user.id), reply_markup=markup, parse_mode="Markdown")
                for x in config.ADMIN_ID:
                    bot.send_message(x, "New user -> [{}](tg://user?id={})".format(message.from_user.first_name, message.from_user.id), parse_mode="markdown")

            else:

                if database.check_lang(message.from_user.id) == "Fa":
                    markup = types.InlineKeyboardMarkup()
                    change_lang = types.InlineKeyboardButton("تغییر زبان", callback_data="change_lang")
                    a = types.InlineKeyboardButton("Iran Cyber Security Group", url="https://iran-cyber.net")
                    b = types.InlineKeyboardButton("Safe Data Hosting Co", url="https://safe-data.ir")
                    markup.add(change_lang)
                    markup.add(a)
                    markup.add(b)
                    bot.send_message(message.chat.id, "سلام [{}](tg://user?id={})\nبه ربات کوتاه کننده لینک ایران سایبر خوش آمدید\nلینک خود را برای کوتاه شدن ارسال کنید".format(message.from_user.first_name, message.from_user.id), reply_markup=markup, parse_mode="Markdown")

                else:
                    markup = types.InlineKeyboardMarkup()
                    change_lang = types.InlineKeyboardButton("change language", callback_data="change_lang")
                    a = types.InlineKeyboardButton("Iran Cyber Security Group", url="https://iran-cyber.net")
                    b = types.InlineKeyboardButton("Safe Data Hosting Co", url="https://safe-data.ir")
                    markup.add(change_lang)
                    markup.add(a)
                    markup.add(b)
                    bot.send_message(message.chat.id, "Hi [{}](tg://user?id={})\nWelcome to IRan Cyber Shortlink Bot\nEnter Your Link".format(message.from_user.first_name, message.from_user.id), reply_markup=markup, parse_mode="Markdown")

    else:

        if message.text.startswith("http://") or message.text.startswith("https://"):
            markup = types.InlineKeyboardMarkup()
            a = types.InlineKeyboardButton("Iran Cyber Security Group", url="https://iran-cyber.net")
            b = types.InlineKeyboardButton("Safe Data Hosting Co", url="https://safe-data.ir")
            markup.add(a)
            markup.add(b)
            if message.from_user.id in config.ADMIN_ID:
                bot.send_message(message.chat.id, "Shorten Link : \n{}".format(short_link(message.text)), reply_markup=markup)
            else:
                if database.check_lang(message.from_user.id) == "Fa":
                    bot.send_message(message.chat.id, "لینک کوتاه شده ی شما \n{}".format(short_link(message.text)), reply_markup=markup)

                else:
                    bot.send_message(message.chat.id, "Shorten Link : \n{}".format(short_link(message.text)), reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    markup = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton("Iran Cyber Security Group", url="https://iran-cyber.net")
    b = types.InlineKeyboardButton("Safe Data Hosting Co", url="https://safe-data.ir")
    markup.add(a)
    markup.add(b)

    if call.data == "En":
        database.new_user(call.from_user.id, "En")
        bot.edit_message_text(text="your language was set to English", chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)

    if call.data == "Fa":
        database.new_user(call.from_user.id, "Fa")
        bot.edit_message_text(text="زبان شما فارسی شد", chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)

    if call.data == "change_lang":
        if database.check_lang(call.from_user.id) == "Fa":
            bot.edit_message_text(text="زبان شما به انگلیسی تغییر کرد", chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)
            database.change_to_en(call.from_user.id)

        else:
            bot.edit_message_text(text="Language Changed to Persian", chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)
            database.change_to_fa(call.from_user.id)
bot.polling(True)
