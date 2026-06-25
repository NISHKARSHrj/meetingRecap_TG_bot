from telegram import Update
from telegram.ext import ContextTypes

from datetime import datetime
from services.archive import archive_audio

async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    if update.message.voice:
        telegram_file = update.message.voice
        extension = ".ogg"

    elif update.message.audio:
        telegram_file = update.message.audio
        extension = ".mp3"

    elif update.message.document:
        telegram_file = update.message.document
        filename = telegram_file.file_name
        extension = filename.split(".")[-1]

    else:
        await update.message.reply_text("❌ Please send a voice message, audio file, or document.")
        return
    
    file = await context.bot.get_file(
        telegram_file.file_id
    )
    save_path = f"temp/audio.{extension}"

    await file.download_to_drive(save_path)

    await archive_audio(
        bot=context.bot,
        file_path=save_path,
        username=update.effective_user.username or 'unknown',
        timestamp=update.message.date.strftime("%Y-%m-%d_%H-%M-%S")
    )

    await update.message.reply_text("✅ Audio downloaded successfully!")
    # voice = update.message.document

    # file = await context.bot.get_file(
    #     voice.file_id
    # )
    # username = update.effective_user.username or 'unknown'

    # timestamp = update.message.date.strftime(
    #     "%Y-%m-%d_%H-%M-%S"
    # )
    # filename = f"temp/{username}_{timestamp}.ogg"

    # await file.download_to_drive(filename)
    # print(f"Voice message saved as {filename}")
    # await update.message.reply_text("✅ Voice downloaded successfully!")