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
    await message.reply_photo(photo,       caption=f"** - 𝒎𝒂𝒊𝒏 𝒅𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓 𝒊𝒏𝒇𝒐𝒓𝒎𝒂𝒕𝒊𝒐𝒏 : \n\n‍ ⌔︙اسم المطور \n :{name}\n ⌔︙معرف المطور \n :@{usr.username}\n ⌔︙ايدي المطور \n :`{usr.id}`\n ⌔︙بايو المطور \n :{usr.bio}\n\n****", 
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
 
