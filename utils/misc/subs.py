from data.config import CHANNELS
from loader import bot


async def check_sub_channels(message):
    for channel in CHANNELS:
        check = await bot.get_chat_member(channel[1], message.from_user.id)

        if check.status == "left":
            return False

    return True

