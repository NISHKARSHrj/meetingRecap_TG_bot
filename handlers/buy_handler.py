from telegram import Update
from telegram.ext import ContextTypes


async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    await update.message.reply_text(
        """
🚀 Premium Plans

10 Credits  → ₹99

50 Credits  → ₹299

Payments coming soon.

Stay tuned ❤️
"""
    )