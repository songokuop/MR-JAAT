from pyrogram import Client, filters
from config import OPENAI_API, LOG_CHANNEL, AI
import openai
import asyncio

openai.api_key = OPENAI_API

async def send_message_in_chunks(client, chat_id, text):
    max_length = 4096  # Maximum length of a message
    for i in range(0, len(text), max_length):
        await client.send_message(chat_id, text[i:i+max_length])


@Client.on_message(filters.private & filters.text & ~filters.command(['start', 'broadcast']))
async def ai_answer(client, message):
    if AI == True: 
        user_id = message.from_user.id
        if user_id:
            try:
                msg = await message.reply_text("⭕ CHAT GPT 4 IS WORKING ■□■●○●▪︎▪︎▪︎•••")
                users_message = message.text
                user_id = message.from_user.id
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": users_message}
                    ],
                    max_tokens=1200,  # Increase the value of max_tokens to allow for longer responses
                    temperature=0.6
                )
                footer_credit = "<b><a href='https://t.me/THE_AI_BOTZ'>• AI BOTZ •</a>•••<a href='https://t.me/AI_BOTZ_MENU_BOT'>• OPEN AI MENU •</a></b>"
                ai_response = response.choices[0].message.content.strip()
                await msg.delete()
                await send_message_in_chunks(client, message.chat.id, f"**RESULT** 👇\n\n{ai_response}\n\n{footer_credit}")
                await send_message_in_chunks(client, LOG_CHANNEL, f"**⭕ ᴀ ᴜsᴇʀ ɴᴀᴍᴇᴅ:** {message.from_user.mention} **ᴡɪᴛʜ ᴜsᴇʀ ɪᴅ -** {user_id}.\n🔍 **ᴀsᴋᴇᴅ ᴍᴇ ᴛʜɪs ǫᴜᴇʀʏ...**👇\n\n🔻 **ǫᴜᴇʀʏ:** `{users_message}`\n\n🔻 **ʜᴇʀᴇ ɪs ᴀɴsᴡᴇʀ ɪ ʀᴇsᴘᴏɴᴅᴇᴅ:**\n🖍️ {ai_response}\n\n\n🔻 **ᴜsᴇʀ ɪᴅ :-** {user_id} \n🔻 **ᴜsᴇʀ ɴᴀᴍᴇ :-** {message.from_user.mention}")
                
            except Exception as error:
                print(error)
                await message.reply_text(f"**An error occurred:**\n\n**{error}**\n\n**Forward This Message To @AI_BOTZ_SUPPORT**")
    else:
        return
