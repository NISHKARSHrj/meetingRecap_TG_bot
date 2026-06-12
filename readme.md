# Meeting Recap Bot

A Telegram bot that helps users turn meeting voice notes into structured summaries using AI.

## Features

### Current Features

* `/start` command
* Receives voice messages from users
* Detects Telegram voice notes
* Displays voice note information such as:

  * Duration
  * File Size
  * File ID
* Beginner-friendly code structure
* Built using async Python

### Planned Features

* Speech-to-Text using OpenAI Whisper
* AI Meeting Summaries using OpenAI GPT
* Action Item Extraction
* Decision Tracking
* Follow-up Suggestions
* User Credit System
* Private Telegram Channel Archive
* Payment Integration for Additional Credits

## Commands

| Command    | Description                            |
| ---------- | -------------------------------------- |
| `/start`   | Start the bot and show welcome message |
| `/help`    | Display available commands             |
| `/balance` | Show remaining recap credits           |
| `/buy`     | Purchase additional recap credits      |

## Tech Stack

* Python 3
* python-telegram-bot
* OpenAI API
* python-dotenv

## Project Structure

meeting-recap-bot/

├── bot.py

├── .env

├── temp/

└── requirements.txt

## Installation

### Clone the Repository

```bash
git clone <your-repository-url>
cd meeting-recap-bot
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Linux / Fedora:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root.

```env
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
```

## Running the Bot

```bash
python bot.py
```

If everything is configured correctly, you should see:

```text
Bot is running...
```

## Learning Goals

This project was built as a learning project to understand:

* Telegram Bot Development
* Async Programming in Python
* Working with APIs
* AI Integration
* File Handling
* Prompt Engineering
* Error Handling
* Building Real-World Automation Tools

## Future Roadmap

### Version 1

* Basic Telegram Bot
* Voice Note Detection
* Command Handling

### Version 2

* Whisper Transcription
* GPT Summaries
* Credit System

### Version 3

* Voice Note Archive Channel
* Payment Integration
* User Dashboard

## Author

Built by Nishkarsh as a learning project to explore AI-powered productivity tools and Telegram bot development.
