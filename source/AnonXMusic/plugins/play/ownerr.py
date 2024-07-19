import asyncio
import os
import time
import requests
import aiohttp
import config
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app

import re
import sys
from os import getenv

from dotenv import load_dotenv

load_dotenv()

OWNER_ID = getenv("OWNER_ID")

OWNER = getenv("OWNER")


def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj



@app.on_message(filters.command(["جوك","يجوك","الجوك","مطور السورس","المبرمج"], ""))
async def yas(client, message):
    usr = await client.get_chat("G_O_OZ")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⋖━━❲𖣂❳━━●○𝚂𝙴𝚉𝙰𝚁○●━━❲𖣂❳━━⋗\n\n☠️ ¦caesar :{name}\n🥰 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n😎 ¦𝙸𝙳 :`{usr.id}`\n❤ ¦𝙱𝙸𝙾 :{usr.bio}\n\n**⋖━━❲𖣂❳━━●○𝚂𝙴𝚉𝙰𝚁○●━━❲𖣂❳━━⋗**",  
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )





@app.on_message(filters.command(["المطور", "《مطور البوت》"], ""))
async def khfzss(client: Client, message: Message):
    usrr = await client.get_chat(OWNER_ID)
    name = usrr.first_name
    bio = usrr.bio
    id = usrr.id
    username = usrr.username
    async for photo in client.get_chat_photos(OWNER_ID, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""- **⋖━━❲𖣂❳━━●○𝚂𝙴𝚉𝙰𝚁○●━━❲𖣂❳━━⋗** : \n\n⌔︙𝒏𝒂𝒎𝒆: {name} \n\n⌔︙𝒖𝒔𝒆𝒓: @{username} \n\n⌔︙𝒊𝒅: {id} \n\n⌔︙𝒃𝒊𝒐: {bio} \n\n⌔︙𝒋𝒐𝒃:  مطور البوت """, 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{username}")
                ],
            ]
        ),
    )                    
                    sender_id = message.from_user.id
                    sender_name = message.from_user.first_name
                    await app.send_message(OWNER_ID, f"الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name}")
                    return await app.send_message(config.LOG_GROUP_ID, f"الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name}")


@app.on_message(filters.command(["تحويل لصوره"], ""))
async def elkatifh(client: Client, message: Message):
    reply = message.reply_to_message
    if not reply:
        return await message.reply("الرد على ملصق.")
    if not reply.sticker:
        return await message.reply("الرد على ملصق.")
    m = await message.reply("يتم المعالجه..")
    f = await reply.download(f"{reply.sticker.file_unique_id}.png")
    await gather(*[message.reply_photo(f),message.reply_document(f)])
    await m.delete()
    os.remove(f)



