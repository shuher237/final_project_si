from states import QUESTION_STATE
from dotenv import load_dotenv
from telegram import (
    Update,
)
from telegram.ext import (
    ContextTypes,
)


async def start(update: Update, context: ContextTypes):
    """Start the conversation and ask user for an option."""

    await update.message.reply_text(
        f"Привет, {update.message.from_user.first_name}! Задай мне какой-нибудь вопрос и я непременно помогу с ответом",
    )

    return QUESTION_STATE
