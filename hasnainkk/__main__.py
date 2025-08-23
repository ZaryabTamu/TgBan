from hasnainkk import app, START_IMG, BOT_USERNAME, BOT_NAME, LOG, BOT_ID, SUDO
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, ChatPermissions
from hydragram import handler, setup 


setup(
    OWNER_ID=6346273488,  # Replace Your user ID and generate from @Raiden_Robot
    DEV_USERS=[8171988347, 5907205317],  # Your dev team Id and generate Their I'd from @Raiden_Robot
    PREFIX_HANDLER=["/", "!" "Raiden ", "raiden "],  # Command prefixes
    BOT_USERNAME="Bot_RoxBot"  # Your bot's username
)

START_MSG = """
ʜᴇʏ **{}**, ɪ ᴀᴍ {},
ɪ ʜᴀᴠᴇ sᴏᴍᴇ ɪɴᴛᴇʀᴇsᴛɪɴɢ ᴘʟᴜɢɪɴs ʏᴏᴜ sʜᴏᴜʟᴅ ᴛʀʏ ɪᴛ ʙʏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ.
ᴀᴅᴅ ᴍᴇ ɪɴ ᴏᴛʜᴇʀs ɢʀᴏᴜᴘ ᴛᴏ ᴅᴇsᴛʀᴏʏ ɪᴛ.
"""

START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="➕ ᴀᴅᴅ ᴍᴇ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton(text="ʜᴇʟᴘ", callback_data="help_back"),
            InlineKeyboardButton(text="sᴏᴜʀᴄᴇ", url="https://github.com/hasnainkk/Tg-BanAll")
        ],
        [
            InlineKeyboardButton(text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/hasnainkk"),
            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url="https://t.me/Endxoz")
        ]
    ]
)

HELP_MSG = """
**ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ᴏɴʟʏ ʙᴇ ᴜsᴇᴅ ɪɴ ɢʀᴏᴜᴘs**

• /banall : ʙᴀɴ-ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ

• /unbanall : ᴜɴʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ

• /kickall : ᴋɪᴄᴋ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ

• /muteall : ᴍᴜᴛᴇ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ

• /unmuteall : ᴜɴᴍᴜᴛᴇ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ(sᴛɪʟʟ ᴡɪʟʟ ᴛʜᴇ ʟɪsᴛ ɪɴ ʀᴇsᴛʀɪᴄᴛᴇᴅ ᴍᴇᴍʙᴇʀs ʙᴜᴛ ᴀʟʟ ʀᴇsᴛʀɪᴄᴛɪᴏɴs ᴡɪʟʟ ɢᴏ)

• /unpinall : ᴜɴᴘɪɴ ᴀʟʟ ᴍᴇssᴀɢᴇs ɪɴ ᴀ ɢʀᴏᴜᴘ.

ᴄʀᴇᴀᴛᴇᴅ ʙʏ: [Hasnain khan](https://t.me/hasnainkk)
"""


@hanlder("start", dev_cmd=True, admin_cmd=True)
async def start(_, msg):
    await msg.reply_photo(
        photo=START_IMG,
        caption=START_MSG.format(msg.from_user.mention, BOT_NAME),
        reply_markup=START_BUTTONS
    )

@app.on_callback_query(filters.regex("help_back"))
async def help_back(_, callback_query: CallbackQuery):
    query = callback_query.message
    await query.edit_caption(HELP_MSG)

@handler("banall", dev_cmd=True, admin_cmd=True)
async def ban_all(_, msg):
    chat_id = msg.chat.id
    bot = await app.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot.privileges.can_restrict_members

    if bot_permission:
        async for member in app.get_chat_members(chat_id):
            try:
                await app.ban_chat_member(chat_id, member.user.id)
                await msg.reply_text(f"ʙᴀɴɴɪɴɢ {member.user.mention}")
            except Exception:
                pass
    else:
        await msg.reply_text("ᴇɪᴛʜᴇʀ ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀɪɢʜᴛ ᴛᴏ ʀᴇsᴛʀɪᴄᴛ ᴜsᴇʀs ᴏʀ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ɪɴ sᴜᴅᴏ ᴜsᴇʀs")

