from pyrogram import filters
from hasnainkk import app, SUDO

@app.on_message(filters.command("stats"))
async def stats(_, msg):
    if msg.from_user.id not in SUDO:
        return await msg.reply_text("🚫 You need to be a sudo user to use this command.")
    
    users = 0
    groups = 0
    
    async for dialog in app.get_dialogs():
        if dialog.chat.type == "private":
            users += 1
        elif dialog.chat.type in ["group", "supergroup"]:
            groups += 1
    
    await msg.reply_text(
        f"📊 **Bot Stats:**\n\n"
        f"**Users:** {users}\n"
        f"**Groups:** {groups}\n"
        f"**Sudo Users:** {len(SUDO)}"
    )

@app.on_message(filters.command("users") & filters.private)
async def users_list(_, msg):
    if msg.from_user.id not in SUDO:
        return await msg.reply_text("🚫 You need to be a sudo user to use this command.")
    
    users = []
    async for dialog in app.get_dialogs():
        if dialog.chat.type == "private":
            users.append(f"{dialog.chat.first_name} | {dialog.chat.id}")
    
    with open("users.txt", "w") as f:
        f.write("\n".join(users))
    
    await msg.reply_document("users.txt")
    os.remove("users.txt")

@app.on_message(filters.command("groups") & filters.private)
async def groups_list(_, msg):
    if msg.from_user.id not in SUDO:
        return await msg.reply_text("🚫 You need to be a sudo user to use this command.")
    
    groups = []
    async for dialog in app.get_dialogs():
        if dialog.chat.type in ["group", "supergroup"]:
            groups.append(f"{dialog.chat.title} | {dialog.chat.id}")
    
    with open("groups.txt", "w") as f:
        f.write("\n".join(groups))
    
    await msg.reply_document("groups.txt")
    os.remove("groups.txt")
