from utils.logging import get_logger

from telegram import (
    Update,
    ReplyKeyboardRemove,
)
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
)


async def cancel(update: Update, context: ContextTypes) -> int:
    """Cancels and ends the conversation."""

    user = update.message.from_user
    get_logger(__name__).info("User %s canceled the conversation.", user.first_name)

    await update.message.reply_text(
        "Был рад пообщаться! Заходи и спрашивай ещё!.",
        reply_markup=ReplyKeyboardRemove(),
    )

    return ConversationHandler.END
