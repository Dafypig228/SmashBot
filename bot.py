import random
from aiogram import Bot, Dispatcher
from aiogram.types import (
    InlineQuery, InlineQueryResultArticle, InputTextMessageContent,
    InlineKeyboardMarkup, InlineKeyboardButton
)
import asyncio

TOKEN = "8599227027:AAHcXPhxGvv_1LWVZj7M5EHNjN9_YwOQ8ZI"
BOT_USERNAME = "HowSmashBot"

SECRET_WORD = "mypass"  # твое секретное слово
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.inline_query()
async def inline(query: InlineQuery):
    text = query.query.strip()

    # Проверка: если текст не начинается с секретного слова — возвращаем пустой ответ
    if not text.startswith(SECRET_WORD):
        await query.answer([], cache_time=0)
        return

    try:
        number = int(text.split()[1])
    except (IndexError, ValueError):
        number = random.randint(1, 100)

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Share your smashness!",
                    switch_inline_query=""
                )
            ]
        ]
    )

    result = InlineQueryResultArticle(
        id="1",
        title="How smash are you?",
        description="Send your current smashness to this chat.",
        input_message_content=InputTextMessageContent(
            message_text=f"I am {number}% smash!"
        ),
        reply_markup=keyboard
    )

    await query.answer([result], cache_time=0)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
