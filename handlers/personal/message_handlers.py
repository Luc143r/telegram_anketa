from aiogram import types
from main import dp, bot, counter_response, list_users
from fsm import *
from keyboard import *
import re


########################################
# Callback handlers / Обрабочтики кнопок
########################################

###################
# Заполнение анкеты
###################


@dp.callback_query_handler(lambda call: call.data == '/go_to_anket')
async def start_test_one(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    owner_message_bot = await owner_message_bot.edit_text('Вы компания или частное лицо?')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_question_1)
    await Anketa().question_1.set()
    await callback_query.answer()


@dp.callback_query_handler(lambda call: call.data == '/company', state=Anketa.question_1)
async def response_question_1(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_1='Компания')
    owner_message_bot = await owner_message_bot.edit_text('Какая услуга Вам нужна?')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_q2)
    data_question = await state.get_data()
    print(data_question)
    await Anketa.next()


@dp.callback_query_handler(lambda call: call.data == '/private', state=Anketa.question_1)
async def response_question_1(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_1='Частное лицо')
    owner_message_bot = await owner_message_bot.edit_text('Какая услуга Вам нужна?')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_q2)
    data_question = await state.get_data()
    print(data_question)
    await Anketa.next()


##########################################
# Message handlers / Обрабочтики сообщений
##########################################


@dp.message_handler(commands='start')
async def command_start(message: types.Message):
    global owner_message_bot
    owner_message_bot = await bot.send_message(message.chat.id, 'Этот чат-бот поможет составить анкету-обращение.', reply_markup=markup_start_anket)
    print(message.chat.id)
    await message.delete()
