import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(filters.command(["زين", "《مطور السورس》"], ""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/2514530559cc173845e3f.jpg",
caption=f"""[زيـــــــٌن اݪــتأࢪيخ 🚸 الغلبان  مطور السورس ❤️‍🔥](https://t.me/p_m_4)يوزر زين @UIU_II ❤️‍🔥✨""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                    "●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧 ⟧⟝◉━●", url=f"https://t.me/UIU_II"
                ),
                ],
                [
                    InlineKeyboardButton(
                        "زيـــــــٌن اݪــتأࢪيخ 🚸", url=f"https://t.me/p_m_4"),
                ],
            ]
        ),
    )
