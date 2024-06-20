from pyrogram import Client
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from led_service import LEDService
from utilities.keyboards import get_main_keyboard

led_service = LEDService()


def start(client: Client, message):
    ping_response = led_service.send_request("ping")
    success, response_data = ping_response

    if success:
        message.reply(response_data, reply_markup=get_main_keyboard())
    else:
        message.reply("LED service is unavailable.")


def schedule(client: Client, message):
    try:
        _, on_time, off_time = message.text.split()
        on_time = int(on_time)
        off_time = int(off_time)
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("Confirm Schedule", callback_data=f"schedule:{on_time}:{off_time}")]
        ])
        message.reply(f"Schedule LED with **on time: {on_time}ms** and **off time: {off_time}ms**",
                      reply_markup=keyboard)
    except ValueError:
        message.reply("Usage: /schedule <on_time_ms> <off_time_ms>", parse_mode=ParseMode.MARKDOWN)
