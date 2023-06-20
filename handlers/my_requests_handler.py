import sqlite3

from main import dp, types
from keyboards.other_keyboards import back_to_main_menu_keyboard


@dp.callback_query_handler(text='my_requests_button')
async def my_requests_button_handler(callback_query: types.CallbackQuery):
    conn = sqlite3.connect('database/db')
    cursor = conn.cursor()

    first_search = cursor.execute("SELECT search FROM users WHERE chat_id = ?", (callback_query.from_user.id, )).fetchone()[-1]
    second_search = cursor.execute("SELECT second_search FROM users WHERE chat_id =?", (callback_query.from_user.id, )).fetchone()[-1]
    third_search = cursor.execute("SELECT third_search FROM users WHERE chat_id = ?", (callback_query.from_user.id, )).fetchone()[-1]

    await callback_query.bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text=f'Ваши запросы:\n\n1: {first_search}\n2: {second_search}\n3: {third_search}', reply_markup=back_to_main_menu_keyboard)
    conn.close()