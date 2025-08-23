from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from hasnainkk import app, START_IMG, BOT_USERNAME, BOT_NAME

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
            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url="https://t.me/endxoz")
        ]
    ]
)

HELP_MSG = """
**ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ᴏɴʟʏ ʙᴇ ᴜsᴇᴅ ɪɴ ɢʀᴏᴜᴘs**

• /banall : ʙᴀɴ-ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ
• /unbanall : ᴜɴʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ
• /kickall : ᴋɪᴄᴋ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ
• /muteall : ᴍᴜᴛᴇ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ
• /unmuteall : ᴜɴᴍᴜᴛᴇ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ
• /unpinall : ᴜɴᴘɪɴ ᴀʟʟ ᴍᴇssᴀɢᴇs ɪɴ ᴀ ɢʀᴏᴜᴘ
• /users : ɢᴇᴛ ʟɪsᴛ ᴏғ ᴀʟʟ ᴍᴇᴍʙᴇʀs
• /groups : ɢᴇᴛ ʟɪsᴛ ᴏғ ᴀʟʟ ɢʀᴏᴜᴘs
• /broadcast : ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜsᴇʀs
• /stats : sʜᴏᴡ ʙᴏᴛ sᴛᴀᴛs

ᴄʀᴇᴀᴛᴇᴅ ʙʏ: [Hasnain khan](https://t.me/hasnainkk)
"""

@app.on_message(filters.command("start"))
async def start(_, msg):
    await msg.reply_photo(
        photo=START_IMG,
        caption=START_MSG.format(msg.from_user.mention, BOT_NAME),
        reply_markup=START_BUTTONS
    )

@app.on_callback_query(filters.regex("help_back"))
async def help_back(_, callback_query: CallbackQuery):
    await callback_query.message.edit_caption(HELP_MSG)

@app.on_message(filters.command("help"))
async def help(_, msg):
    await msg.reply_text(HELP_MSG)
