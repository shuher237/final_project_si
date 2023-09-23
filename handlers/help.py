from states import QUESTION_STATE
from dotenv import load_dotenv
from telegram import (
    Update,
)
from telegram.ext import (
    ContextTypes,
)

""" (
    QUESTION_STATE,
) = range(1)
 """


async def help(update: Update, context: ContextTypes) -> None:
    """Shows the help menu."""

    help_text = (
        "/start - запустить бота\n"
        + "/help - показать все доступные команды\n"
        + "/cancel - остановить диалог с ботом\n"
    )

    await update.message.reply_text(help_text, disable_web_page_preview=True)

    return QUESTION_STATE