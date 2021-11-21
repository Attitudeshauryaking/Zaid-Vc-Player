import asyncio
from time import time
from datetime import datetime
from config import BOT_USERNAME, UPDATES_CHANNEL, ZAID_SUPPORT
from helpers.filters import command
from helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/be59d5c0d55a63ba62193.jpg",
        caption=f"""**ᴀ ᴀᴅᴠᴀɴᴄᴇᴅ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜꜱɪᴄ ʙᴏᴛ ʙᴀꜱᴇᴅ ᴏɴ ᴍᴏɴɢᴏᴅʙ ᴡɪᴛʜ ᴀɪ ꜰᴇᴀᴛᴜʀᴇꜱ ...
💞 ᴛʜᴀɴᴋꜱ ꜰᴏʀ  
ᴜꜱɪɴɢ [✴𝔸𝕥𝕥𝕚𝕥𝕦𝕕𝕖 𝔾𝕒𝕝𝕒𝕩𝕪✴](t.me/@attitude_galaxy)........
**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔥ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ🔥", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🍹ꜱᴜᴩᴩᴏʀᴛ🍹", url=f"https://t.me/Sweetkingdom1"
                    ),
                    InlineKeyboardButton(
                        "🥂⚜️ᴏᴡɴᴇʀ⚜️🥂", url=f"@Alone_Shaurya_king"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📣ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ📣", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/be59d5c0d55a63ba62193.jpg",
        caption=f"""ᴛʜᴀɴᴋꜱ ꜰᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ🔥♥️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴊᴏɪɴ ʜᴇʀᴇ ᴀɴᴅ sᴜᴘᴘᴏʀᴛ 💞", url=f"https://t.me/attitude_galaxy")
                ]
            ]
        ),
    )


@Client.on_message(command(["repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/bfc3e137fc23773b4cd74.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔥🍹ᴄʟɪᴄᴋ ᴍᴇ ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ🍹🔥", url=f"https://github.com/ItsAttitudeking")
                ]
            ]
        ),
    )
