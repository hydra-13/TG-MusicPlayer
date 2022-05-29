import asyncio

from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.errors import FloodWait, UserNotParticipant
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest
from MusicPlayer.utils.filters import command

from MusicPlayer import BOT_NAME, BOT_USERNAME
from MusicPlayer.config import BOT_USERNAME 
from MusicPlayer.config import BOT_NAME
from MusicPlayer.config import START_IMG

@Client.on_message(command("mstart") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})** 

I am **[{BOT_NAME}](https://t.me/{BOT_USERNAME}),** a lag free music bot player for your groups 

I can play music in your groups without any bugs. Just add me to your group & promote as a admin with needed admin permissions to perform a right actions !

Use the given buttons for more info📍""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Commands", callback_data="cbcmnds"),
                    InlineKeyboardButton(
                        "About", callback_data="cbabout")
                ],
                [
                    InlineKeyboardButton(
                        "Basic Guide", callback_data="cbguide")
                ],
                [
                    InlineKeyboardButton(
                        "✚ Add Bot in Your Group ✚", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
           ]
        ),
    )
