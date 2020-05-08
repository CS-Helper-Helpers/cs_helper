import os
import threading

import speech_recognition as sr
import playsound
from gtts import gTTS
from tensorflow.keras.models import Sequential, load_model

from input.speech_to_text import STT
from input.text_to_speech import TTS
from input.text_to_text import TTT
from input.wakeword import wake_word
from intent_classifier.intent_classifier import IntentClassifier

# from gui import cshelpergui as ui
# from kivy.app import App
# from kivy.uix.widget import Widget
# from kivy.vector import Vector
# from kivy.core.window import Window
# from kivy.uix.screenmanager import ScreenManager, Screen
# import gui.cshelpergui as ui

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

            print(text)
            answer = corefunc()
            print(answer)
            tts.assistant_speaks(answer)


def textfunc():

    global text
    ttt = TTT()
    # maingui()
    # while 1:
    #     text = ttt.get_input()
    #     inputType = "text"
    #     print(text, inputType)
    #     answer = corefunc()
    #     print(answer)


def corefunc():
    """ Returns answer from database """
    global text

    ic = IntentClassifier()
    return ic.answer(text)


def startThreads():
    # if __name__ == "__main__":

    loaded = load_model("intent_classifier/model.h5")

    # Add a lock so this runs first
    speech_thread = threading.Thread(target=speechfunc)
    # text_thread = threading.Thread(target=textfunc)
    # text_thread.start()
    speech_thread.start()

    # print("Text: ", text)
