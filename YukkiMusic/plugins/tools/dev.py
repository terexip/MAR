import asyncio 
import os 
import time 
import requests 
from config import YAFA_NAME, YAFA_CHANNEL 
from pyrogram import filters 
import random 
from pyrogram import Client 
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup 
from strings.filters import command 
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app 
from random import  choice, randint




@app.on_message(
    command(["مطور","المطور","المبرمج"])
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("Huseenytiq")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞  𝙎𝙊𝙉𝙄𝘾 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞  𝙎𝙊𝙉𝙄𝘾 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                  ],
                ],
                [ 
                   InlineKeyboardButton(
                     text=f"{YAFA_NAME}", url=f"{YAFA_CHANNEL}",)
                ],
            ]
        ),
    )
