from aiogram import F
from aiogram.types import Message, CallbackQuery
from loader import dp, db
from keyboard_buttons.inline.menu import back_to_menu

@dp.callback_query(F.data == "profile")
async def profile_handler(callback: CallbackQuery):
    user = db.select_user(telegram_id=callback.from_user.id)
    telegram_id = user[1]
    full_name = user[2]
    phone_number = user[3]
    
    txt = f"""
Sizning profilingiz:

<b>🆔 Telegram ID</b>: {telegram_id}
<b>👤 Ism familiya</b>: {full_name}
<b>📞 Telefon raqam</b>: +{phone_number}

    """
    await callback.message.edit_text(text=txt, parse_mode="HTML", reply_markup=back_to_menu)
    
    await callback.answer()