from aiogram.utils import executor
from states.filling_request_state import *
from main import dp, types, bot
import schedule
import sqlite3
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from googlesearch import search
from datetime import datetime


class GetSendingTime(StatesGroup):
    first_sending_time = State()
    second_sending_time = State()
    third_sending_time = State()


@dp.callback_query_handler(text='first_request_three_times_day_button')
async def first_request_three_times_day_button_handler(callback_query: types.CallbackQuery):
    await callback_query.bot.edit_message_text(
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id,
        text='Напишите время, в которое вы хотели бы получать новости. (до 3 вариаций, допустим, (14:30, 13:50, -), - означает, что 3 вариации не будет)'
    )

    await GetSendingTime.first_sending_time.set()


@dp.message_handler(state=GetSendingTime.first_sending_time)
async def first_sending_time_handler(message: types.Message, state: FSMContext):
    times = message.text
    values = times.split(', ')

    if len(values) >= 1 and values[0] != '-':
        try:
            first_time = datetime.strptime(values[0].split()[0], '%H:%M').time()
        except:
            await message.answer('Вы неправильно ввели время, повторите снова. (часы:минуты, часы:минуты, часы:минуты; если хочет меньше 3 вариаций ставьте -')
            await state.reset_state()
            await GetSendingTime.first_sending_time.set()
            return
    else:
        first_time = None

    if len(values) >= 2 and values[1] != '-':
        try:
            second_time = datetime.strptime(values[1].split()[0], '%H:%M').time()
        except:
            await message.answer(
                'Вы неправильно ввели время, повторите снова. (часы:минуты, часы:минуты, часы:минуты; если хочет меньше 3 вариаций ставьте -')
            await state.reset_state()
            await GetSendingTime.first_sending_time.set()
            return
    else:
        second_time = None

    if len(values) >= 3 and values[2] != '-':
        try:
            third_time = datetime.strptime(values[2].split()[0], '%H:%M').time()
        except:
            await message.answer(
                'Вы неправильно ввели время, повторите снова. (часы:минуты, часы:минуты, часы:минуты; если хочет меньше 3 вариаций ставьте -')
            await state.reset_state()
            await GetSendingTime.first_sending_time.set()
            return

    else:
        third_time = None
    await message.answer('Ваше время добавлено.')
    await state.finish()

    scheduler = AsyncIOScheduler()

    async def execute_code(chat_id):
        conn = sqlite3.connect('database/db')
        cursor = conn.cursor()
        request = cursor.execute("SELECT search FROM users WHERE chat_id = ?", (chat_id,)).fetchone()[-1]
        search_results = search(request, num_results=100, lang='ru')
        existing_websites = cursor.execute("SELECT website FROM websites WHERE chat_id = ?",
                                           (message.from_user.id,)).fetchall()
        existing_websites = set(website[0] for website in existing_websites)

        response = ''
        count = 0
        id = 1
        for idx, result in enumerate(search_results, start=1):
            print(count)
            if count >= 10:
                break

            if result not in existing_websites:
                response += f"Сайт #{id}: {result}\n"
                cursor.execute("INSERT INTO websites (chat_id, website) VALUES (?,?)",
                               (message.from_user.id, result,))
                conn.commit()
                count += 1
                id += 1

        await message.answer(response)

    if first_time is not None:
        scheduler.add_job(execute_code, 'cron', hour=first_time.hour, minute=first_time.minute, day_of_week='*',
                          args=[message.chat.id])

    if second_time is not None:
        scheduler.add_job(execute_code, 'cron', hour=second_time.hour, minute=second_time.minute, day_of_week='*',
                          args=[message.chat.id])

    if third_time is not None:
        scheduler.add_job(execute_code, 'cron', hour=third_time.hour, minute=third_time.minute, day_of_week='*',
                          args=[message.chat.id])

    scheduler.start()


@dp.callback_query_handler(text='second_request_three_times_day_button')
async def second_request_three_times_day_button_handler(callback_query: types.CallbackQuery):
    await callback_query.bot.edit_message_text(
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id,
        text='Напишите время, в которое вы хотели бы получать новости. (до 3 вариаций, допустим, (14:30, 13:50, -), - означает, что 3 вариации не будет)'
    )

    await GetSendingTime.second_sending_time.set()


