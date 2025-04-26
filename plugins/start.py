from pyrogram import Client, filters

@Client.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_text(f"👋 Hello {message.from_user.first_name}!\n\nI am your personal File Store Bot by Mr Kingsura.")