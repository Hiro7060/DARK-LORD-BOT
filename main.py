import os
import logging
import requests
from pyrogram import Client, filters
from pyrogram.types import Message

logging.getLogger("pyrogram").setLevel(logging.WARNING)

app = Client("dark_lord_bot", bot_token=os.getenv("BOT_TOKEN"))

API_URL = os.getenv("API_URL", "https://httpbin.org")
API_KEY = os.getenv("API_KEY", "sk-darklord-aditya-2024")
ADMIN_IDS = [6975889263]

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply("👑 **DARK LORD BOT** 👑\n\n⚡ /destroy <target> <method> <time>\n📊 /status\n❓ /help")

@app.on_message(filters.command("destroy") & filters.private)
async def destroy(client, message):
    if message.from_user.id not in ADMIN_IDS:
        return await message.reply("🚫 Admin only!")
    
    args = message.text.split()[1:]
    if len(args) < 3:
        return await message.reply("❌ /destroy google.com udp 60")
    
    target = args[0]
    method = args[1]
    duration = args[2]
    
    await message.reply(f"💥 **ATTACK LAUNCHED**\n🎯 {target}\n⚡ {method}\n⏰ {duration}s")
    
    # Mock API call
    await message.reply(f"✅ **SUCCESS** - {target} destroyed!")

@app.on_message(filters.command("status") & filters.private)
async def status(client, message):
    await message.reply(f"🔥 **DARK LORD STATUS**\nAPI: {API_URL}\nAdmin: {ADMIN_IDS[0]}\nStatus: Online")

@app.on_message(filters.command("api") & filters.private)
async def api(client, message):
    await message.reply(f"🌐 API: {API_URL}\n🔑 Key: {API_KEY[:10]}...")

@app.on_message(filters.command("help") & filters.private)
async def help(client, message):
    await message.reply("⚡ **Commands:**\n/destroy google.com udp 60\n/status\n/help")

print("👑 DARK LORD Starting...")
app.run()
