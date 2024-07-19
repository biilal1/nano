import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app




########################### بوت حذف
@app.on_message(filters.command(["بنلتمماا", "بتبتن", "نبنبمم"], ""))
async def svksksa(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/a6137caa707bdb1247d7c.jpg",
        caption=f"""[خش احذف محدش هيمسك فيك يلا غور فداهية 😂❤](https://t.me/LC6BOT)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• اضـغـط لـدخول للـبوت", url=f"https://t.me/d_accubot")
                ]
           ]
        ),
    )
   
   
 ########################### قول  
@app.on_message(filters.command(["قول", "كول"], ""))
def elko(client: Client, message: Message):
    tet = message.text.split(None, 1)[1]
    message.reply(tet) 
    
########################### رتيتي

@app.on_message(filters.command(["رتبتي"], ""))
def forward(client: Client, message: Message):
  chat_id = message.chat.id
  user_id = message.from_user.id
  rank = app.get_chat_member(chat_id, user_id)
  rank = rank.status
  if rank == "administrator":
   app.send_message(chat_id,"رتبتك هياا \n│ \n└ʙʏ  : مطور ف ام الخرا")
  elif rank == "creator":
   app.send_message(chat_id," رتبتك هياا \n│ \n└ʙʏ  : مطور اساسي")
  elif rank == "member":
   app.send_message(chat_id,"رتبتك هياا \n│ \n└ʙʏ  : عضو حقير ملكش لازمه😛")
  elif rank == "restricted":
   app.send_message(chat_id,"رتبتك هياا \n│ \n└ʙʏ  : متقيد")
  elif rank == "left":
   app.send_message(chat_id,"رتبتك هياا \n│ \n└ʙʏ  : مغادر")
  elif rank == "kicked":
   app.send_message(chat_id,"رتبتك هياا \n│ \n└ʙʏ  : محظور")
   



    
   
   
   
