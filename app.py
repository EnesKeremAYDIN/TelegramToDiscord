import os
import requests
from telethon import TelegramClient, events
from dotenv import load_dotenv

load_dotenv()
api_id = int(os.getenv('TELEGRAM_APP_ID'))
api_hash = os.getenv('TELEGRAM_APP_HASH')
phone_number = os.getenv('TELEGRAM_PHONE_NUMBER')
discord_webhook_url = os.getenv('OCHAIN_LOG_CHANNEL_WEHHOOK')
target_username = os.getenv('TARGET_USERNAME')

client = TelegramClient('TelegramToDiscord', api_id, api_hash)

def send_to_discord(content):
    data = {'content': content}
    response = requests.post(discord_webhook_url, json=data)
    if response.status_code == 204:
        print('Message sent to Discord.')
    else:
        print(f'Message could not be sent to Discord. Error: {response.status_code}')

@client.on(events.NewMessage)
async def handler(event):
    sender = await event.get_sender()
    if sender.username == target_username:
        message = event.message.message
        sender_name = f'{sender.first_name} {sender.last_name}' if sender.last_name else sender.first_name
        discord_message = f'{message}'
        send_to_discord(discord_message)

async def main():
    await client.start(phone=phone_number)
    print(f"I am listening to messages from user {target_username}.")
    await client.run_until_disconnected()

if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())
