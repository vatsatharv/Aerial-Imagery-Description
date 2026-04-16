from gtts import gTTS
import os

AUDIO_DIR = "uploads/audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

def generate_audio(text, image_id):
    file_path = os.path.join(AUDIO_DIR, f"{image_id}.mp3")

    tts = gTTS(text)
    tts.save(file_path)

    # ✅ Return public URL
    return f"http://127.0.0.1:8000/audio/{image_id}.mp3"