from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    msg = State()
    finish = State()
