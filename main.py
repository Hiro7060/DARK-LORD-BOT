from pyrogram import Client, filters

app = Client("darklord", bot_token="8699271898:AAGP_j-Yoy3jQixrWdxfolr0Of8XXyKrLoQ")

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("👑 **DARK LORD BOT** 👑\n\n⚡ `/destroy <target> <method> <time>`\n📊 `/status`\n❓ `/help`")

@app.on_message(filters.command("destroy"))
async def destroy(client, message):
    args = message.text.split()
    if len(args) < 4:
        await message.reply("❌ **Syntax:** `/destroy google.com udp 60`")
        return
    target, method, duration = args[1], args[2], args[3]
    await message.reply(f"💥 **ATTACK LAUNCHED!**\n🎯 `{target}`\n⚡ `{method}`\n⏰ `{duration}s`\n\n✅ **TARGET DESTROYED!**")

@app.on_message(filters.command("status"))
async def status(client, message):
    await message.reply("🔥 **DARK LORD STATUS**\n✅ Bot: Online\n✅ Attacks: Ready\n👑 Admin: Active")

@app.on_message(filters.command("help"))
async def help(client, message):
    await message.reply("⚡ **Commands:**\n`/start` - Welcome\n`/destroy target method time` - Attack\n`/status` - Status\n`/help` - Help")

print("👑 DARK LORD BOT LIVE!")
app.run()
