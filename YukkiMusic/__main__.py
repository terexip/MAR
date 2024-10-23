import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls import GroupCall  # تأكد من أن هذه الكلاسات متاحة
from pytgcalls.exceptions import NoActiveCall  # تأكد من استخدام الاستثناء الصحيح

import config
from config import BANNED_USERS
from YukkiMusic import LOGGER, app, userbot
from YukkiMusic.core.call import Yukki
from YukkiMusic.plugins import ALL_MODULES
from YukkiMusic.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()

async def init():
    # (بقية الكود كما هو)
    try:
        await Yukki.stream_call(
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
    except NoActiveCall:  # تأكد من استخدام الاستثناء الصحيح هنا
        LOGGER("YukkiMusic").error(
            "[ERROR] - \n\nPlease turn on your Logger Group's Voice Call."
        )
        sys.exit()
    # (بقية الكود تبقى كما هي)

if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("YukkiMusic").info("Stopping Yukki Music Bot! GoodBye")
