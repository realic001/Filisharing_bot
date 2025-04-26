from pyrogram import Client, filters

@Client.on_message(filters.document | filters.video | filters.audio & filters.private)
async def save_file(client, message):
    await message.reply_text("✅ File saved successfully!")