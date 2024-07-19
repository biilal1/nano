import asyncio
from pyrogram import Client, filters
from AnonXMusic.core.userbot import assistants
from AnonXMusic.utils.database import (
    get_active_chats,
    get_authuser_names,
    get_client,
    get_served_chats,
    get_served_users,
)

from AnonXMusic import app

@app.on_message(filters.command("انضم", ""))
async def tom_join(client, message):
    tom_chat_user = message.chat.id
    tom_info = await app.get_chat(tom_chat_user)
    if tom_info.invite_link:
        tom_link = tom_info.invite_link
    else:
        await message.reply("لا يمكن العثور على رابط الدعوة لهذه المجموعة/القناة.")
        return
    
    for ahmed in assistants:
        tom_c = await get_client(ahmed)
        try:
            await tom_c.join_chat(str(tom_link))
            await message.reply("تم انضمام الحساب المساعد بنجاح")
        except Exception as e:
            await message.reply(f"حدث خطأ أثناء الانضمام: {str(e)}")