@dp.message_handler(state=GetSendingTime.second_sending_time)
async def second_sending_time_handler(message: types.Message, state: FSMContext):
    times = message.text
    await message.answer('Ваше время было добавлено.')
    values = times.split(', ')

    if len(values) >= 1 and values[0] != '-':
        try:
            first_time = datetime.strptime(values[0].split()[0], '%H:%M').time()
        except:
            await message.answer(
                'Вы неправильно ввели время, повторите снова. (часы:минуты, часы:минуты, часы:минуты; если хочет меньше 3 вариаций ставьте -')
            await state.reset_state()
            await GetSendingTime.first_sending_time.set()
            return
    else:
        first_time = None

    if len(values) >= 2 and values[1] != '-':
        try:
            second_time = datetime.strptime(values[1].split()[0], '%H:%M').time()
        except:
            await message.answer(
                'Вы неправильно ввели время, повторите снова. (часы:минуты, часы:минуты, часы:минуты; если хочет меньше 3 вариаций ставьте -')
            await state.reset_state()
            await GetSendingTime.first_sending_time.set()
            return
    else:
        second_time = None

    if len(values) >= 3 and values[2] != '-':
        try:
            third_time = datetime.strptime(values[2].split()[0], '%H:%M').time()
        except:
            await message.answer(
                'Вы неправильно ввели время, повторите снова. (часы:минуты, часы:минуты, часы:минуты; если хочет меньше 3 вариаций ставьте -')
            await state.reset_state()
            await GetSendingTime.first_sending_time.set()
            return

    else:
        third_time = None
    await message.answer('Ваше время добавлено.')
    await state.finish()

    scheduler = AsyncIOScheduler()

    async def execute_code(chat_id):
        conn = sqlite3.connect('database/db')
        cursor = conn.cursor()
        request = cursor.execute("SELECT second_search FROM users WHERE chat_id = ?", (chat_id,)).fetchone()[-1]
        search_results = search(request, num_results=100, lang='ru')
        existing_websites = cursor.execute("SELECT website FROM websites WHERE chat_id = ?",
                                           (message.from_user.id,)).fetchall()
        existing_websites = set(website[0] for website in existing_websites)

        response = ''
        count = 0
        id = 1
        for idx, result in enumerate(search_results, start=1):
            print(count)
            if count >= 10:
                break

            if result not in existing_websites:
                response += f"Сайт #{id}: {result}\n"
                cursor.execute("INSERT INTO websites (chat_id, website) VALUES (?,?)",
                               (message.from_user.id, result,))
                conn.commit()
                count += 1
                id += 1

        await message.answer(response)

    if first_time is not None:
        scheduler.add_job(execute_code, 'cron', hour=first_time.hour, minute=first_time.minute, day_of_week='*',
                          args=[message.chat.id])

    if second_time is not None:
        scheduler.add_job(execute_code, 'cron', hour=second_time.hour, minute=second_time.minute, day_of_week='*',
                          args=[message.chat.id])

    if third_time is not None:
        scheduler.add_job(execute_code, 'cron', hour=third_time.hour, minute=third_time.minute, day_of_week='*',
                          args=[message.chat.id])

    scheduler.start()


@dp.callback_query_handler(text='third_request_three_times_day_button')
async def third_request_three_times_day_button_handler(callback_query: types.CallbackQuery):
    await callback_query.bot.edit_message_text(
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id,
        text='Напишите время, в которое вы хотели бы получать новости. (до 3 вариаций, допустим, (14:30, 13:50, -), - означает, что 3 вариации не будет)'
    )

    await GetSendingTime.third_sending_time.set()


@dp.message_handler(state=GetSendingTime.third_sending_time)
async def third_sending_time_handler(message: types.Message, state: FSMContext):
    times = message.text
    await message.answer('Ваше время было добавлено.')
    values = times.split(', ')

    if len(values) >= 1 and values[0] != '-':
        try:
            first_time = datetime.strptime(values[0].split()[0], '%H:%M').time()
        except:
            await message.answer(
                'Вы неправильно ввели время, повторите снова. (часы:минуты, часы:минуты, часы:минуты; если хочет меньше 3 вариаций ставьте -')
            await state.reset_state()
            await GetSendingTime.first_sending_time.set()
            return
    else:
        first_time = None

    if len(values) >= 2 and values[1] != '-':
        try:
            second_time = datetime.strptime(values[1].split()[0], '%H:%M').time()
        except:
            await message.answer(
                'Вы неправильно ввели время, повторите снова. (часы:минуты, часы:минуты, часы:минуты; если хочет меньше 3 вариаций ставьте -')
            await state.reset_state()
            await GetSendingTime.first_sending_time.set()
            return
    else:
        second_time = None

    if len(values) >= 3 and values[2] != '-':
        try:
            third_time = datetime.strptime(values[2].split()[0], '%H:%M').time()
        except:
            await message.answer(
                'Вы неправильно ввели время, повторите снова. (часы:минуты, часы:минуты, часы:минуты; если хочет меньше 3 вариаций ставьте -')
            await state.reset_state()
            await GetSendingTime.first_sending_time.set()
            return

    else:
        third_time = None
    await message.answer('Ваше время добавлено.')
    await state.finish()

    scheduler = AsyncIOScheduler()

    async def execute_code(chat_id):
        conn = sqlite3.connect('database/db')
        cursor = conn.cursor()
        request = cursor.execute("SELECT third_search FROM users WHERE chat_id = ?", (chat_id,)).fetchone()[-1]
        search_results = search(request, num_results=100, lang='ru')
        existing_websites = cursor.execute("SELECT website FROM websites WHERE chat_id = ?",
                                           (message.from_user.id,)).fetchall()
        existing_websites = set(website[0] for website in existing_websites)

        response = ''
        count = 0
        id = 1
        for idx, result in enumerate(search_results, start=1):
            if count >= 10:
                break

            if result not in existing_websites:
                response += f"Сайт #{id}: {result}\n"
                cursor.execute("INSERT INTO websites (chat_id, website) VALUES (?,?)",
                               (message.from_user.id, result,))
                conn.commit()
                count += 1
                id += 1

        await message.answer(response)

    if first_time is not None:
        scheduler.add_job(execute_code, 'cron', hour=first_time.hour, minute=first_time.minute, day_of_week='*',
                          args=[message.chat.id])

    if second_time is not None:
        scheduler.add_job(execute_code, 'cron', hour=second_time.hour, minute=second_time.minute, day_of_week='*',
                          args=[message.chat.id])

    if third_time is not None:
        scheduler.add_job(execute_code, 'cron', hour=third_time.hour, minute=third_time.minute, day_of_week='*',
                          args=[message.chat.id])

    scheduler.start()