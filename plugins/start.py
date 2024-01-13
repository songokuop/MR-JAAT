from pyrogram import Client, filters
from config import LOG_CHANNEL
from plugins.database import db
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message
)


LOG_TEXT = """<b>#NewUser CHATGPT USER
    
ID - <code>{}</code>

Nᴀᴍᴇ - {}</b>
"""

@Client.on_message(filters.command('start'))
async def start_message(c,m):
    await db.is_user_exist(m.from_user.id)
    await db.add_user(m.from_user.id, m.from_user.first_name)
    await c.send_message(LOG_CHANNEL, LOG_TEXT.format(m.from_user.id, m.from_user.mention))
    await m.reply_photo(f"https://telegra.ph/AI-11-01-4",
        caption="**ʜɪ** 👋\n\n**ɪ ᴀᴍ ᴀ ᴄʜᴀᴛɢᴘᴛ ⁴ ʙᴏᴛ**\n\n⭕ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ :-** **[Movies_Zone_Media](https://t.me/Movies_Zone_Media)**",
        reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('🤖 Movies Zone MENU 🤖', url='https://t.me/Movies_Zone_Contact_Bot')
                    ],  
                    [
                        InlineKeyboardButton("MAIN CHANNEL", url='https://t.me/Movies_Zone_Media'),
                        InlineKeyboardButton("SUPPORT GROUP", url='https://t.me/Movies_Zone_Support')
                    ]
                ]
            )
        )
  
