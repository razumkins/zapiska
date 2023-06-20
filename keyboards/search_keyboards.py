from main import types
from keyboards.other_keyboards import back_to_main_menu_button


search_keyboard = types.InlineKeyboardMarkup()
make_request_button = types.InlineKeyboardButton(text='🌐 Сделать/Заменить запрос', callback_data='make_request_button')
search_keyboard.row(make_request_button)
search_keyboard.row(back_to_main_menu_button)

choose_number_request_without_vip_keyboard = types.InlineKeyboardMarkup()
choose_number_request_with_vip_keyboard = types.InlineKeyboardMarkup()
first_request_button = types.InlineKeyboardButton(text='Запрос #1', callback_data='first_request_button')
second_request_button = types.InlineKeyboardButton(text='Запрос #2', callback_data='second_request_button')
third_request_button = types.InlineKeyboardButton(text='Запрос #3', callback_data='third_request_button')
choose_number_request_with_vip_keyboard.row(first_request_button)
choose_number_request_with_vip_keyboard.row(second_request_button)
choose_number_request_with_vip_keyboard.row(third_request_button)
choose_number_request_without_vip_keyboard.row(first_request_button)

first_request_sending_time_keyboard = types.InlineKeyboardMarkup()
first_request_three_times_day_button = types.InlineKeyboardButton(text='Выбрать время отправки', callback_data='first_request_three_times_day_button')
first_request_sending_time_keyboard.row(first_request_three_times_day_button)

second_request_sending_time_keyboard = types.InlineKeyboardMarkup()
second_request_three_times_day_button = types.InlineKeyboardButton(text='Выбрать время отправки', callback_data='second_request_three_times_day_button')
second_request_sending_time_keyboard.row(second_request_three_times_day_button)

third_request_sending_time_keyboard = types.InlineKeyboardMarkup()
third_request_three_times_day_button = types.InlineKeyboardButton(text='Выбрать время отправки', callback_data='third_request_three_times_day_button')
third_request_sending_time_keyboard.row(third_request_three_times_day_button)