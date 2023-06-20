from main import types

main_menu_keyboard = types.InlineKeyboardMarkup()
search_button = types.InlineKeyboardButton(text='🔎Поиск', callback_data='search_button')
my_requests_button = types.InlineKeyboardButton(text='📝Мои запросы', callback_data='my_requests_button')
get_trial_vip_status_button = types.InlineKeyboardButton(text='💎Получить пробный вип статус', callback_data='get_trial_vip_status_button')
about_me_button = types.InlineKeyboardButton(text='🙋‍♂️Обо мне', callback_data='about_me_button')
main_menu_keyboard.add(search_button, my_requests_button)
main_menu_keyboard.row(get_trial_vip_status_button)
main_menu_keyboard.row(about_me_button)

main_menu__without_trial_vip_keyboard = types.InlineKeyboardMarkup().add(search_button, my_requests_button)
main_menu__without_trial_vip_keyboard.row(about_me_button)