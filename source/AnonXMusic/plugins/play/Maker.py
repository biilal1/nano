import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(filters.command(["مصنع","ماركت","المصنع"], ""))
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/2514530559cc173845e3f.jpg",
        caption=f"""[⭑ٖٖᵂᴱᴸᶜᴼᴹᴱ ᵀᴼ ˢᴼᵁᴿᶜᴱ ˢᴱᶻᴬᴿ](https://t.me/UIU_II) 

♡♕ هاا هالو عزيزي : \n│ \n└ʙʏ: {message.from_user.mention()}**
♡♕ اختار ما تشاء من أقسام ســــيزر المختلفه
♡♕ من مصانع..ســــيزر مختلفه..و بمميزاتها""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗘𝗭𝗔𝗥⚡️", url=f"https://t.me/UIU_II"),
                   ],
                   [
                    InlineKeyboardButton(
                       "⋆ٰصانع الميوزك", url=f"https://t.me/sezarmusic_bot"),
                   ],
                   [     
                    InlineKeyboardButton(
                        "⋆ٰصانع الحمايه", url=f"https://t.me/Sezarfac2_bot"),    
                   InlineKeyboardButton(
                        "◁", callback_data="close"),
               ],
          ]
        ),
    )