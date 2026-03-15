import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import speech_recognition as sr
import os


def get_voice():
    fs = 44100  # Sample rate
    seconds = 5  # Duration
    filename = 'temp_audio.wav'

    try:
        print("Recording...")
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait()  # Wait until finished
        write(filename, fs, myrecording)

        r = sr.Recognizer()
        with sr.AudioFile(filename) as source:
            audio = r.record(source)
            text = r.recognize_google(audio)
            return text.lower()
    except Exception as e:
        print(f"Voice Error: {e}")
        return ""
    finally:
        if os.path.exists(filename): os.remove(filename)


def get_disease_info(disease):
    info_map = {
        "Fungal infection": {"precaution": "Keep skin dry and clean.", "specialist": "Dermatologist"},
        "Asthma": {"precaution": "Avoid dust and use inhaler.", "specialist": "Pulmonologist"},
        "Anxiety": {"precaution": "Practice deep breathing.", "specialist": "Psychiatrist"},
        "Acne": {"precaution": "Wash face twice daily.", "specialist": "Dermatologist"},
        "Unknown": {"precaution": "No info available.", "specialist": "General Physician"}
    }
    return info_map.get(disease, info_map["Unknown"])