import asyncio
from main import types, dp
import sqlite3
from keyboards.other_keyboards import back_to_main_menu_keyboard


@dp.callback_query_handler(text='get_trial_vip_status_button')
async def get_trial_vip_status_button_handler(callback_query: types.CallbackQuery):
    await callback_query.bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text='Вы получили пробный вип статус на 3 дня.', reply_markup=back_to_main_menu_keyboard)

    conn = sqlite3.connect('database/db')
    cursor = conn.cursor()

    cursor.execute("UPDATE users SET trial_vip = ?, vip = ?, vip_time = ? WHERE chat_id = ?",
                   (1, 1, 259200, callback_query.from_user.id, ))

    cursor.execute("UPDATE users SET second_search = ?, third_search = ? WHERE chat_id = ?",
                   ('Не задан', 'Не задан', callback_query.from_user.id, ))

    time = cursor.execute("SELECT vip_time FROM users WHERE chat_id = ?", (callback_query.from_user.id,)).fetchone()[-1]

    while time > 0:
        cursor.execute(f"UPDATE users SET vip_time = {time} - 1 WHERE chat_id = ?", (callback_query.from_user.id, ))
        conn.commit()
        await asyncio.sleep(1)
        time -= 1
        if time == 0:
            await callback_query.bot.send_message(chat_id=callback_query.from_user.id, text='У вас закончился вип статус.')
            cursor.execute("UPDATE users SET vip = ?, second_search = ?, third_search = ? WHERE chat_id = ?", (0, 'Нет вип', 'Нет вип', callback_query.from_user.id, ))
            conn.commit()
            break
    conn.commit()
    conn.close()