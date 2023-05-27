from aiogram import types
from main import dp, bot
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
    owner_message_bot = await owner_message_bot.edit_text('Какая услуга Вам нужна?\n\n'
                                                        '1. Информационное обследование\n'
                                                        '2. Определение уровня информационной безопасности.\n'
                                                        '3. Разработка политик, концепций и другой документации по процессам обеспечения информационной безопасности.\n'
                                                        '4. Аудит и проверка на соответствие стандартам, нормативным актам, проектной документации и требованиям регуляторов.\n'
                                                        '5. Анализ рисков информационной безопасности\n'
                                                        '6. Другая услуга.')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_q2)
    data_question = await state.get_data()
    print(data_question)
    await Anketa.next()


@dp.callback_query_handler(lambda call: call.data == '/private', state=Anketa.question_1)
async def response_question_1(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_1='Частное лицо')
    owner_message_bot = await owner_message_bot.edit_text('Какая услуга Вам нужна?\n\n'
                                                        '1. Информационное обследование\n'
                                                        '2. Определение уровня информационной безопасности.\n'
                                                        '3. Разработка политик, концепций и другой документации по процессам обеспечения информационной безопасности.\n'
                                                        '4. Аудит и проверка на соответствие стандартам, нормативным актам, проектной документации и требованиям регуляторов.\n'
                                                        '5. Анализ рисков информационной безопасности\n'
                                                        '6. Другая услуга.')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_q2)
    data_question = await state.get_data()
    print(data_question)
    await Anketa.next()


list_service = []


@dp.callback_query_handler(lambda call: call.data == '/q2_r1', state=Anketa.question_2)
async def response_question_2(callback_query: types.CallbackQuery, state:FSMContext):
    global owner_message_bot
    global list_service
    await state.update_data(question_2='Информационное обследование')
    if 'Информационное обследование' not in list_service:
        list_service.append('Информационное обследование')
    data_question = await state.get_data()
    owner_message_bot = await owner_message_bot.edit_text('Выбранная услуга добавлена в список желаемых. Хотите выбрать еще услугу?\n\n'
                                                        '1. Информационное обследование\n'
                                                        '2. Определение уровня информационной безопасности.\n'
                                                        '3. Разработка политик, концепций и другой документации по процессам обеспечения информационной безопасности.\n'
                                                        '4. Аудит и проверка на соответствие стандартам, нормативным актам, проектной документации и требованиям регуляторов.\n'
                                                        '5. Анализ рисков информационной безопасности.\n'
                                                        '6. Другая услуга.')
    print(data_question)
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_q2_v2)


@dp.callback_query_handler(lambda call: call.data == '/q2_r2', state=Anketa.question_2)
async def response_question_2(callback_query: types.CallbackQuery, state:FSMContext):
    global owner_message_bot
    global list_service
    await state.update_data(question_2='Определение уровня информационной безопасности')
    if 'Определение уровня информационной безопасности' not in list_service:
        list_service.append('Определение уровня информационной безопасности')
    data_question = await state.get_data()
    owner_message_bot = await owner_message_bot.edit_text('Выбранная услуга добавлена в список желаемых. Хотите выбрать еще услугу?\n\n'
                                                        '1. Информационное обследование\n'
                                                        '2. Определение уровня информационной безопасности.\n'
                                                        '3. Разработка политик, концепций и другой документации по процессам обеспечения информационной безопасности.\n'
                                                        '4. Аудит и проверка на соответствие стандартам, нормативным актам, проектной документации и требованиям регуляторов.\n'
                                                        '5. Анализ рисков информационной безопасности.\n'
                                                        '6. Другая услуга.')
    print(data_question)
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_q2_v2)


@dp.callback_query_handler(lambda call: call.data == '/q2_r3', state=Anketa.question_2)
async def response_question_2(callback_query: types.CallbackQuery, state:FSMContext):
    global owner_message_bot
    global list_service
    await state.update_data(question_2='Разработка политик, концепций и другой документации по процессам обеспечения информационной безопасности')
    if 'Разработка политик, концепций и другой документации по процессам обеспечения информационной безопасности' not in list_service:
        list_service.append('Разработка политик, концепций и другой документации по процессам обеспечения информационной безопасности')
    data_question = await state.get_data()
    owner_message_bot = await owner_message_bot.edit_text('Выбранная услуга добавлена в список желаемых. Хотите выбрать еще услугу?\n\n'
                                                        '1. Информационное обследование\n'
                                                        '2. Определение уровня информационной безопасности.\n'
                                                        '3. Разработка политик, концепций и другой документации по процессам обеспечения информационной безопасности.\n'
                                                        '4. Аудит и проверка на соответствие стандартам, нормативным актам, проектной документации и требованиям регуляторов.\n'
                                                        '5. Анализ рисков информационной безопасности.\n'
                                                        '6. Другая услуга.')
    print(data_question)
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_q2_v2)


