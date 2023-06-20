from aiogram.utils import executor
from database.database import *
from handlers.my_requests_handler import *
from handlers.about_me_handler import *
from handlers.main_menu_handler import *
from handlers.choose_number_request_handler import *
from handlers.get_trial_vip_status_handler import *
from handlers.other_handlers import *
from handlers.search_handler import *
from states.filling_request_state import *
from handlers.sending_time_handler import *
from main import dp


async def on_startup(_):
    print('Бот успешно запущен.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)