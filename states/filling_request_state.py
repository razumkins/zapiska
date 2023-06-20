import asyncio
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from keyboards.search_keyboards import *
from keyboards.main_menu_keyboards import main_menu_keyboard, main_menu__without_trial_vip_keyboard
import sqlite3
from main import dp, types, bot


class FillingRequest(StatesGroup):
    get_first_request = State()
    get_second_request = State()
    get_third_request = State()


@dp.message_handler(state=FillingRequest.get_first_request)
async def get_request_handler(message: types.Message, state: FSMContext):
    request = message.text
    data = await state.get_data()
    get_request_message_id = data.get('get_request_message_id')
    if request == '/cancel':
        await state.reset_state()
        edit_message = await message.answer('Отменяем...')
        edit_message_id = edit_message.message_id
        await asyncio.sleep(2)
        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
        await bot.delete_message(chat_id=message.from_user.id, message_id=get_request_message_id)

        conn = sqlite3.connect('database/db')
        cursor = conn.cursor()

        check_trial_vip = \
        cursor.execute("SELECT trial_vip FROM users WHERE chat_id = ?", (message.from_user.id,)).fetchone()[-1]
        if check_trial_vip == 0:
            await bot.edit_message_text(chat_id=message.from_user.id, message_id=edit_message_id, text='Главное меню: ', reply_markup=main_menu_keyboard)
        else:
            await bot.edit_message_text(chat_id=message.from_user.id, message_id=edit_message_id, text='Главное меню: ', reply_markup=main_menu__without_trial_vip_keyboard)

        conn.commit()
        conn.close()
    else:
        conn = sqlite3.connect('database/db')
        cursor = conn.cursor()

        cursor.execute("UPDATE users SET search = ? WHERE chat_id = ?", (request, message.from_user.id, ))

        await message.answer(f'Вы записали ваш запрос в #1 ячейку, выберите время получения сообщений по запросу.', reply_markup=first_request_sending_time_keyboard)
        await state.finish()

        conn.commit()
        conn.close()


@dp.message_handler(state=FillingRequest.get_second_request)
async def get_request_handler(message: types.Message, state: FSMContext):
    request = message.text
    data = await state.get_data()
    get_request_message_id = data.get('get_request_message_id')
    if request == '/cancel':
        await state.reset_state()
        edit_message = await message.answer('Отменяем...')
        edit_message_id = edit_message.message_id
        await asyncio.sleep(2)
        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
        await bot.delete_message(chat_id=message.from_user.id, message_id=get_request_message_id)

        conn = sqlite3.connect('database/db')
        cursor = conn.cursor()

        check_trial_vip = \
            cursor.execute("SELECT trial_vip FROM users WHERE chat_id = ?", (message.from_user.id,)).fetchone()[-1]
        if check_trial_vip == 0:
            await bot.edit_message_text(chat_id=message.from_user.id, message_id=edit_message_id, text='Главное меню: ',
                                        reply_markup=main_menu_keyboard)
        else:
            await bot.edit_message_text(chat_id=message.from_user.id, message_id=edit_message_id, text='Главное меню: ',
                                        reply_markup=main_menu__without_trial_vip_keyboard)

        conn.commit()
        conn.close()
    else:
        conn = sqlite3.connect('database/db')
        cursor = conn.cursor()

        cursor.execute("UPDATE users SET second_search = ? WHERE chat_id = ?", (request, message.from_user.id,))

        await message.answer(f'Вы записали ваш запрос в #2 ячейку, выберите время получения сообщений по запросу.',
                             reply_markup=second_request_sending_time_keyboard)
        await state.finish()

        conn.commit()
        conn.close()


@dp.message_handler(state=FillingRequest.get_third_request)
async def get_request_handler(message: types.Message, state: FSMContext):
    request = message.text
    data = await state.get_data()
    get_request_message_id = data.get('get_request_message_id')
    if request == '/cancel':
        await state.reset_state()
        edit_message = await message.answer('Отменяем...')
        edit_message_id = edit_message.message_id
        await asyncio.sleep(2)
        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
        await bot.delete_message(chat_id=message.from_user.id, message_id=get_request_message_id)

        conn = sqlite3.connect('database/db')
        cursor = conn.cursor()

        check_trial_vip = \
            cursor.execute("SELECT trial_vip FROM users WHERE chat_id = ?", (message.from_user.id,)).fetchone()[-1]
        if check_trial_vip == 0:
            await bot.edit_message_text(chat_id=message.from_user.id, message_id=edit_message_id, text='Главное меню: ',
                                        reply_markup=main_menu_keyboard)
        else:
            await bot.edit_message_text(chat_id=message.from_user.id, message_id=edit_message_id, text='Главное меню: ',
                                        reply_markup=main_menu__without_trial_vip_keyboard)

        conn.commit()
        conn.close()
    else:
        conn = sqlite3.connect('database/db')
        cursor = conn.cursor()

        cursor.execute("UPDATE users SET third_search = ? WHERE chat_id = ?", (request, message.from_user.id,))

        await message.answer(f'Вы записали ваш запрос в #3 ячейку, выберите время получения сообщений по запросу.',
                             reply_markup=third_request_sending_time_keyboard)
        await state.finish()

        conn.commit()
        conn.close()