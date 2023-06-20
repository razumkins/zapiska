from main import types, dp
from keyboards.other_keyboards import *
import sqlite3
from keyboards.main_menu_keyboards import main_menu_keyboard, main_menu__without_trial_vip_keyboard


@dp.callback_query_handler(text='back_to_main_menu_button')
async def back_to_main_menu_handler(callback_query: types.CallbackQuery):
    conn = sqlite3.connect('database/db')
    cursor = conn.cursor()

    check_trial_vip = cursor.execute("SELECT trial_vip FROM users WHERE chat_id = ?",
                                     (callback_query.from_user.id,)).fetchone()[-1]
    if check_trial_vip == 0:
        await callback_query.bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text='Главное меню: ', reply_markup=main_menu_keyboard)
    else:
        await callback_query.bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text='Главное меню: ', reply_markup=main_menu__without_trial_vip_keyboard)

    conn.commit()
    conn.close()