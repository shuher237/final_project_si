import os

from handlers.answer import answer
from handlers.start import start
from handlers.help import help
from handlers.cancel import cancel

from utils.states import QUESTION_STATE
from utils.logging import get_logger

from dotenv import load_dotenv

from telegram.ext import (
    Application,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)


def main() -> None:
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
    get_logger(__name__).info("Bot is running...")
    application.run_polling()


if __name__ == "__main__":
    main()
