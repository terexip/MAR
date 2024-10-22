import asyncio
import importlib
import sys
from pyrogram import Client
from pytgcalls import PyTgCalls

# استيراد الإعدادات
import config
from YukkiMusic import LOGGER, app, userbot
from YukkiMusic.core.call import Yukki
from YukkiMusic.plugins import ALL_MODULES

loop = asyncio.get_event_loop()

async def main():
    # تحقق من وجود التوكنات والإعدادات اللازمة
    if not config.BOT_TOKEN:
        LOGGER("YukkiMusic").error("No Bot Token Defined. Exiting.")
        return
    
    await app.start()
    for module in ALL_MODULES:
        importlib.import_module("YukkiMusic.plugins" + module)

    LOGGER("YukkiMusic").info("Yukki Music Bot Started Successfully")
    await Yukki.start()
    
    try:
        # قم بتشغيل البوت
        await loop.run_forever()
    except Exception as e:
        LOGGER("YukkiMusic").error(f"Error occurred: {str(e)}")
    finally:
        await app.stop()

if __name__ == "__main__":
    loop.run_until_complete(main())