@dp.callback_query_handler(lambda call: call.data == '/q2_r4', state=Anketa.question_2)
async def response_question_2(callback_query: types.CallbackQuery, state:FSMContext):
    global owner_message_bot
    global list_service
    await state.update_data(question_2='Аудит и проверка на соответствие стандартам, нормативным актам, проектной документации и требованиям регуляторов')
    if 'Аудит и проверка на соответствие стандартам, нормативным актам, проектной документации и требованиям регуляторов' not in list_service:
        list_service.append('Аудит и проверка на соответствие стандартам, нормативным актам, проектной документации и требованиям регуляторов')
    data_question = await state.get_data()
    owner_message_bot = await owner_message_bot.edit_text('Выбранная услуга добавлена в список желаемых. Хотите выбрать еще услугу?\n\n'
                                                        '1. Информационное обследование\n'
                                                        '2. Определение уровня информационной безопасности.\n'
                                                        '3. Разработка политик, концепций и другой документации по процессам обеспечения информационной безопасности.\n'
                                                        '4. Аудит и проверка на соответствие стандартам, нормативным актам, проектной документации и требованиям регуляторов.\n'
                                                        '5. Анализ рисков информационной безопасности.\n'
                                                        '6. Другая услуга.')
    print(data_question)
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_q2_v2)


@dp.callback_query_handler(lambda call: call.data == '/q2_r5', state=Anketa.question_2)
async def response_question_2(callback_query: types.CallbackQuery, state:FSMContext):
    global owner_message_bot
    global list_service
    await state.update_data(question_2='Анализ рисков информационной безопасности')
    if 'Анализ рисков информационной безопасности' not in list_service:
        list_service.append('Анализ рисков информационной безопасности')
    data_question = await state.get_data()
    owner_message_bot = await owner_message_bot.edit_text('Выбранная услуга добавлена в список желаемых. Хотите выбрать еще услугу?\n\n'
                                                        '1. Информационное обследование\n'
                                                        '2. Определение уровня информационной безопасности.\n'
                                                        '3. Разработка политик, концепций и другой документации по процессам обеспечения информационной безопасности.\n'
                                                        '4. Аудит и проверка на соответствие стандартам, нормативным актам, проектной документации и требованиям регуляторов.\n'
                                                        '5. Анализ рисков информационной безопасности.\n'
                                                        '6. Другая услуга.')
    print(data_question)
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_q2_v2)


@dp.callback_query_handler(lambda call: call.data == '/q2_r6', state=Anketa.question_2)
async def response_question_2(callback_query: types.CallbackQuery, state:FSMContext):
    global owner_message_bot
    global list_service
    await state.update_data(question_2='Другая услуга')
    if 'Другая услуга' not in list_service:
        list_service.append('Другая услуга')
    data_question = await state.get_data()
    owner_message_bot = await owner_message_bot.edit_text('Выбранная услуга добавлена в список желаемых. Хотите выбрать еще услугу?\n\n'
                                                        '1. Информационное обследование\n'
                                                        '2. Определение уровня информационной безопасности.\n'
                                                        '3. Разработка политик, концепций и другой документации по процессам обеспечения информационной безопасности.\n'
                                                        '4. Аудит и проверка на соответствие стандартам, нормативным актам, проектной документации и требованиям регуляторов.\n'
                                                        '5. Анализ рисков информационной безопасности.\n'
                                                        '6. Другая услуга.')
    print(data_question)
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_q2_v2)


@dp.callback_query_handler(lambda call: call.data == '/next_q', state=Anketa.question_2)
async def response_question_2(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    global list_service
    await state.update_data(question_2=list_service)
    owner_message_bot = await owner_message_bot.edit_text('Пришлите Ваши контактные данные в чат\n\n')
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


@dp.message_handler(state=Anketa.question_3)
async def response_q3(message: types.Message, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_3=message.text)
    await message.delete()
    await owner_message_bot.delete()
    owner_message_bot = await bot.send_message(message.chat.id, 'Ваше обращение принято, скоро с Вами свяжется специалистка для обсуждения деталей.')
    data_question = await state.get_data()
    print(data_question)
    await state.finish()