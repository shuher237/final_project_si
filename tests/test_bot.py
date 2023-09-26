import pytest

from utils.texts import get_hello_text

from unittest.mock import AsyncMock

from bot import start


@pytest.mark.asyncio
async def test_start():
    """Test case for /start command."""

    # Create mockup of objects Update and Context
    update = AsyncMock()
    context = AsyncMock()

    await start(update, context)

    # Check that the bot has sent the expected message
    update.message.reply_text.assert_called_with(
        get_hello_text(update.message.from_user.first_name)
    )
