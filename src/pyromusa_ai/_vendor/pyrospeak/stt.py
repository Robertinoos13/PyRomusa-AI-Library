import os
os.environ.setdefault('KMP_DUPLICATE_LIB_OK', 'TRUE')
os.environ.setdefault('HF_HUB_DISABLE_SYMLINKS_WARNING', '1')

# STT Modules
from faststt import FastSTT
import whisper

# Other Modules
import logging
import sounddevice as sd
import numpy as np

def record(engine="faststt", 
           faststt_model_size="base", 
           faststt_device="CPU", 
           faststt_timeout=3,
           faststt_phrase_time_limit=5,
           whisper_seconds=5,
           whisper_samplerate=16000,
           whisper_name="base",
           whisper_device="cpu"):

    # FastSTT code
    if engine.lower() in ("faststt"):

        logging.basicConfig(level=logging.INFO)

        stt = FastSTT(
            model_size=faststt_model_size.lower(), 
            device=faststt_device.lower()
            )
        
        print("Listening...")

        try:
            text = stt.listen_and_transcribe(timeout=faststt_timeout, phrase_time_limit=faststt_phrase_time_limit)
            if text and isinstance(text, dict):
                print("Transcription:", text["text"])
            else:
                print("...no speech detected")

        except KeyboardInterrupt:
            print("\nStopped by user")

        except Exception as e:
            pass

        result = text
        return result["text"] if isinstance(result, dict) else result
    

    # Whisper code
    elif engine.lower() in ("whisper"):
        print(f"Listening for {whisper_seconds} seconds. Speak...")
        model = whisper.load_model(name=whisper_name.lower(), device=whisper_device.lower())
    
        # Înregistrare direct în memorie: float32 (formatul cerut de Whisper)
        audio = sd.rec(int(whisper_seconds * whisper_samplerate), samplerate=whisper_samplerate, channels=1, dtype=np.float32)
        sd.wait() # Așteaptă finalizarea înregistrării

        # Transcrierea directă a array-ului aplatizat (1D)
        return model.transcribe(audio.flatten())["text"]