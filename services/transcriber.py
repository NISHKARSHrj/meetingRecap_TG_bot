from faster_whisper import WhisperModel


model = WhisperModel(
    "base",
    compute_type="int8"
)

def transcribe_audio(file_path: str) -> str:
    segments, info = model.transcribe(file_path, language="hi")
    transcript = ""

    for segment in segments:
        transcript += segment.text + " "

    return transcript.strip()
