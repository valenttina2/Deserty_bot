#5533009771:AAEOV7B3ImfCo_oi4sjVcG2_mfumSDakpHQ

import telebot
from telebot import types
#import logging

token = '5533009771:AAEOV7B3ImfCo_oi4sjVcG2_mfumSDakpHQ'

bot = telebot.TeleBot(token)
cake_data= {"med": ["Медовик",1],
            "tra": ["Трайфл",2],
            "pav": ["Павлова",3],
            "mak": ["Макарон",4],
            "kap": ["Капкейк",5],
            }
logger = telebot.logger
# telebot.logger.setLevel(logging.DEBUG)
# "id":-1001605514697 - канал для заказов


def create_keyboard(): #функция для создания кнопок
    menu = types.InlineKeyboardMarkup()
    for k,v in cake_data.items():
        cake_btn = types.InlineKeyboardButton(text=v[0], callback_data=k)
        menu.add(cake_btn)
    return menu

@bot.message_handler(commands=['start']) #декоратор указывает, в каком случае выполнять функцию, в данном случае при команде старт
def start_bot(message): #функция при старте бота
    keyboard = create_keyboard()
    bot.send_message(
        message.chat.id,
        'Добрый день, выберите, что вы хотите',
        reply_markup=keyboard
    )

def to_back_menu():
    back_menu = types.InlineKeyboardMarkup()
    back_menu_btn = types.InlineKeyboardButton(text="Вернуться в основное меню",
                                               callback_data="back")
    back_menu.add(back_menu_btn)
    return back_menu

def make_choice(choice_cake):
    choice = types.InlineKeyboardMarkup()
    description_btn = types.InlineKeyboardButton(text='Описание',
                                            callback_data=f'description_{cake_data[choice_cake][1]}')
    order_btn = types.InlineKeyboardButton(text='Заказать',
                                             callback_data=f'order_{cake_data[choice_cake][1]}')
    choice.add(description_btn)
    choice.add(order_btn)
    return choice

def order_done(message):
    keyboard = create_keyboard()
    bot.send_message(
        message.chat.id,
        f'Ваш заказ: {message.text}.  Скоро мы свяжемся с вами.  '
        f' Выберите еще десерт?',
        reply_markup=keyboard)
    # bot.send_message(
    #     chat_id ='-1001605514697',
    #     text = f'Новый заказ от: {message.text}')
    bot.forward_message(
        chat_id=-1001605514697,  # chat_id чата в которое необходимо переслать сообщение
        from_chat_id=message.chat.id,  # chat_id из которого необходимо переслать сообщение
        message_id=message.message_id # message_id которое необходимо переслать
    )

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call): #функция дейтвий, при нажатии на кнопки
    keyboard = create_keyboard()
    back_menu = to_back_menu()

    if call.message: #проверяем, есть ли вообще сообщение
        
        if call.data in cake_data:
            bot.send_message(
                chat_id=call.message.chat.id,
                text=f'Вы выбрали {cake_data[call.data][0]}:',
                reply_markup=make_choice(call.data)
            )

        if call.data == 'description_1':
            img = open('медовік.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Медовик",
                )
            img.close()
            bot.send_message(
                call.message.chat.id,
                'Медовые коржи и нежный сливочный крем. '
                'Веc 2100 г. Стоимость 50 р.',
                reply_markup=back_menu)

        if call.data == 'order_1':
            msg = bot.send_message(
                call.message.chat.id,
                'Для заказа напишите, какое количество десерта вы хотите, '
                'и на каку дату хотите заказать',
                reply_markup=back_menu)
            bot.register_next_step_handler(msg, order_done)

        if call.data == 'description_2':
            img = open('тра.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Трайфл")
            img.close()
            bot.send_message(
                call.message.chat.id,
                'Порционный десерт. Ванильный или шоколадный бисквит '
                'с прослойкой из нежного сливочного крема.'
                'Веc одной порции 200 г. Минимальный заказ от 3 порций. '
                'Стоимость за 1 порцию 4 р.',
                reply_markup=back_menu)


        if call.data == 'order_2':
            msg = bot.send_message(
                call.message.chat.id,
                'Для заказа напишите, какое количество десерта вы хотите, '
                'и на каку дату хотите заказать',
                reply_markup=back_menu)
            bot.register_next_step_handler(msg, order_done)

        if call.data == 'description_3':
            img = open('павлово.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Павлова"
                )
            img.close()
            bot.send_message(
                call.message.chat.id,
                'Сладкий десерт с ягодной или фруктовой начинкой и кремчизом. '
                'Вкусное сочетание для любителей необычного. '
                'Веc 150 г. Заказ от 3 шт. Стоимость 5 р. за шт.',
                reply_markup=back_menu)


        if call.data == 'order_3':
            msg = bot.send_message(
                call.message.chat.id,
                'Для заказа напишите, какое количество десерта вы хотите, '
                'и на каку дату хотите заказать',
                reply_markup=back_menu)
            bot.register_next_step_handler(msg, order_done)

        if call.data == 'description_4':
            img = open('макарон.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Макарон")
            img.close()
            bot.send_message(
                call.message.chat.id,
                'Нежнейшее миндальное безе с кремовой или шоколадной начинкой. '
                'Веc 50 г. Заказ от 6 шт. Стоимость 2 р. за шт.',
                 reply_markup=back_menu)


        if call.data == 'order_4':
            msg = bot.send_message(
                call.message.chat.id,
                'Для заказа напишите, какое количество десерта вы хотите, '
                'и на каку дату хотите заказать',
                reply_markup=back_menu)
            bot.register_next_step_handler(msg, order_done)

        if call.data == 'description_5':
            img = open('капкейк.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Капкейк")
            img.close()
            bot.send_message(
                call.message.chat.id,
                'Вкусный десерт с начинкой из ягод/карамели '
                'с нежным кремом на основе белого шоколада. '
                'Веc 150 г. Заказ от 3 шт. Стоимость 4 р. за шт.',
                reply_markup=back_menu)

        if call.data == 'order_5':
            msg = bot.send_message(
                call.message.chat.id,
                'Для заказа напишите, какое количество десерта вы хотите, '
                'и на каку дату хотите заказать',
                reply_markup=back_menu)
            bot.register_next_step_handler(msg, order_done)

        if call.data == "back":
            bot.send_message(
                chat_id=call.message.chat.id,
                text="Не понравилось? Попробуй выбрать другой десерт:",
                reply_markup=keyboard
            )



if __name__ == '__main__':
    bot.polling(none_stop=True)