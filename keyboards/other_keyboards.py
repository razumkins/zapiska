from main import types


back_to_main_menu_button = types.InlineKeyboardButton(text='◀️ Вернуться в меню', callback_data='back_to_main_menu_button')
back_to_main_menu_keyboard = types.InlineKeyboardMarkup().add(back_to_main_menu_button)
