from pyrogram import Client, idle
from pyromod import listen



bot = Client(
    "mo",
    api_id=9671629,
    api_hash="be5c84e9dc1ca0e2b53d54b71e575124",
    bot_token="7324813477:AAEU31qskRcD8U-M4IsGpLeGnTT8UIhQRR4",
    plugins=dict(root="MZombie")
    )

DEVS = ["BDB0B","BDB0B","BDB0B", "noordot"] 

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
