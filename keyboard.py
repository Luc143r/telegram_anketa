from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


###############
# Кнопка отмены
###############


button_cancel = InlineKeyboardButton('Cancel', callback_data='/cancel')
markup_cancel = InlineKeyboardMarkup()
markup_cancel.row(button_cancel)

button_back_to_menu = InlineKeyboardButton(
    'Вернуться в меню', callback_data='/back_to_menu')
markup_back_to_menu = InlineKeyboardMarkup()
markup_back_to_menu.row(button_back_to_menu)

button_start_anket = InlineKeyboardButton(
    'Всё понятно, перейти к анкете', callback_data='/go_to_anket')
markup_start_anket = InlineKeyboardMarkup()
markup_start_anket.row(button_start_anket)


button_company = InlineKeyboardButton(
    'Компания', callback_data='/company')
button_private = InlineKeyboardButton(
    'Частное лицо', callback_data='/private')
markup_question_1 = InlineKeyboardMarkup()
markup_question_1.row(button_company, button_private)


button_q2_r1 = InlineKeyboardButton('1', callback_data='/q2_r1')
button_q2_r2 = InlineKeyboardButton('2', callback_data='/q2_r2')
button_q2_r3 = InlineKeyboardButton('3', callback_data='/q2_r3')
button_q2_r4 = InlineKeyboardButton('4', callback_data='/q2_r4')
button_q2_r5 = InlineKeyboardButton('5', callback_data='/q2_r5')
button_q2_r6 = InlineKeyboardButton('6', callback_data='/q2_r6')
button_next_q = InlineKeyboardButton(
    'Следующий вопрос', '/next_q')
markup_q2 = InlineKeyboardMarkup()
markup_q2.row(button_q2_r1, button_q2_r2, button_q2_r3)
markup_q2.row(button_q2_r4, button_q2_r5, button_q2_r6)
markup_q2_v2 = InlineKeyboardMarkup()
markup_q2_v2.row(button_q2_r1, button_q2_r2, button_q2_r3)
markup_q2_v2.row(button_q2_r4, button_q2_r5, button_q2_r6)
markup_q2_v2.row(button_next_q)
