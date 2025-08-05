from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔎 Kino izlash", callback_data="search")
        ],
        [
            InlineKeyboardButton(text="👤 Profil", callback_data="profile")
        ]
    ]
)

back_to_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 Orqaga", callback_data="main_menu")
        ]
    ]
)