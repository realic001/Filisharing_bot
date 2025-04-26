from pyrogram import Client, idle
from config import API_HASH, APP_ID, TG_BOT_TOKEN, PLUGIN_ROOT
from webserver import keep_alive

app = Client(
    name="FileStoreBot",
    api_id=APP_ID,
    api_hash=API_HASH,
    bot_token=TG_BOT_TOKEN,
    plugins=dict(root=PLUGIN_ROOT)
)

async def main():
    keep_alive()
    await app.start()
    print("Bot is running...")
    await idle()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
