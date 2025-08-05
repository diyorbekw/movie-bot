from aiogram.fsm.state import State, StatesGroup

class SearchStates(StatesGroup):
    movie_id = State()