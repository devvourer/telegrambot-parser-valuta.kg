import telebot
from telebot import types
from decouple import config
from valuta_parser import get_buy_usd, get_sell_usd, main
import json

bot = telebot.TeleBot(config('TOKEN'))

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn1 = types.KeyboardButton('Валюта')
btn2 = types.KeyboardButton('Новости')
keyboard.add(btn1, btn2)

quit = types.ReplyKeyboardMarkup(resize_keyboard=True)
button = types.KeyboardButton('quit')
quit.add(button)


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'choose one of this', reply_markup=keyboard)


# Обработчик кнопок (Валюта, Новости)
@bot.message_handler(content_types=['text'])
def send_text(message):
    chat_id = message.chat.id

    if message.text == message.text.startswith('['):
        bot.send_message(chat_id, ' . ', reply_markup=quit)
    if message.text.lower() == 'quit':
        bot.send_message(chat_id, 'До свидания')

    if message.text.lower() == 'валюта':
        inline_kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton('USD', callback_data='usd')
        btn2 = types.InlineKeyboardButton('EUR', callback_data='eur')
        btn3 = types.InlineKeyboardButton('RUB', callback_data='rub')
        btn4 = types.InlineKeyboardButton('TENGE', callback_data='tenge')
        inline_kb.add(btn1, btn2, btn3, btn4)
        bot.send_message(chat_id, 'What are we do ?', reply_markup=inline_kb)


@bot.callback_query_handler(func=lambda call: True)
def inline_kb(call):
    chat_id = call.message.chat.id

    if call.data == 'usd':
        kb_usd = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('buy', callback_data='buy')
        btn2 = types.InlineKeyboardButton('sell', callback_data='sell')
        kb_usd.add(btn1, btn2)
        bot.send_message(chat_id, 'what are we do?', reply_markup=kb_usd)

    if call.data == 'buy':
        show = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('show', callback_data='show')
        btn2 = types.InlineKeyboardButton('save as json', callback_data='save')
        show.add(btn1, btn2)
        bot.send_message(chat_id, 'save or show?', reply_markup=show)

    if call.data == 'sell':
        show = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('show', callback_data='show1')
        btn2 = types.InlineKeyboardButton('save as json', callback_data='save1')
        show.add(btn1, btn2)
        bot.send_message(chat_id, 'save or show?', reply_markup=show)

    if call.data == 'show':
        data = get_buy_usd(main(), 0, 1)
        bot.send_message(chat_id, f'{data}')
        bot.send_message(chat_id, 'quit', reply_markup=quit)
    if call.data == 'save':
        data = main()
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        bot.send_message(chat_id, 'quit', reply_markup=quit)

    if call.data == 'show1':
        data = get_buy_usd(main(), 0, 2)
        bot.send_message(chat_id, f'{data}')
        bot.send_message(chat_id, 'quit', reply_markup=quit)
    if call.data == 'save1':
        data = main()
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        bot.send_message(chat_id, 'quit', reply_markup=quit)

    if call.data == 'eur':
        kb_usd = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('buy', callback_data='buy3')
        btn2 = types.InlineKeyboardButton('sell', callback_data='sell3')
        kb_usd.add(btn1, btn2)
        bot.send_message(chat_id, 'what are we do?', reply_markup=kb_usd)

    if call.data == 'buy3':
        show = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('show', callback_data='show3')
        btn2 = types.InlineKeyboardButton('save as json', callback_data='save3')
        show.add(btn1, btn2)
        bot.send_message(chat_id, 'save or show?', reply_markup=show)

    if call.data == 'sell3':
        show = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('show', callback_data='show31')
        btn2 = types.InlineKeyboardButton('save as json', callback_data='save31')
        show.add(btn1, btn2)
        bot.send_message(chat_id, 'save or show?', reply_markup=show)

    if call.data == 'show3':
        data = get_buy_usd(main(), 0, 3)
        bot.send_message(chat_id, f'{data}')
        bot.send_message(chat_id, 'quit', reply_markup=quit)
    if call.data == 'save3':
        data = main()
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        bot.send_message(chat_id, 'quit', reply_markup=quit)

    if call.data == 'show31':
        data = get_buy_usd(main(), 0, 4)
        bot.send_message(chat_id, f'{data}')
        bot.send_message(chat_id, 'quit', reply_markup=quit)
    if call.data == 'save31':
        data = main()
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        bot.send_message(chat_id, 'quit', reply_markup=quit)

    if call.data == 'rub':
        kb_usd = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('buy', callback_data='buy4')
        btn2 = types.InlineKeyboardButton('sell', callback_data='sell4')
        kb_usd.add(btn1, btn2)
        bot.send_message(chat_id, 'what are we do?', reply_markup=kb_usd)

    if call.data == 'buy4':
        show = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('show', callback_data='show4')
        btn2 = types.InlineKeyboardButton('save as json', callback_data='save4')
        show.add(btn1, btn2)
        bot.send_message(chat_id, 'save or show?', reply_markup=show)

    if call.data == 'sell4':
        show = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('show', callback_data='show41')
        btn2 = types.InlineKeyboardButton('save as json', callback_data='save41')
        show.add(btn1, btn2)
        bot.send_message(chat_id, 'save or show?', reply_markup=show)

    if call.data == 'show4':
        data = get_buy_usd(main(), 0, 5)
        bot.send_message(chat_id, f'{data}')
        bot.send_message(chat_id, 'quit', reply_markup=quit)
    if call.data == 'save4':
        data = main()
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        bot.send_message(chat_id, 'quit', reply_markup=quit)

    if call.data == 'show41':
        data = get_sell_usd(main(), 0, 6)
        bot.send_message(chat_id, f'{data}')
        bot.send_message(chat_id, 'quit', reply_markup=quit)
    if call.data == 'save41':
        data = main()
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        bot.send_message(chat_id, 'quit', reply_markup=quit)

    if call.data == 'tenge':
        kb_usd = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('buy', callback_data='buy5')
        btn2 = types.InlineKeyboardButton('sell', callback_data='sell5')
        kb_usd.add(btn1, btn2)
        bot.send_message(chat_id, 'what are we do?', reply_markup=kb_usd)

    if call.data == 'buy5':
        show = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('show', callback_data='show5')
        btn2 = types.InlineKeyboardButton('save as json', callback_data='save5')
        show.add(btn1, btn2)
        bot.send_message(chat_id, 'save or show?', reply_markup=show)

    if call.data == 'sell5':
        show = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('show', callback_data='show51')
        btn2 = types.InlineKeyboardButton('save as json', callback_data='save51')
        show.add(btn1, btn2)
        bot.send_message(chat_id, 'save or show?', reply_markup=show)

    if call.data == 'show5':
        data = get_buy_usd(main(), 0, 7)
        bot.send_message(chat_id, f'{data}')
        bot.send_message(chat_id, 'quit', reply_markup=quit)
    if call.data == 'save5':
        data = main()
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        bot.send_message(chat_id, 'quit', reply_markup=quit)

    if call.data == 'show51':
        data = get_sell_usd(main(), 0, 8)
        bot.send_message(chat_id, f'{data}')
        bot.send_message(chat_id, 'quit', reply_markup=quit)
    if call.data == 'save51':
        data = main()
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

        bot.send_message(chat_id, 'quit', reply_markup=quit)


@bot.message_handler()
def send_quit(message):
    chat_id = message.chat.id

    if message.text.lower == message.text.startswith('['):
        bot.send_message(chat_id, 'quit', reply_markup=quit)


bot.polling()
