from aiogram.fsm.state import State, StatesGroup


class StatesGroup(StatesGroup):
    message = State()
    confirmation = State()