from utils.states import QUESTION_STATE
from utils.texts import help_text

from telegram import Update
from telegram.ext import ContextTypes


async def help(update: Update, context: ContextTypes) -> int:
    """Shows the help menu."""

    await update.message.reply_text(help_text, disable_web_page_preview=True)

    return QUESTION_STATE
