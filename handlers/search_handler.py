from handlers.main_menu_handler import *
from keyboards.main_menu_keyboards import *
from states.filling_request_state import *
from handlers.choose_number_request_handler import *
from keyboards.search_keyboards import *
import sqlite3
from googlesearch import *


@dp.callback_query_handler(text='search_button')
async def search_button_handler(callback_query: types.CallbackQuery):
    await callback_query.bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text='Небольшая инструкция:\n\nЕсли хотите сделать или заменить запрос - нажмите кнопочку Сделать/Заменить запрос.\nЕсли хотите вернуться в меню - нажмите кнопочку назад.',
                                          reply_markup=search_keyboard)


@dp.callback_query_handler(text='make_request_button')
async def make_request_button_handler(callback_query: types.CallbackQuery):
    conn = sqlite3.connect('database/db')
    cursor = conn.cursor()

    check_trial_vip = cursor.execute("SELECT vip FROM users WHERE chat_id = ?", (callback_query.from_user.id, )).fetchone()[-1]
    if check_trial_vip == 0:
        await callback_query.bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text='Выберите ячейку!\n\nПосле нажатия на ячейку отменить заполнение ячейки Вы сможете командой /cancel.', reply_markup=choose_number_request_without_vip_keyboard)
    else:
        await callback_query.bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text='Выберите ячейку!\n\nПосле нажатия на ячейку отменить заполнение ячейки Вы сможете командой /cancel.', reply_markup=choose_number_request_with_vip_keyboard)


@dp.callback_query_handler(text='first_request_button')
async def first_request_button_handler(callback_query: types.CallbackQuery, state: FSMContext):
    get_request_message = await callback_query.bot.edit_message_text(chat_id=callback_query.from_user.id,
                                               message_id=callback_query.message.message_id,
                                               text='Введите запрос: ')
    get_request_message_id = get_request_message.message_id
    number_request = 1
    await state.update_data(get_request_message_id=get_request_message_id)
    await state.update_data(number_request=number_request)
    await FillingRequest.get_first_request.set()


@dp.callback_query_handler(text='second_request_button')
async def second_request_button_handler(callback_query: types.CallbackQuery, state: FSMContext):
    get_request_message = await callback_query.bot.edit_message_text(chat_id=callback_query.from_user.id,
                                                                     message_id=callback_query.message.message_id,
                                                                     text='Введите запрос: ')
    get_request_message_id = get_request_message.message_id
    number_request = 2
    await state.update_data(get_request_message_id=get_request_message_id)
    await state.update_data(number_request=number_request)
    await FillingRequest.get_second_request.set()


@dp.callback_query_handler(text='third_request_button')
async def second_request_button_handler(callback_query: types.CallbackQuery, state: FSMContext):
    get_request_message = await callback_query.bot.edit_message_text(chat_id=callback_query.from_user.id,
                                                                     message_id=callback_query.message.message_id,
                                                                     text='Введите запрос: ')
    get_request_message_id = get_request_message.message_id
    number_request = 3
    await state.update_data(get_request_message_id=get_request_message_id)
    await state.update_data(number_request=number_request)
    await FillingRequest.get_third_request.set()