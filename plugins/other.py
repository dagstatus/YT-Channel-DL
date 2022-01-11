from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio


@Client.on_message(filters.command("start"))
async def start_msg(client, message):
    await message.reply_text(
        f"Привет {message.from_user.mention}, я умею скачивать видео с YouTube.\n\n:Жми помощь чтобы узнать как пользоваться",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("🛠 Помощь", callback_data=f"help"),
                InlineKeyboardButton("🧰 Обо мне", callback_data=f"about")
            ]]
        ),
        quote=True)


@Client.on_callback_query()
async def cb_handler(client, update):
    cb_data = update.data

    if "help" in cb_data:
        await update.message.edit_text(
            "Просто отправь ссылку на видео, на плейлист или канал и все видео будут скачаны.\nПример:\n`https://youtube.com/channel/UCfwavlAv6xw`",
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton("🧰 Обо мне", callback_data=f"about"),
                    InlineKeyboardButton("🔙 Назад", callback_data=f"back")
                ]]
            ))
    elif "about" in cb_data:
        await update.message.edit_text("Написано на Python\n@dagstatus",
                                       reply_markup=InlineKeyboardMarkup(
                                           [[
                                               InlineKeyboardButton("🛠 Помощь", callback_data=f"help"),
                                               InlineKeyboardButton("🔙 Назад", callback_data=f"back")
                                           ]]
                                       ))
    elif "back" in cb_data:
        await update.message.edit_text(
            f"Привет {update.from_user.mention}, я умею скачивать видео с YouTube.\n\n:Жми помощь чтобы узнать как пользоваться",
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton("🛠 Помощь", callback_data=f"help"),
                    InlineKeyboardButton("🧰 Обо мне", callback_data=f"about")
                ]]
            ))
