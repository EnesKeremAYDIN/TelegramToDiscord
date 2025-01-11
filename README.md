# Telegram to Discord Bridge

A Python-based bot that forwards messages from a Telegram chat to a Discord channel, enabling seamless communication between the two platforms.

## Features

- Forwards messages from a specified Telegram chat to a Discord channel.
- Uses environment variables for secure configuration.

## Installation and Setup

### Prerequisites

- **Python 3.x** installed on your machine.
- **Telegram Bot API Token** and **Discord Webhook URL**.

### Installation

1. **Clone or Download** this repository:
   ```bash
   git clone https://github.com/EnesKeremAYDIN/TelegramToDiscord.git
   cd TelegramToDiscord
   ```

2. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. **Set Up Environment Variables**:
   - Open the `.env` file and configure the following values:
     - `TELEGRAM_API_TOKEN`: Your Telegram Bot API Token.
     - `DISCORD_WEBHOOK_URL`: The Discord Webhook URL for the target channel.

### Running the Bot

Start the bot by running:
```bash
python app.py
```

## Files

- **`app.py`**: Main script that handles message forwarding from Telegram to Discord.
- **`.env`**: Stores configuration values securely.

## Disclaimer

This tool is intended for personal or small community use. Ensure compliance with the terms of service of both Telegram and Discord when using this bot.
