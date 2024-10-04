from aiogram import Bot
from aiogram.types import Message


async def get_user_info(msg: Message, bot: Bot):
    user = await bot.get_chat(msg.from_user.id)
    user_photos = await msg.from_user.get_profile_photos()

    matn = (
        f"{msg.from_user.mention_html('USER')} INFO:\n\n"
        f"Ism-familiya: {msg.from_user.full_name}\n"
        f"ID: {msg.from_user.id}\n"
    )

    if user.bio: matn += f"Tarjimai holi: {user.bio}\n"
    if msg.from_user.username: matn += f"Username: @{msg.from_user.username}\n"
    if user_photos.photos:
        await msg.answer_photo(user_photos.photos[0][0].file_id, caption=matn)
    else:
        await msg.answer(matn)


async def startup_answer(bot: Bot):
    await bot.send_message(6318392141, "Bot ishga tushdi ✅")


async def shutdown_answer(bot: Bot):
    await bot.send_message(6318392141, 'Bot ishdan to\'xtadi ❌')

