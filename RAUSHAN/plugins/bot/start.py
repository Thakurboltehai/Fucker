from RAUSHAN import app, API_ID, API_HASH
from config import ALIVE_PIC
from pyrogram import filters
import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import * 

PHONE_NUMBER_TEXT = (
    "**╭────── ˹ ʜᴇʟʟᴏ ʙᴀʙʏ ˼ ──── ⚘**\n**┆⚘ ʜᴇʏ, ɪ ᴀᴍ : [˹ ʀɪsʜᴀɴᴛ ꭙ ᴜsєʀʙσᴛ ˼](https://t.me/Userbotxbot_rebot)**\n**┆⚘ ᴍᴏʀᴇ ᴀɴɪᴍᴀᴛɪᴏɴ, ғᴜɴ, ʀᴀɪᴅ, sᴘᴀᴍ**\n**┊⚘ ᴘᴏᴡᴇʀғᴜʟ & ᴜsᴇғᴜʟʟ ᴜsᴇʀʙᴏᴛ**\n**╰───────────────────────**\n**────────────────────────**\n**❍ ʜᴏᴡ тᴏ ᴜsᴇ тнɪs вσᴛ - [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/publick_hu/224)**\n**────────────────────────**\n**❍ sᴇssɪᴏɴ ɢᴇɴ вᴏᴛ ⁚ [sᴇssɪᴏɴ-ʙᴏᴛ](https://t.me/StringFatherRobot)**\n**────────────────────────**\n**❍ ᴄʟᴏɴᴇ вσт ⁚ /clone [ sᴛʀɪɴɢ sᴇssɪᴏɴ ]**\n**────────────────────────**\n**❍ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ⏤‌ [˹ sᴜᴘᴏʀᴛ ˼](https://t.me/publick_hu)**\n**────────────────────────**"
)

@app.on_message(filters.command("start"))
async def hello(client: app, message):
    buttons = [
           [
                InlineKeyboardButton("˹ 𝐎ᴡɴᴇʀ ˼", url="https://t.me/OY_BABY"),
                InlineKeyboardButton("˹ 𝐔ᴘᴅᴀᴛᴇ ˼", url="https://t.me/publick_hu"),
            ],
            [
                InlineKeyboardButton("˹ 𝐒ᴜᴘᴘᴏʀᴛ ˼", url="https://t.me/publick_hu"),
                InlineKeyboardButton("˹ sᴜᴘᴘᴏʀᴛ ˼", url="https://t.me/publick_hu"),
            ],
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(message.chat.id, ALIVE_PIC, caption=PHONE_NUMBER_TEXT, reply_markup=reply_markup)

@app.on_message(filters.command("clone"))
async def clone(bot: app, msg: Message):
    chat = msg.chat
    text = await msg.reply("ᴜsᴀɢᴇ:\n\n /clone session")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("**ʀᴜᴋ ᴛʜᴏᴅᴀ sᴀ ᴀʟᴘʜᴀ ᴛᴇʀɪ ɢᴀɴᴅ ᴍᴀʀ ʀʜᴀ 👅.....✲**")
                   # change this Directry according to ur repo
        client = Client(name="Melody", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="RAUSHAN/plugins"))
        await client.start()
        user = await client.get_me()
        await msg.reply(f" **ᴊᴀ ᴘᴇʟ sᴀʙᴋᴏ ᴏʀ ʜᴀᴀ ʀɪsʜᴀɴᴛ ᴋᴏ ᴘᴀᴘᴀ ʙᴏʟ ᴋᴇ ᴊᴀɴᴀ** 🥵 {user.first_name} 💨.")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
