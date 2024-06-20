from pyrogram.enums import ParseMode

from services.led_service import LEDService
from utilities.keyboards import get_main_keyboard

led_service = LEDService()


def handle_callback_query(client, callback_query):
    callback_data = callback_query.data.split(":")
    action = callback_data[0]

    if action == "schedule_prompt":
        callback_query.message.reply("Usage: /schedule <on_time_ms> <off_time_ms>", parse_mode=ParseMode.MARKDOWN)
        return

    if action in ["ping", "on", "off"]:
        response = led_service.send_request(action)
    elif action == "schedule":
        on_time = callback_data[1]
        off_time = callback_data[2]
        response = led_service.send_request(action, on_time, off_time)
    else:
        raise ValueError(f"Invalid action: {action}")

    success, response_data = response

    if success:
        callback_query.answer("Status Updated. ✅")
        if callback_query.message.text != response_data.replace('*', ''):
            callback_query.message.edit_text(response_data, reply_markup=get_main_keyboard())
    else:
        callback_query.answer("Unable to connect to server. ❌")
