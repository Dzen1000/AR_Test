import telegram
from telegram.ext import Updater, MessageHandler, Filters

# Замените YOUR_API_KEY на ваш API ключ Telegram
bot = telegram.Bot(token='6177671379:AAGAm4fY-NOqEZUQc2mzFSTtxuP0d88AlNI')


def handle_message(update, context):
    # Получаем текст сообщения
    text = update.message.text
    # Отвечаем на приветствия
    if text.lower() in ['привет', 'здравствуйте', ]:
        update.message.reply_text('Здравствуйте!')


def main():
    # Создаем Updater и регистрируем обработчик сообщений
    updater = Updater(
        token='6177671379:AAGAm4fY-NOqEZUQc2mzFSTtxuP0d88AlNI', use_context=True)
    updater.dispatcher.add_handler(
        MessageHandler(Filters.text, handle_message))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
