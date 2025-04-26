from pyrogram import Client, filters

@Client.on_message(filters.command("broadcast") & filters.user(int))
async def broadcast(client, message):
    text = message.text.split(" ", 1)[1]
    for user_id in [123456789, 987654321]:  # Example user IDs
        try:
            await client.send_message(user_id, text)
        except Exception:
            continue
    await message.reply_text("✅ Broadcast complete!")