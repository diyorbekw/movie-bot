from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

register_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Telefon raqamni yuborish", request_contact=True)
        ]
    ]
)