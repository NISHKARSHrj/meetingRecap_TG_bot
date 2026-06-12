import openai

import os
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

load_dotenv()

telegram_token = os.getenv("telegram_bot")
openai_key = os.getenv("openaikey")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to the Meeting Recap Bot! \n\n" 
        "Send me a message and I'll help you recap your meetings!"
    )

async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):

    voice = update.message.voice

    print("Duration:", voice.duration)
    print("File ID:", voice.file_id)
    print("Size:", voice.file_size)

    file = await context.bot.get_file(
        voice.file_id
    )
    await file.download_to_drive(
        "temp/voice_note.ogg"
    )
    await update.message.reply_text("Voice note received!")


def main():
    app = Application.builder().token(telegram_token).build()

    app.add_handler(
        CommandHandler("start", start)
    )
    app.add_handler(
        MessageHandler(filters.VOICE, handle_voice)
    )
    print("Bot is running...")

    app.run_polling()

if __name__ == "__main__":
    main()