# main.py
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from config import API_TOKEN
from handlers import bulk_share, channel, users, automation, logs, security, advanced

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Registering handlers
dp.register_message_handler(bulk_share.handle_bulk_share, commands=['bulk_share'])
dp.register_message_handler(channel.handle_channel_subscription, commands=['channel_subscribe'])
dp.register_message_handler(users.handle_user_list, commands=['user_list'])
dp.register_message_handler(automation.handle_auto_posting, commands=['auto_posting'])
dp.register_message_handler(logs.handle_logs, commands=['logs'])
dp.register_message_handler(security.handle_security, commands=['security'])
dp.register_message_handler(advanced.handle_advanced_features, commands=['advanced'])

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
