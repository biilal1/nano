from pyrogram import Client, idle
from pyromod import listen



bot = Client(
    "mo",
    api_id=22284698,
    api_hash="80114fbfcdb5b886a9e69f31a7e6b248",
    bot_token="7327600929:AAF3E7EXyjnlmRlzBUvTu3NSWZcwEo66uC0",
    plugins=dict(root="MZombie")
    )

DEVS = ["N_7_K","M_9_T","M_9_T", "noordot"] 

bot_id = bot.bot_token.split(":")[0]

async def start_zombiebot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    for hh in DEVS:
        try:
            await bot.send_message(hh, "**تم تشغيل الصانع بنجاح ...🥀**")
        except:
            pass
    await idle()
