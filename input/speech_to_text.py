import speech_recognition as sr
from gtts import gTTS  # google text to speech
import playsound  # to play saved mp3 file
import os  # to save/open files


class STT():
    """
    Speech to Text
    """
    # init

    def __init__(self):
        pass

    def get_audio(self):
        # Declare speech recognition recognizer object
        rObject = sr.Recognizer()
        audio = ''

        with sr.Microphone() as source:
            rObject.adjust_for_ambient_noise(source)
            print("Speak...")

            # recording the audio using speech recognition
            # audio = rObject.listen(source, phrase_time_limit = 5)
            audio = rObject.listen(source)
        print("Stop.")  # limit 5 secs

        try:

            text = rObject.recognize_google(audio, language='en-US').lower()
            print("You : ", text)
            return text

        except:

            print(
                "Could not understand your audio, Please try again !")
            return ''

