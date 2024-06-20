# LED Controller Telegram Bot

## Setup
Create `.env` file in `src` directory:
```
API_ID=<your-api-id>
API_HASH=<your-api-hash>
BOT_TOKEN=<your-bot-token>
PROXY_SCHEME=socks5
PROXY_HOSTNAME=127.0.0.1
PROXY_PORT=10808
SERVER_API_URL=http://your-server-api/led
```

## Running the Bot Manually
1. Install the required dependencies:
```
pip install -r requirements.txt
```
2. Start the bot:
```
python bot.py
```

## Running the Bot with Docker
1. Update the `PROXY_HOSTNAME` value in the `.env` file to `host.docker.internal`:
```
PROXY_HOSTNAME=host.docker.internal
```
2. Build the Docker image:
```
docker build -t led-ctrl-bot .
```
3. Run the Docker container:
```
docker run --env-file .env led-tg-bot 
```
