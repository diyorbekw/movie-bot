from aiogram import F
from aiogram.types import Message, CallbackQuery
from loader import dp, db, bot, MOVIE_CHANNEL
from keyboard_buttons.inline.menu import back_to_menu
from aiogram.fsm.context import FSMContext
from states.search_stt import SearchStates

@dp.callback_query(F.data == "search")
async def search_handler(callback: CallbackQuery, state: FSMContext):
    await state.set_state(SearchStates.movie_id)
    await callback.message.edit_text(text="Kino IDsini kiriting!", reply_markup=back_to_menu)
    await callback.answer()
    
@dp.message(F.text, SearchStates.movie_id)
async def search_handler(message: Message, state: FSMContext):
    movie_id = message.text
    await state.update_data(movie_id=movie_id)
    data = await state.get_data()
    movie_id = data.get("movie_id")
    await state.clear()
    
    movie = db.get_movie_by_id(movie_id=movie_id)
    
    
    await bot.copy_message(
        chat_id=message.from_user.id,
        from_chat_id=MOVIE_CHANNEL,
        message_id=movie[3].split('/')[5],
        caption=f"<b>🎬 Kino nomi</b>: {movie[1]}\n\n<b>📅 Kino Yili</b>: {movie[5]}\n\n<b>🌐 Kino tili</b>: {movie[4]}\n\n<b>🎬 Kino haqida</b>: {movie[2]}",
        reply_markup=back_to_menu,
        parse_mode="HTML"
    )