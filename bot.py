from pyrogram import Client, idle
from config import API_HASH, APP_ID, TG_BOT_TOKEN, PLUGIN_ROOT, ADMINS
from pyrogram.types import BotCommand

app = Client(
    name="FileStoreBot",
    api_id=APP_ID,
    api_hash=API_HASH,
    bot_token=TG_BOT_TOKEN,
    plugins=dict(root=PLUGIN_ROOT)
)

@app.on_message()
async def set_commands_once(client, message):
    if str(message.from_user.id) in ADMINS:
        commands = [
            BotCommand("start", "check I am Alive"),
            BotCommand("link", "To generate sharable link"),
            BotCommand("batch", "To generate batch link"),
            BotCommand("pbatch", "Protected batch link"),
            BotCommand("stats", "To check database"),
            BotCommand("broadcast", "Broadcast message")
        ]
        await client.set_bot_commands(commands)

async def main():
    await app.start()
    print("Bot is running...")
    await idle()
    await app.stop()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())