# https://t.me/chickchoker

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://graph.org/file/924052956c320c4a30e2c.jpg",
    "https://graph.org/file/eac99dd18a261b11adaca.jpg",
    "https://graph.org/file/8c924fd0844c6cadedd07.jpg",
    "https://graph.org/file/4d8f6f38a7f3683fa2a4a.jpg",
    "https://graph.org/file/67979fc64642071b7e8e3.jpg",
    "https://graph.org/file/f4ec6cba9db0a9e570ff4.jpg",
    "https://graph.org/file/4708c35417ea1f985d2fc.jpg",
]

HEY_IMG = "https://telegra.ph/file/33a8d97739a2a4f81ddde.jpg"

ALIVE_ANIMATION = [
    "https://telegra.ph//file/f9e2b9cdd9324fc39970a.mp4",
    "https://telegra.ph//file/8d4d7d06efebe2f8becd0.mp4",
    "https://telegra.ph//file/c4c2759c5fc04cefd207a.mp4",
    "https://telegra.ph//file/b1fa6609b1c4807255927.mp4",
    "https://telegra.ph//file/f3c7147da6511fbe27c25.mp4",
    "https://telegra.ph//file/39071b73c02e3ff5945ca.mp4",
    "https://telegra.ph//file/8d4d7d06efebe2f8becd0.mp4",
    "https://telegra.ph//file/6efdd8e28756bc2f6e53e.mp4",
]

FIRST_PART_TEXT = "✨ *ʜᴇʟʟᴏ* `{}` . . ."

PM_START_TEXT = "✨ *ɪ'ᴍ ᴀꜱᴀ ᴍɪᴛᴀᴋᴀ . . .

❖ ᴀ ᴘᴏᴡᴇʀꜰᴜʟ ᴀɴᴅ ᴀᴅᴠᴀɴᴄᴇᴅ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ. ɪ'ᴍ ʜᴇʀᴇ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ꜱᴜᴘᴇʀ ᴄᴏᴏʟ ꜰᴇᴀᴛᴜʀᴇꜱ. ✨

≪━─━─━─━─◈─━─━─━─━≫
• ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ 🔑
• ɪɴꜰᴏ ᴘʀᴏᴠɪᴅᴇʀ 📤
• ᴀɴᴛɪ ꜱᴘᴀᴍ 🚨
• ᴀɪ ᴀʀᴛɪꜰɪᴄɪᴀʟ ɪɴᴛᴇʟʟɪɢᴇɴᴄᴇ 🤖
• ᴍᴀɴʏ ɪɴᴛᴇʀᴇꜱᴛɪɴɢ ᴛʜɪɴɢꜱ ✨
≪━─━─━─━─◈─━─━─━─━≫

ᴛʏᴘᴇ /start ᴛᴏ ꜱᴛᴀʀᴛ ᴍᴇ ɪɴ ᴅᴍ.
ᴛʏᴘᴇ /help ᴛᴏ ᴄʜᴇᴄᴋᴏᴜᴛ ᴍʏ ᴄᴏᴏʟ ꜰᴇᴀᴛᴜʀᴇꜱ.*"

START_BTN = [
    [
        InlineKeyboardButton(
            text="❖ ADD ME ❖",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="HELP/commands", callback_data="help_back"),
    ],
    [
        InlineKeyboardButton(text="Info", callback_data="Miko_"),
        InlineKeyboardButton(text="AI", callback_data="ai_handler"),
    ],
    [
        InlineKeyboardButton(text="Developer", url=f"tg://user?id={OWNER_ID}"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="❖ ADD ME ❖",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="SUPPORT", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="UPDATES", url="https://t.me/Hydra_Updates"),
        ib(text="SUPPORT", url="https://t.me/hydraXsupport"),
    ],
    [
        ib(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
🫧 *Yae-Miko* 🫧

☉ *Here, you will find a list of all the available commands.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
