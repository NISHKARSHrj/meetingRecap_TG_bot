import openai

import os
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from datetime import datetime


load_dotenv()

# telegram token
telegram_token = os.getenv("telegram_bot")

# gpt token
openai_key = os.getenv("openaikey")


# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to the Meeting Recap Bot! \n\n" 
        "Send me a message and I'll help you recap your meetings!"
    )

# voice handling
async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):

    voice = update.message.voice

    file = await context.bot.get_file(
        voice.file_id
    )
    username = update.effective_user.username or "unknown"
    message_time = update.message.date
    timestamp = message_time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"temp/{username}_{timestamp}.ogg"
    # print(username) for debugging
    
    # download file
    await file.download_to_drive(
        filename
    )

    await update.message.reply_text("Voice note received!")

# main function to run the app
def main():
    app = Application.builder().token(telegram_token).build()


    # handle the /start command
    app.add_handler(
        CommandHandler("start", start)
    )
    # handle voice messages
    app.add_handler(
        MessageHandler(filters.VOICE, handle_voice)
    )

    print("Bot is running...")

    app.run_polling()

if __name__ == "__main__":
    main()