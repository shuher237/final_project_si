import pytest

from unittest.mock import AsyncMock

from bot import start


@pytest.mark.asyncio
async def test_start():
    """Test case for /start command."""
    
    # Создаем макеты объектов Update и Context
    update = AsyncMock()
    context = AsyncMock()

    await start(update, context)

    # Проверить, что бот отправил ожидаемое сообщение
    update.message.reply_text.assert_called_with(
        f"Hello, {update.message.from_user.first_name}! Ask me any question"
    )
