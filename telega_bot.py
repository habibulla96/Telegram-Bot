import telebot
import os
import atexit
import json

from parsing import parse_page
from telebot import types
from decouple import config

# Config TOKEN
TOKEN = config('TOKEN')
bot = telebot.TeleBot(TOKEN)

# Keyboards
main_keyboard = types.InlineKeyboardMarkup(row_width=1)
main_key_info = types.InlineKeyboardMarkup(row_width=1)
main_key_return = types.InlineKeyboardMarkup(row_width=1)

news = types.InlineKeyboardButton('Читать новости', callback_data='news')
create = types.InlineKeyboardButton('Создать новость', callback_data='create')
url = types.InlineKeyboardButton('Ссылка', callback_data='url')
back_ = types.InlineKeyboardButton('Назад', callback_data='back_')
back_1 = types.InlineKeyboardButton('Назад', callback_data='back_1')
return_ = types.InlineKeyboardButton('Вернуться', callback_data='return_')
exit_ = types.InlineKeyboardButton('Выйти', callback_data='exit_')

main_keyboard.add(news, create, exit_)
main_key_info.add(url, back_, exit_)
main_key_return.add(return_)


main_numbers = types.InlineKeyboardMarkup(row_width=5)
btn1 = types.InlineKeyboardButton('1', callback_data='btn1')
btn2 = types.InlineKeyboardButton('2', callback_data='btn2')
btn3 = types.InlineKeyboardButton('3', callback_data='btn3')
btn4 = types.InlineKeyboardButton('4', callback_data='btn4')
btn5 = types.InlineKeyboardButton('5', callback_data='btn5')
btn6 = types.InlineKeyboardButton('6', callback_data='btn6')
btn7 = types.InlineKeyboardButton('7', callback_data='btn7')
btn8 = types.InlineKeyboardButton('8', callback_data='btn8')
btn9 = types.InlineKeyboardButton('9', callback_data='btn9')
btn10 = types.InlineKeyboardButton('10', callback_data='btn10')
btn11 = types.InlineKeyboardButton('11', callback_data='btn11')
btn12 = types.InlineKeyboardButton('12', callback_data='btn12')
btn13 = types.InlineKeyboardButton('13', callback_data='btn13')
btn14 = types.InlineKeyboardButton('14', callback_data='btn14')
btn15 = types.InlineKeyboardButton('15', callback_data='btn15')
btn16 = types.InlineKeyboardButton('16', callback_data='btn16')
btn17 = types.InlineKeyboardButton('17', callback_data='btn17')
btn18 = types.InlineKeyboardButton('18', callback_data='btn18')
btn19 = types.InlineKeyboardButton('19', callback_data='btn19')
btn20 = types.InlineKeyboardButton('20', callback_data='btn20')

main_numbers.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, 
            btn11, btn12, btn13, btn14, btn15, btn16, btn17, btn18, btn19, btn20, back_1, exit_)
   

# Command Start
@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    user = message.chat.first_name
    img = ("https://bit.ly/3okPJ0M")
    bot.send_photo(chat_id, img)
    bot.send_message(chat_id, f"Добро пожаловать {user}!\nНовостной Телеграм Бот Kaktus.media", reply_markup=main_keyboard)


