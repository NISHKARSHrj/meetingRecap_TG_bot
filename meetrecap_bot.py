import openai

import os
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()

telegram_token = os.getenv("telegram_bot")
openai_key = os.getenv("openaikey")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to the Meeting Recap Bot! \n\n" 
        "Send me a message and I'll help you recap your meetings!"
    )

def main():
    app = Application.builder().token(telegram_token).build()

    app.add_handler(
        CommandHandler("start", start)
    )
    print("Bot is running...")

    app.run_polling()

if __name__ == "__main__":
    main()