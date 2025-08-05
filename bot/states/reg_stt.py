from aiogram.fsm.state import State, StatesGroup

class RegisterStates(StatesGroup):
    phone_number = State()
    full_name = State()