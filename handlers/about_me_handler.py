from handlers.main_menu_handler import *
from keyboards.main_menu_keyboards import *
from keyboards.other_keyboards import back_to_main_menu_button


@dp.callback_query_handler(text='about_me_button')
async def about_me_button_handler(callback_query: types.CallbackQuery):
    about_me_keyboard = types.InlineKeyboardMarkup().add(back_to_main_menu_button)
    await callback_query.bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="""Привет! Я бот, который будет раз в 24 часа отправлять новости, по твоему запросу. Я выдаю самую актуальную и свежую информацию.
А с VIP статусом, ты можешь получать новости до трёх раз в сутки, так что ты точно будешь знать все актуальные новости!""",
                                               reply_markup=about_me_keyboard)