from aiogram import F
from aiogram.types import Message, CallbackQuery
from loader import dp, db
from keyboard_buttons.inline.menu import menu

@dp.callback_query(F.data == "main_menu")
async def main_menu_handler(callback: CallbackQuery):
    try:
        await callback.message.edit_text(text="Assalomu alaykum, Kino botiga xush kelibsiz!", reply_markup=menu)
    
    except:
        await callback.message.delete()
        await callback.message.answer(text="Assalomu alaykum, Kino botiga xush kelibsiz!", reply_markup=menu)
    
    await callback.answer()
    
    