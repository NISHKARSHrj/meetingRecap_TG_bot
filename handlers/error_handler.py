from telegram import Update
from telegram.ext import ContextTypes

from utils.logger import logger


async def error_handler(
    update: object,
    context: ContextTypes.DEFAULT_TYPE
):

    logger.exception(context.error)

    if isinstance(update, Update):

        try:

            await update.effective_message.reply_text(
                "❌ Something went wrong.\nPlease try again."
            )

        except Exception:

            pass