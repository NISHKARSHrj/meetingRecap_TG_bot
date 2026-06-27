from telegram import Update
from telegram.ext import ContextTypes


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    help_text = """
🤖 Meeting Recap Bot

Send me a voice message, MP3, or WAV file and I'll generate an AI-powered meeting summary.

📋 Available Commands

/start
Welcome message

/help
Show this help menu

/balance
Check your remaining credits

/buy
Purchase more credits

━━━━━━━━━━━━━━

🎙 Supported Formats

• Voice Notes (.ogg)
• MP3 Audio
• WAV Audio

━━━━━━━━━━━━━━

🧠 What I Do

1. Convert speech to text
2. Generate an AI meeting recap
3. Extract:
   🎯 Action Items
   💡 Decisions
   📌 Follow-up

Happy Recapping! 🚀
"""

    await update.message.reply_text(help_text)