from main import types, dp
import sqlite3
from keyboards.main_menu_keyboards import *


@dp.message_handler(commands=['start'])
async def start_command_handler(message: types.Message):
    conn = sqlite3.connect('database/db')
    cursor = conn.cursor()
    check_user = cursor.execute("SELECT username FROM users WHERE chat_id = ?", (message.from_user.id, )).fetchone()
    if check_user:
        check_trial_vip = cursor.execute("SELECT trial_vip FROM users WHERE chat_id = ?", (message.from_user.id, )).fetchone()[-1]
        if check_trial_vip == 0:
            await message.answer('Главное меню: ', reply_markup=main_menu_keyboard)
        else:
            await message.answer('Главное меню: ', reply_markup=main_menu__without_trial_vip_keyboard)
    else:
        await message.answer('Привет, ты первый раз у нас? Обязательно прочти "Обо мне".', reply_markup=main_menu_keyboard)

        username = message.from_user.username
        chat_id = message.from_user.id

        cursor.execute("INSERT INTO users (username, chat_id, trial_vip, vip, vip_time, search, second_search, third_search) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       (username, chat_id, 0, 0, 0, 'Не задан', 'Нет вип', 'Нет вип'))

    conn.commit()
    conn.close()