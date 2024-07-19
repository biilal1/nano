import asyncio
from pyrogram import Client, filters
from AnonXMusic import app
import random
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMembersFilter
from pyrogram import enums


TOm = []

@app.on_message(filters.command(["قفل الايدي", "تعطيل الايدي"], ""))
def iddlock(client, message):
    chat_id = message.chat.id
    tom_id = message.from_user.id
    tooom = client.get_chat_members(chat_id, filter=ChatMembersFilter.ADMINISTRATORS)
    for tom in tooom:
        if tom.user.id == tom_id and (tom.status == enums.ChatMemberStatus.OWNER or tom.status == enums.ChatMemberStatus.ADMINISTRATOR):
            if message.chat.id in TOm:
                return message.reply_text("تم معطل من قبل🔒")
            TOm.append(message.chat.id)
            return message.reply_text("تم تعطيل الايدي بنجاح ✅🔒")
    return message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")

@app.on_message(filters.command(["فتح الايدي", "تفعيل الايدي"], ""))
def iddopen(client, message):
    chat_id = message.chat.id
    tom_id = message.from_user.id
    tooom = client.get_chat_members(chat_id, filter=ChatMembersFilter.ADMINISTRATORS)
    for tom in tooom:
        if tom.user.id == tom_id and (tom.status == enums.ChatMemberStatus.OWNER or tom.status == enums.ChatMemberStatus.ADMINISTRATOR):
            if not message.chat.id in TOm:
                return message.reply_text("الايدي مفعل من قبل ✅")
            TOm.remove(message.chat.id)
            return message.reply_text("تم فتح الايدي بنجاح ✅🔓")
    return message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")




@app.on_message(filters.command(["ايدي","الايدي","ا"], ""))
async def iddd(client, message):
    if message.chat.id in TOm:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"""☠️ ¦𝙽𝙰𝙼𝙴 :{message.from_user.mention}\n🥰 ¦𝚄𝚂𝙴𝚁 :@{message.from_user.username}\n😍 ¦𝙸𝙳 :`{message.from_user.id}`\n💕 ¦𝙱𝙸𝙾 :{usr.bio}\n❤ ¦𝙲𝙷𝙰𝚃: {message.chat.title}\n😎 ¦𝙸𝙳.𝙲𝙷𝙰𝚃 :`{message.chat.id}`""", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )







ahmed_tom = []
@app.on_message(filters.command(["قفل جمالي","تعطيل جمالي"], ""))
def lllock(client, message):
    chat_id = message.chat.id
    tom_id = message.from_user.id
    tooom = client.get_chat_members(chat_id, filter=ChatMembersFilter.ADMINISTRATORS)
    for tom in tooom:
        if tom.user.id == tom_id and (tom.status == enums.ChatMemberStatus.OWNER or tom.status == enums.ChatMemberStatus.ADMINISTRATOR):
            if message.chat.id in ahmed_tom:
                return message.reply_text("جمالي معطل من قبل✅")
            ahmed_tom.append(message.chat.id)
            return message.reply_text(" تم تعطيل جمالي بنجاح✅🔒")
    return message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")



@app.on_message(filters.command(["فتح جمالي","تفعيل جمالي"], ""))
def idljjopen(client, message):
    chat_id = message.chat.id
    tom_id = message.from_user.id
    tooom = client.get_chat_members(chat_id, filter=ChatMembersFilter.ADMINISTRATORS)
    for tom in tooom:
        if tom.user.id == tom_id and (tom.status == enums.ChatMemberStatus.OWNER or tom.status == enums.ChatMemberStatus.ADMINISTRATOR):
            if not message.chat.id in ahmed_tom:
                return message.reply_text("جمالي مفعل من قبل✅")
            ahmed_tom.remove(message.chat.id)
            return message.reply_text("تم فتح جمالي بنجاح ✅🔓")
    return message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")






@app.on_message(filters.command(["جمالي"], ""))
async def idjjdd(client, message):
    if message.chat.id in ahmed_tom:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    i = ["0","10", "15","20", "25","30","35", "40","45", "50","55", "60"," 66", "70","77", "80","85", "90","99", "100","1000" ]
    ik = random.choice(i)
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"نسبه جمالك يا مز انت \n│ \n└ʙʏ: {ik} %😂❤️", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )
       

