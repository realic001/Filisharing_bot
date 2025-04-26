from pyrogram import Client, filters

@Client.on_message(filters.command("stats") & filters.private)
async def stats(client, message):
    await message.reply_text("📊 Total saved users: 2")