from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp,db
from aiogram.filters import CommandStart
from keyboard_buttons.inline.menu import menu
from keyboard_buttons.default.user_keyboard import register_button
from states.reg_stt import RegisterStates
from aiogram.fsm.context import FSMContext
from aiogram import F

@dp.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    user = db.select_user(telegram_id=message.from_user.id)
    if user:
        await message.answer(f"Assalomu alaykum, Kino botiga xush kelibsiz!", reply_markup=menu)
        return
        
    await message.answer("Assalomu alaykum, botdan foydalanish uchun telefon raqamingini yuboring.\nPastdagi tugmani bosishingiz mumkin.", reply_markup=register_button)
    await state.set_state(RegisterStates.phone_number)
    
@dp.message(F.contact, RegisterStates.phone_number)
async def phone_number(message:Message,state:FSMContext):
    phone_number = message.contact.phone_number
    
    await state.update_data(phone_number=phone_number)
    await state.set_state(RegisterStates.full_name)
    
    await message.answer("Ajoyib! Endi esa ism-familiyangizni kiriting!", reply_markup=ReplyKeyboardRemove(remove_keyboard=True))

@dp.message(RegisterStates.full_name)
async def full_name(message: Message, state: FSMContext):
    full_name = message.text
    await state.update_data(full_name=full_name)
    data = await state.get_data()
    phone_number = data.get("phone_number")
    await state.clear()
    telegram_id = message.from_user.id

    db.add_user(phone_number=phone_number,full_name=full_name, telegram_id=telegram_id)
    await message.answer(f"Assalomu alaykum, Kino botiga xush kelibsiz!", reply_markup=menu)