from openai import OpenAI
from config import Openrouter_key

client = OpenAI(
    api_key=Openrouter_key,
    base_url="https://openrouter.ai/api/v1"
)
def generate_summary(transcript: str) -> str:
    prompt = f"""
    You are a meeting assistant powered by AI.

    Review the following meeting transcript and create a structured summary of the meeting.

    Follow the template below:

    🎯 Action Items
    - ...

    💡 Decisions
    - ...

    📌 Follow-up
    - ...

    If there is nothing in a particular section, write "None".

    Transcript:

    {transcript}
    """
    response = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3",
        messages=[
            {
                "role": "system",
                "content": "You are an expert meeting assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content