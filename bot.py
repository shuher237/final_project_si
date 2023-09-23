from states import QUESTION_STATE
import logging
import os
import json
import requests
import time
import openai
from handlers.answer_handler import answer
from handlers.start import start
from handlers.help import help
from handlers.cancel import cancel

from dotenv import load_dotenv

from telegram.ext import (
    Application,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)

if __name__ == "__main__":
    load_dotenv()

    application = (
        Application.builder()
        .token(os.getenv("BOT_TOKEN"))
        .read_timeout(100)
        .get_updates_read_timeout(100)
        .build()
    )

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            QUESTION_STATE: [
                CommandHandler("help", help),
                CommandHandler("cancel", cancel),
                MessageHandler(filters.TEXT, answer),
            ],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)
    print("Bot is running ...")
    application.run_polling()
