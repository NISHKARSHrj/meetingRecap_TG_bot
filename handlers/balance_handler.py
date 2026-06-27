from telegram import Update
from telegram.ext import ContextTypes

from services.credits import get_balance


async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):

    credits = get_balance(update.effective_user.id)

    await update.message.reply_text(
        f"""
        💳 Your Credits

        📊 Your current credit balance is: {credits}

        Free Credits : 3 Credits
        """
    )