@handler("unbanall", dev_cmd=True, admin_cmd=True)
async def unban_all(_, msg):
    chat_id = msg.chat.id
    banned_users = []

    bot = await app.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot.privileges.can_restrict_members

    if bot_permission:
        async for m in app.get_chat_members(chat_id, filter="banned"):
            banned_users.append(m.user.id)
            try:
                await app.unban_chat_member(chat_id, banned_users[-1])
                await msg.reply_text(f"ᴜɴʙᴀɴɪɴɢ {m.user.mention}")
            except Exception:
                pass
    else:
        await msg.reply_text("ᴇɪᴛʜᴇʀ ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀɪɡʜᴛ ᴛᴏ ʀᴇsᴛʀɪᴄᴛ ᴜsᴇʀs ᴏʀ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ɪɴ sᴜᴅᴏ ᴜsᴇʀs")

@handler("kickall", dev_cmd=True, admin_cmd=True)
async def kick_all(_, msg):
    chat_id = msg.chat.id
    bot = await app.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot.privileges.can_restrict_members

    if bot_permission:
        async for member in app.get_chat_members(chat_id):
            try:
                await app.kick_chat_member(chat_id, member.user.id)
                await msg.reply_text(f"ᴋɪᴄᴋɪɴɢ {member.user.mention}")
            except Exception:
                pass
    else:
        await msg.reply_text("ᴇɪᴛʜᴇʀ ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀɪɡʜᴛ ᴛᴏ ʀᴇsᴛʀɪᴄᴛ ᴜsᴇʀs ᴏʀ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ɪɴ sᴜᴅᴏ ᴜsᴇʀs")

@handler("muteall", dev_cmd=True, admin_cmd=True)
async def mute_all(_, msg):
    chat_id = msg.chat.id
    bot = await app.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot.privileges.can_restrict_members

    if bot_permission:
        async for member in app.get_chat_members(chat_id):
            try:
                await app.restrict_chat_member(chat_id, member.user.id, ChatPermissions(can_send_messages=False))
                await msg.reply_text(f"ᴍᴜᴛɪɴɢ {member.user.mention}")
            except Exception:
                pass
    else:
        await msg.reply_text("ᴇɪᴛʜᴇʀ ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀɪɡʜᴛ ᴛᴏ ʀᴇsᴛʀɪᴄᴛ ᴜsᴇʀs ᴏʀ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ɪɴ sᴜᴅᴏ ᴜsᴇʀs")

@hanlder("unbanall", dev_cmd=True, admin_cmd=True)
async def unmute_all(_, msg):
    chat_id = msg.chat.id
    bot = await app.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot.privileges.can_restrict_members

    if bot_permission:
        async for member in app.get_chat_members(chat_id):
            try:
                await app.restrict_chat_member(chat_id, member.user.id, ChatPermissions(can_send_messages=True))
                await msg.reply_text(f"ᴜɴᴍᴜᴛɪɴɢ {member.user.mention}")
            except Exception:
                pass
    else:
        await msg.reply_text("ᴇɪᴛʜᴇʀ ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀɪɡʜᴛ ᴛᴏ ʀᴇsᴛʀɪᴄᴛ ᴜsᴇʀs ᴏʀ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ɪɴ sᴜᴅᴏ ᴜsᴇʀs")

@hanlder("unpinall", dev_cmd=True, admin_cmd=True)
async def unpin_all(_, msg):
    chat_id = msg.chat.id
    bot = await app.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot.privileges.can_pin_messages

    if bot_permission:
        async for message in app.get_chat_history(chat_id):
            try:
                await app.unpin_chat_message(chat_id, message.message_id)
                await msg.reply_text(f"ᴜɴᴘɪɴɪɴɢ ᴍᴇssᴀɢᴇ {message.message_id}")
            except Exception:
                pass
    else:
        await msg.reply_text("ᴇɪᴛʜᴇʀ ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀɪɡʜᴛ ᴛᴏ ᴘɪɴ ᴏʀ ᴜɴᴘɪɴ ᴍᴇssᴀɢᴇs ᴏʀ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ɪɴ sᴜᴅᴏ ᴜsᴇʀs")

# Add any additional modules or command handlers here

# Start the bot
if __name__ == "__main__":
    app.run()
