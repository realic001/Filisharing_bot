from pyrogram import Client, filters

@Client.on_message(filters.command("batch") & filters.private)
async def batch(client, message):
    await message.reply_text("🔗 Batch link created!")