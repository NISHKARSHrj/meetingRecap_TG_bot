from pathlib import Path
from telegram import Update
from telegram.ext import ContextTypes

from datetime import datetime

from services.archive import archive_audio
from services.transcriber import transcribe_audio
from services.summarizer import generate_summary
async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    if update.message.voice:
        telegram_file = update.message.voice
        extension = "ogg"

    elif update.message.audio:
        telegram_file = update.message.audio
        extension = "mp3"

    elif update.message.document:
        telegram_file = update.message.document
        filename = telegram_file.file_name
        extension = filename.split(".")[-1]

    else:
        await update.message.reply_text("❌ Unsupported file.")
        return
    
    file = await context.bot.get_file(
        telegram_file.file_id
    )
    
    username = update.effective_user.username or "unknown"

    timestamp = update.message.date.strftime(
        "%Y-%m-%d_%H-%M-%S"
    )
    save_path = f"temp/{username}_{timestamp}.{extension}"

    await file.download_to_drive(save_path)
    processing = await update.message.reply_text(
        "🎙️ Audio received.\n\n⏳ Processing..."
    )
    print(f"Audio saved to {save_path}")
    await archive_audio(
        bot=context.bot,
        file_path=save_path,
        username=username,
        timestamp=timestamp
    )
    try:
        await processing.edit_text(
            "📝 Transcribing audio..."
        )

        transcript = transcribe_audio(save_path)
        print(transcript)
        await processing.edit_text(
            "🧠 Generating meeting summary..."
        )

        summary = generate_summary(transcript)
        
        await update.message.reply_text(summary)
    except Exception as e:
        print(e)
        await update.message.reply_text("❌ Error occurred while processing the audio.")

    finally:

        # -------- Cleanup -------- #

        try:
            Path(save_path).unlink(missing_ok=True)
            print("🗑 Temporary file deleted.")
        except Exception as cleanup_error:
            print(cleanup_error)