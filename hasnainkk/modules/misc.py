import os
import time
from pyrogram import filters
from hasnainkk import app, SUDO, LOG_CHANNEL

@app.on_message(filters.command("broadcast") & filters.private)
async def broadcast(_, msg):
    if msg.from_user.id not in SUDO:
        return await msg.reply_text("🚫 You need to be a sudo user to use this command.")
    
    if not msg.reply_to_message:
        return await msg.reply_text("❌ Please reply to a message to broadcast.")
    
    users = []
    async for dialog in app.get_dialogs():
        if dialog.chat.type == "private":
            users.append(dialog.chat.id)
    
    success = 0
    failed = 0
    
    broadcast_msg = msg.reply_to_message
    await msg.reply_text(f"📢 Starting broadcast to {len(users)} users...")
    
    for user_id in users:
        try:
            await broadcast_msg.copy(user_id)
            success += 1
            time.sleep(0.2)  # Avoid flooding
        except Exception:
            failed += 1
    
    await msg.reply_text(
        f"✅ Broadcast completed!\n\n"
        f"**Success:** {success}\n"
        f"**Failed:** {failed}"
    )
    
    # Log to channel
    if LOG_CHANNEL:
        try:
            await app.send_message(
                LOG_CHANNEL,
                f"#BROADCAST\n\n"
                f"Broadcast sent to {success} users.\n"
                f"Failed for {failed} users.\n"
                f"By: {msg.from_user.mention}"
            )
        except Exception:
            pass

@app.on_message(filters.command("log") & filters.private)
async def send_log(_, msg):
    if msg.from_user.id not in SUDO:
        return await msg.reply_text("🚫 You need to be a sudo user to use this command.")
    
    if os.path.exists("log.txt"):
        await msg.reply_document("log.txt")
    else:
        await msg.reply_text("❌ No log file found!")

@app.on_message(filters.command("restart") & filters.private)
async def restart_bot(_, msg):
    if msg.from_user.id not in SUDO:
        return await msg.reply_text("🚫 You need to be a sudo user to use this command.")
    
    await msg.reply_text("🔄 Restarting bot...")
    os.system("pip install -U -r requirements.txt")
    os.execl(sys.executable, sys.executable, "-m", "hasnainkk")
