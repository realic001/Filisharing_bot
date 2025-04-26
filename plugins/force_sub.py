from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant

FORCE_SUB_CHANNEL = -1001234567890

@Client.on_message(filters.private)
async def force_sub(client, message):
    try:
        user = await client.get_chat_member(FORCE_SUB_CHANNEL, message.from_user.id)
    except UserNotParticipant:
        link = await client.create_chat_invite_link(FORCE_SUB_CHANNEL)
        await message.reply_text(f"⚠️ You must join [this channel]({link.invite_link}) to use me.", disable_web_page_preview=True)
        return