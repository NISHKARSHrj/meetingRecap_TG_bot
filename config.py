import os
from dotenv import load_dotenv

load_dotenv()

Bot_token = os.getenv("telegram_bot")
Openrouter_key = os.getenv("openrouter_key")
TG_channel_id = os.getenv("tg_channel_id")
Deepseek_model = os.getenv("deepseek_model")
path = os.getenv("path")