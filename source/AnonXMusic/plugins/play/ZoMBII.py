import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
from random import  choice, randint


                
@app.on_message(filters.command(["مطورين سيزر","المطورين","مطورين"], ""))
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/2514530559cc173845e3f.jpg",
        caption=f"""**⋖━━❲𖣂❳━━●○𝚂𝙴𝚉𝙰𝚁○●━━❲𖣂❳━━⋗**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين سيزر ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⋖━━❲𖣂❳━━●○𝚂𝙴𝚉𝙰𝚁○●━━❲𖣂❳━━⋗**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⧛ َ𝗝َ َ𝗢َ ٍ𝗞َ ׀ مــ ـٰٖمـوِٰلٰ ׀ جـِوڪَ ׀ ⧚", url=f"https://t.me/G_O_OZ"), 
                 ],[
                    InlineKeyboardButton(
                        "زيـــــــٌن اݪــتأࢪيخ 🚸", url=f"https://t.me/p_m_4"),
                ],[
                    InlineKeyboardButton(
                        "《 ⎖᳒𝘿𝙀𝙑⌯⤹𝗭𝗢𝗠𝗕𝗜𝗘⤸‹༄►》", url=f"https://t.me/Zo_Mbi_e"),
                ],

            ]

        ),

    )

