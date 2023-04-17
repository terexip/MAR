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
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from YukkiMusic import app 
from random import  choice, randint




@app.on_message(
    command(["مطور","المطور","المبرمج"])
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("Huseenytiq")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"** ⌔︙معلومات المطور \n ⌔︙الاسم : {name}\n ⌔︙المعرف : @{usr.username}\n ⌔︙الايدي : `{usr.id}`\n ⌔︙البايو : {usr.bio}\n\n****", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],[ 
                    
                   InlineKeyboardButton(
                     text=f"{YAFA_NAME}", url=f"{YAFA_CHANNEL}",)
                ],
                       
            ]
                       
        ),
                    
    )
 
