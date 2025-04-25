from pyrogram import Client, filters
from pyrogram.types import Message
from config import ADMINS

@Client.on_message(filters.command("start") & filters.private)
async def start_handler(client, message: Message):
    if str(message.from_user.id) not in ADMINS:
        await message.reply_text("This bot is private. You can only access shared files via link.")
        return
    await message.reply_text("Welcome, Admin. Bot is up and running!")