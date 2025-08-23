from pyrogram import filters
from pyrogram.types import ChatPermissions
from hasnainkk import app, BOT_ID, SUDO
from pyrogram.enums import ChatMemberStatus


async def is_admin(chat_id: int, user_id: int) -> bool:
    try:
        member = await app.get_chat_member(chat_id, user_id)
        return (
            member.status == ChatMemberStatus.ADMINISTRATOR
            or member.status == ChatMemberStatus.OWNER
        )
    except Exception:
        return False


async def is_owner(chat_id: int, user_id: int) -> bool:
    try:
        member = await app.get_chat_member(chat_id, user_id)
        return member.status == ChatMemberStatus.OWNER
    except Exception:
        return False

@app.on_message(filters.command("banall") & filters.group)
async def ban_all(_, msg):
    # Check if user is sudo, group admin, or owner
    user_id = msg.from_user.id
    chat_id = msg.chat.id
    
    if user_id not in SUDO and not await is_admin(chat_id, user_id):
        return await msg.reply_text("🚫 You need to be an admin or sudo user to use this command.")
    
    bot = await app.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot.privileges.can_restrict_members if bot.privileges else False

    if bot_permission:
        count = 0
        async for member in app.get_chat_members(chat_id):
            # Don't ban self, sudo users, or other admins (unless user is sudo)
            if member.user.id == BOT_ID:
                continue
                
            if user_id not in SUDO:
                # Regular admins can't ban other admins or sudo users
                if member.user.id in SUDO or await is_admin(chat_id, member.user.id):
                    continue
            
            try:
                await app.ban_chat_member(chat_id, member.user.id)
                count += 1
            except Exception:
                pass
        await msg.reply_text(f"✅ Banned {count} members!")
    else:
        await msg.reply_text("❌ I don't have permission to restrict users!")

@app.on_message(filters.command("unbanall") & filters.group)
async def unban_all(_, msg):
    user_id = msg.from_user.id
    chat_id = msg.chat.id
    
    if user_id not in SUDO and not await is_admin(chat_id, user_id):
        return await msg.reply_text("🚫 You need to be an admin or sudo user to use this command.")
    
    bot = await app.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot.privileges.can_restrict_members if bot.privileges else False

    if bot_permission:
        count = 0
        async for m in app.get_chat_members(chat_id, filter="banned"):
            try:
                await app.unban_chat_member(chat_id, m.user.id)
                count += 1
            except Exception:
                pass
        await msg.reply_text(f"✅ Unbanned {count} members!")
    else:
        await msg.reply_text("❌ I don't have permission to restrict users!")

@app.on_message(filters.command("kickall") & filters.group)
async def kick_all(_, msg):
    user_id = msg.from_user.id
    chat_id = msg.chat.id
    
    if user_id not in SUDO and not await is_admin(chat_id, user_id):
        return await msg.reply_text("🚫 You need to be an admin or sudo user to use this command.")
    
    bot = await app.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot.privileges.can_restrict_members if bot.privileges else False

    if bot_permission:
        count = 0
        async for member in app.get_chat_members(chat_id):
            # Don't kick self, sudo users, or other admins (unless user is sudo)
            if member.user.id == BOT_ID:
                continue
                
            if user_id not in SUDO:
                # Regular admins can't kick other admins or sudo users
                if member.user.id in SUDO or await is_admin(chat_id, member.user.id):
                    continue
            
            try:
                await app.ban_chat_member(chat_id, member.user.id)
                await app.unban_chat_member(chat_id, member.user.id)
                count += 1
            except Exception:
                pass
        await msg.reply_text(f"✅ Kicked {count} members!")
    else:
        await msg.reply_text("❌ I don't have permission to restrict users!")

