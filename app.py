import os
import requests
from telethon import TelegramClient, events
from dotenv import load_dotenv

load_dotenv()
api_id = int(os.getenv('TELEGRAM_APP_ID'))
api_hash = os.getenv('TELEGRAM_APP_HASH'))
phone_number = os.getenv('TELEGRAM_PHONE_NUMBER'))
discord_webhook_url = os.getenv('DISCORD_WEHHOOK'))
target_username = os.getenv('TARGET_USERNAME')

client = TelegramClient('DiscordBot', api_id, api_hash)

async def send_to_discord(content):
    data = {'content': content}
    response = requests.post(discord_webhook_url, json=data)
    if response.status_code == 204:
        print('Message successfully sent to Discord.')
    else:
        print(f'Failed to send message to Discord. Error: {response.status_code}')

@client.on(events.NewMessage)
async def handler(event):
    sender = await event.get_sender()
    if sender is not None and sender.username == target_username:
        message = event.message.message
        await send_to_discord(message)

async def main():
    print('Starting Telegram client.')
    await client.start(phone=phone_number)
    print(f"Listening for messages from {target_username}...")
    try:
        await client.run_until_disconnected()
    except Exception as e:
        print(f'Telegram connection error: {e}')

if __name__ == '__main__':
    print('Bot started.')
    client.loop.run_until_complete(main())
