import os
os.environ.setdefault('KMP_DUPLICATE_LIB_OK', 'TRUE')
os.environ.setdefault('HF_HUB_DISABLE_SYMLINKS_WARNING', '1')

# TTS Modules
import pyttsx3
from gtts import gTTS
from elevenlabs.client import ElevenLabs
from elevenlabs import stream

# Other
import pygame
import tempfile
import os
import sys
import io

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    # Fallback pentru versiuni Python mai învechite
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    except Exception:
        pass

def speak(text_to_procces="", 
          engine="gtts", 
          language='en', 
          elevenlabs_api_key="", 
          elevenlabs_voice_id='21m00Tcm4TlvDq8ikWAM', 
          elevenlabs_model_id='eleven_multilingual_v2'):

    # gTTS code
    if engine.lower() in ("gtts", 'google', 'free_online'):
        
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
            if language.lower() == 'auto':
                tts = gTTS(
                    text=text_to_procces, 
                    lang_check=True
                )

            else:
                tts = gTTS(
                    text=text_to_procces,
                    lang=language
                )

            tts.save(fp.name)
        
        pygame.mixer.init()
        pygame.mixer.music.load(fp.name)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass

        pygame.mixer.music.stop()
        pygame.mixer.quit()
        os.unlink(fp.name)


    # ElevenLabs code 
    elif engine.lower() in ("elevenlabs", "pay_online", "eleven labs"):
        

        client = ElevenLabs(api_key=elevenlabs_api_key)

        audio_stream = client.text_to_speech.stream(
            text=text_to_procces,
            voice_id=elevenlabs_voice_id,
            model_id=elevenlabs_model_id
        )

        stream(audio_stream)


    # pyttsx3 code
    elif engine.lower() in ("pyttsx3", "offline", "free offline"):
        
        engine_pyttsx3 = pyttsx3.init()
        engine_pyttsx3.say(text_to_procces)
        engine_pyttsx3.runAndWait()