@app.on_message(filters.command("muteall") & filters.group)
async def mute_all(_, msg):
    user_id = msg.from_user.id
    chat_id = msg.chat.id
    
    if user_id not in SUDO and not await is_admin(chat_id, user_id):
        return await msg.reply_text("🚫 You need to be an admin or sudo user to use this command.")
    
    bot = await app.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot.privileges.can_restrict_members if bot.privileges else False

    if bot_permission:
        count = 0
        async for member in app.get_chat_members(chat_id):
            # Don't mute self, sudo users, or other admins (unless user is sudo)
            if member.user.id == BOT_ID:
                continue
                
            if user_id not in SUDO:
                # Regular admins can't mute other admins or sudo users
                if member.user.id in SUDO or await is_admin(chat_id, member.user.id):
                    continue
            
            try:
                await app.restrict_chat_member(chat_id, member.user.id, ChatPermissions())
                count += 1
            except Exception:
                pass
        await msg.reply_text(f"✅ Muted {count} members!")
    else:
        await msg.reply_text("❌ I don't have permission to restrict users!")

@app.on_message(filters.command("unmuteall") & filters.group)
async def unmute_all(_, msg):
    user_id = msg.from_user.id
    chat_id = msg.chat.id
    
    if user_id not in SUDO and not await is_admin(chat_id, user_id):
        return await msg.reply_text("🚫 You need to be an admin or sudo user to use this command.")
    
    bot = await app.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot.privileges.can_restrict_members if bot.privileges else False

    if bot_permission:
        count = 0
        permissions = ChatPermissions(
            can_send_messages=True,
            can_send_media_messages=True,
            can_send_polls=True,
            can_send_other_messages=True,
            can_add_web_page_previews=True,
            can_change_info=True,
            can_invite_users=True,
            can_pin_messages=True
        )
        
        async for member in app.get_chat_members(chat_id):
            if member.user.id != BOT_ID:
                try:
                    await app.restrict_chat_member(chat_id, member.user.id, permissions)
                    count += 1
                except Exception:
                    pass
        await msg.reply_text(f"✅ Unmuted {count} members!")
    else:
        await msg.reply_text("❌ I don't have permission to restrict users!")

@app.on_message(filters.command("unpinall") & filters.group)
async def unpin_all(_, msg):
    user_id = msg.from_user.id
    chat_id = msg.chat.id
    
    if user_id not in SUDO and not await is_admin(chat_id, user_id):
        return await msg.reply_text("🚫 You need to be an admin or sudo user to use this command.")
    
    bot = await app.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot.privileges.can_pin_messages if bot.privileges else False

    if bot_permission:
        count = 0
        async for message in app.get_chat_history(chat_id):
            if message.pinned:
                try:
                    await app.unpin_chat_message(chat_id, message.id)
                    count += 1
                except Exception:
                    pass
        await msg.reply_text(f"✅ Unpinned {count} messages!")
    else:
        await msg.reply_text("❌ I don't have permission to pin/unpin messages!")

# New command to promote all members to admin (only for group owners)
@app.on_message(filters.command("promoteall") & filters.group)
async def promote_all(_, msg):
    user_id = msg.from_user.id
    chat_id = msg.chat.id
    
    # Only group owners can use this command
    if not await is_owner(chat_id, user_id):
        return await msg.reply_text("🚫 Only group owners can use this command.")
    
    bot = await app.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot.privileges.can_promote_members if bot.privileges else False

    if bot_permission:
        count = 0
        async for member in app.get_chat_members(chat_id):
            # Don't promote self, sudo users, or already admins
            if (member.user.id == BOT_ID or 
                member.user.id in SUDO or 
                await is_admin(chat_id, member.user.id)):
                continue
            
            try:
                await app.promote_chat_member(
                    chat_id,
                    member.user.id,
                    can_change_info=True,
                    can_delete_messages=True,
                    can_restrict_members=True,
                    can_invite_users=True,
                    can_pin_messages=True,
                    can_manage_video_chats=True
                )
                count += 1
            except Exception:
                pass
        await msg.reply_text(f"✅ Promoted {count} members to admin!")
    else:
        await msg.reply_text("❌ I don't have permission to promote members!")
