from utils.states import QUESTION_STATE

from utils.messages import get_hello_msg

from dotenv import load_dotenv

from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes) -> int:
    """Start the conversation and ask user for an option."""

    await update.message.reply_text(
        get_hello_msg(update.message.from_user.first_name),
    )

    return QUESTION_STATE
