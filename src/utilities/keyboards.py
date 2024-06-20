from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_main_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Update status 🔄", callback_data="ping")],
        [InlineKeyboardButton("Turn On 🟢", callback_data="on"),
         InlineKeyboardButton("Turn Off 🔴", callback_data="off")],
        [InlineKeyboardButton("Schedule ⏰", callback_data="schedule_prompt")]
    ])
