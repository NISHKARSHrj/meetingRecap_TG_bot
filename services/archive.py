from config import TG_channel_id

async def archive_audio(bot, file_path, username, timestamp):
    caption = (
        f"user: @{username}"
        f"times: {timestamp}"
    )

    with open(file_path, 'rb') as audio_file:
        await bot.send_document(
            chat_id=TG_channel_id,
            document=audio_file,
            caption=caption
        )