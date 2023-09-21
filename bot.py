import logging
import os
import json
import requests
import time

from copilot import Copilot
from dotenv import load_dotenv
from telegram import (
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    Update,
    KeyboardButton,
)
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


(ENTRY_STATE, QUESTION_STATE,) = range(2)


def _generate_copilot(prompt: str):
    """Gets answer from copilot"""
    
    copilot = Copilot()
    c = copilot.get_answer(prompt)

    return c


#Starting the bot
async def start(update: Update, context: ContextTypes):
    """Start the conversation and ask user for an option."""

    # button = [[KeyboardButton(text="Question-Answering")]]
    # reply_markup = ReplyKeyboardMarkup(
    #     button, resize_keyboard=True
    # )

    # await update.message.reply_text(
    #     "Choose an option: 👇🏻",
    #     reply_markup=reply_markup,
    # )

    await update.message.reply_text(
        "Welcome to the club, body!!!",
    )

    return QUESTION_STATE


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    await update.message.reply_text(
        "Bye! I hope we can talk again some day.", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


# #Handling the question
# async def pre_query_handler(update: Update, context: ContextTypes):
#     """Ask the user for a query."""

#     button = [[KeyboardButton(text="Back")]]
#     reply_markup = ReplyKeyboardMarkup(
#         button, resize_keyboard=True
#     )

#     await update.message.reply_text(
#         "Enter your text: 👇🏻",
#         reply_markup=reply_markup,
#     )

#     return QUESTION_STATE


#Handling the answer
async def pre_query_answer_handler(update: Update, context: ContextTypes):
    """Display the answer to the user."""

    # button = [[KeyboardButton(text="Back")]]
    # reply_markup = ReplyKeyboardMarkup(
    #     button, resize_keyboard=True
    # )

    question = update.message.text

    answer = _generate_copilot(question)
    context.user_data['answer'] = answer

    await update.message.reply_text(
        answer, 
        # reply_markup=reply_markup,
    )

    return QUESTION_STATE


if __name__ == '__main__':
    load_dotenv()

    application = (Application.builder().token(os.getenv("BOT_TOKEN"))
                    .read_timeout(100).get_updates_read_timeout(100).build()
    )

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            ENTRY_STATE: [
                # MessageHandler(filters.Regex('^Back$'), start),
                # MessageHandler(filters.Regex('^Question-Answering$'),
                #                 pre_query_handler),
            ],
            QUESTION_STATE: [
                CommandHandler('cancel', cancel),
                MessageHandler(filters.TEXT, pre_query_answer_handler),
            ],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    
    application.add_handler(conv_handler)
    print("Bot is running ...")
    application.run_polling()
