from pyrogram import Client, filters

from config import API_ID, API_HASH, BOT_TOKEN, PROXY
from handlers import callbacks, commands

app = Client("led_ctrl_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, proxy=PROXY)

app.on_message(filters.command('start'))(commands.start)
app.on_message(filters.command('schedule'))(commands.schedule)

app.on_callback_query(filters.regex(r"^(ping|on|off|schedule)"))(callbacks.handle_callback_query)

if __name__ == "__main__":
    print('bot is running...')
    app.run()
