from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.config import CHANNELS


async def show_channels():
    keyboard = InlineKeyboardMarkup(row_width=1)

    for channel in CHANNELS:
        btn = InlineKeyboardButton(text=channel[0], url=channel[2])
        keyboard.insert(btn)

    done = InlineKeyboardButton(text="✅ A`zo Bo`ldim ✅", callback_data="sub_channels_bot")
    keyboard.insert(done)

    return keyboard

