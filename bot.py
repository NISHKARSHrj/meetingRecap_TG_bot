from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import Bot_token

from handlers.start_handler import start
from handlers.voice_handler import handle_voice
def main():
    app = Application.builder().token(Bot_token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Document.ALL| filters.VOICE| filters.AUDIO, handle_voice))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()