# Call Keyboards
@bot.callback_query_handler(lambda call:True)
def call_data(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    user = call.message.chat.first_name


    if call.data == 'news':
        new = get_infooo(0)
        textt = ""
        for i, nw in enumerate(new):
            ti = (f"{i+1}) {str(nw)}\n")
            textt = textt + ti
        bot.edit_message_text(f"{textt}", message_id=message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=message_id, chat_id=chat_id, reply_markup=main_numbers)


    if call.data == "btn1":
        btn_1 = main_key(1)
        all_ = all_info(1)
        bot.edit_message_text(f"{all_}", message_id=message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=message_id, chat_id=chat_id, reply_markup=btn_1)

    if call.data == "btn2":
        btn_2 = main_key(2)
        all_ = all_info(2)
        bot.edit_message_text(f"{all_}", message_id=message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=message_id, chat_id=chat_id, reply_markup=btn_2)
    
    if call.data == "btn3":
        btn_3 = main_key(3)
        all_ = all_info(3)
        bot.edit_message_text(f"{all_}", message_id=message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=message_id, chat_id=chat_id, reply_markup=btn_3)
    
    if call.data == "btn4":
        btn_4 = main_key(4)
        all_ = all_info(4)
        bot.edit_message_text(f"{all_}", message_id=message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=message_id, chat_id=chat_id, reply_markup=btn_4)

    if call.data == "btn5":
        btn_5 = main_key(5)
        all_ = all_info(5)
        bot.edit_message_text(f"{all_}", message_id=message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=message_id, chat_id=chat_id, reply_markup=btn_5)

    if call.data == "btn6":
        btn_6 = main_key(6)
        all_ = all_info(6)
        bot.edit_message_text(f"{all_}", message_id=message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=message_id, chat_id=chat_id, reply_markup=btn_6)

    if call.data == "btn7":
        btn_7 = main_key(7)
        all_ = all_info(7)
        bot.edit_message_text(f"{all_}", message_id=message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=message_id, chat_id=chat_id, reply_markup=btn_7)

    if call.data == "btn8":
        btn_8 = main_key(8)
        all_ = all_info(8)
        bot.edit_message_text(f"{all_}", message_id=message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=message_id, chat_id=chat_id, reply_markup=btn_8)

    if call.data == "btn9":
        btn_9 = main_key(9)
        all_ = all_info(9)
        bot.edit_message_text(f"{all_}", message_id=message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=message_id, chat_id=chat_id, reply_markup=btn_9)

    if call.data == "btn10":
        btn_10 = main_key(10)
        all_ = all_info(10)
        bot.edit_message_text(f"{all_}", message_id=message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=message_id, chat_id=chat_id, reply_markup=btn_10)
    
    if call.data == "btn11":
        btn_11 = main_key(11)
        all_ = all_info(11)
        bot.edit_message_text(f"{all_}", message_id=message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=message_id, chat_id=chat_id, reply_markup=btn_11)
    
    if call.data == "btn12":
        btn_12 = main_key(12)
        all_ = all_info(12)
        bot.edit_message_text(f"{all_}", message_id=message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=message_id, chat_id=chat_id, reply_markup=btn_12)
    
    if call.data == "btn13":
        btn_13 = main_key(13)
        all_ = all_info(13)
        bot.edit_message_text(f"{all_}", message_id=message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=message_id, chat_id=chat_id, reply_markup=btn_13)

    if call.data == "btn14":
        btn_14 = main_key(14)
        all_ = all_info(14)
        bot.edit_message_text(f"{all_}", message_id=message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=message_id, chat_id=chat_id, reply_markup=btn_14)

    if call.data == "btn15":
        btn_15 = main_key(15)
        all_ = all_info(15)
        bot.edit_message_text(f"{all_}", message_id=message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=message_id, chat_id=chat_id, reply_markup=btn_15)

    if call.data == "btn16":
        btn_16 = main_key(16)
        all_ = all_info(16)
        bot.edit_message_text(f"{all_}", message_id=message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=message_id, chat_id=chat_id, reply_markup=btn_16)

    if call.data == "btn17":
        btn_17 = main_key(17)
        all_ = all_info(17)
        bot.edit_message_text(f"{all_}", message_id=message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=message_id, chat_id=chat_id, reply_markup=btn_17)

    if call.data == "btn18":
        btn_18 = main_key(18)
        all_ = all_info(18)
        bot.edit_message_text(f"{all_}", message_id=message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=message_id, chat_id=chat_id, reply_markup=btn_18)

    if call.data == "btn19":
        btn_19 = main_key(19)
        all_ = all_info(19)
        bot.edit_message_text(f"{all_}", message_id=message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=message_id, chat_id=chat_id, reply_markup=btn_19)

    if call.data == "btn20":
        btn_20 = main_key(20)
        all_ = all_info(20)
        bot.edit_message_text(f"{all_}", message_id=message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=message_id, chat_id=chat_id, reply_markup=btn_20)

    if call.data == 'create':
        create_url = types.InlineKeyboardMarkup(row_width=2)
        url2 = types.InlineKeyboardButton("Ссылка", url="https://kaktus.media/?user_news&l=15")
        create_url.add(url2, back_1)
        bot.edit_message_text(text="Нажмите на (Ссылку) для создания своей новости: ", message_id=message_id, chat_id=chat_id, reply_markup=create_url)

    if call.data == 'exit_':
        bot.edit_message_text(text=f"До встречи {user}!", message_id=message_id, chat_id=chat_id, reply_markup=main_key_return)
        os.remove("data_file.json")
    
    if call.data == 'return_':
        parse_page()
        bot.edit_message_text(text=f"Снова рады вас видеть {user}!", message_id=message_id, chat_id=chat_id, reply_markup=main_keyboard)
        
    if call.data == 'back_1':
        bot.edit_message_text(f"Добро пожаловать {user}!\nНовостной Телеграм Бот Kaktus.media", message_id=message_id, chat_id=chat_id, reply_markup=main_keyboard)

    if call.data == 'back_':
        new = get_infooo(0)
        textt = ""
        for i, nw in enumerate(new):
            ti = (f"{i+1}) {str(nw)}\n")
            textt = textt + ti
        bot.edit_message_text(f"{textt}", message_id=message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=message_id, chat_id=chat_id, reply_markup=main_numbers)


def main_key(i):
    main_key_new = types.InlineKeyboardMarkup(row_width=2)
    photo = get_photo(i)
    url_ = get_url(i)
    url = types.InlineKeyboardButton("Ссылка", url=url_)
    photo = types.InlineKeyboardButton("Фото", photo)
    main_key_new.add(url, photo, back_, exit_)
    return main_key_new


def get_infooo(i):
    with open("data_file.json", "r") as f:
        data = json.loads(f.read())
    
    info = data[i]

    return info[:20]


def get_news(i):
    news = get_infooo(0)
    for new in news[i-1:i]:
        return f"{i}) {str(new)}"


def get_url(i):
    urls = get_infooo(1)
    for url in urls[i-1:i]:
        return url


def get_desc(i):
    desc_ = get_infooo(2)
    for des in desc_[i-1:i]:
        return des
    

def get_photo(i):
    photos = get_infooo(3)
    for photo in photos[i-1:i]:
        return photo


def all_info(i):
    item = str(all_filter(i))
    item1 = item.replace("[", "").replace("]", "").replace("'", "")
    all_in = f"{get_news(i)}\nОписание:\n{item1}"
    return all_in


def all_filter(i):
    with open("data_file.json", "r") as f:
        data = json.loads(f.read())

    info = data[2]

    all_infos = list(filter(None, info))
    return all_infos[i-1:i]


def main():
    parse_page()


main()


def exit_handler():
    os.remove("data_file.json")


atexit.register(exit_handler)


if __name__ == '__main__':
    bot.polling(none_stop=True)
