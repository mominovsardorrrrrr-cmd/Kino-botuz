import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from config import TOKEN, CHANNELS

bot = Bot(TOKEN)
dp = Dispatcher()

async def check_sub(user_id):
    for channel in CHANNELS:
        try:
            member = await bot.get_chat_member(channel, user_id)
            if member.status == "left":
                return False
        except:
            return False
    return True

@dp.message(CommandStart())
async def start(message: types.Message):
    if not await check_sub(message.from_user.id):
        text = "❗ Botdan foydalanish uchun kanalga obuna bo‘ling:\n"
        for ch in CHANNELS:
            text += f"👉 {ch}\n"
        await message.answer(text)
        return

    await message.answer("🎬 Kino yoki serial nomini yozing")

@dp.message()
async def search(message: types.Message):
    await message.answer("🔍 Topildi:\nhttps://t.me/your_channel/1")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
