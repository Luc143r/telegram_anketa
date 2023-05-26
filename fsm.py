from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext


class Anketa(StatesGroup):
    question_1 = State()
    question_2 = State()
    question_3 = State()