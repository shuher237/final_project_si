from utils.states import QUESTION_STATE

from api.chatgpt import ChatGPT

from telegram import (
    Update,
)
from telegram.ext import (
    ContextTypes,
)


def _generate_chatgpt(prompt: str) -> str:
    """Gets answer from ChatGPT"""

    chatgpt = ChatGPT()
    c = chatgpt.get_answer(prompt)

    return c


async def answer(update: Update, context: ContextTypes) -> int:
    """Display the answer to the user."""

    question = update.message.text

    answer = _generate_chatgpt(question)
    context.user_data["answer"] = answer

    await update.message.reply_text(
        answer,
    )

    return QUESTION_STATE
