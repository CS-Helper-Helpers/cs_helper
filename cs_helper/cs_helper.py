import speech_recognition as sr
import playsound
from gtts import gTTS
import os
from tensorflow.keras.models import Sequential, load_model
from input.speech_to_text import STT
from input.text_to_speech import TTS
from input.text_to_text import TTT
from input.wakeword import wake_word

import threading

text = ""


def speechfunc():

    global text
    stt = STT()
    tts = TTS()

    while 1:
        text = stt.get_audio()

        if wake_word(text) == True:
            tts.assistant_speaks("How may I help you?")
            text = stt.get_audio()
            inputType = "speech"
            print(text, inputType)


def textfunc():

    global text
    ttt = TTT()

    while 1:
        text = ttt.get_input()
        inputType = "text"
        print(text, inputType)


if __name__ == "__main__":

    # Add a lock so this runs first
    speech_thread = threading.Thread(target=speechfunc)
    text_thread = threading.Thread(target=textfunc)
    text_thread.start()
    speech_thread.start()

    # Then this
    print("Text: ", text)
