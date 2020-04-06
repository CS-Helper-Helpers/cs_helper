# importing speech recognition package from google api 
import speech_recognition as sr  
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files 
from tensorflow.keras.models import Sequential, load_model



#from Speech.assistantSpeaks import assistant_speaks
#from Speech.listening import listening
#from Speech.wakeWord import wake_word
#from Speech.getAudio import get_audio
#from Speech.processInput import process_text

from input.speech_to_text import STT
from input.text_to_speech import TTS
from input.text_to_text import TTT
from input.wakeword import wake_word

import threading

def speechfunc():
    stt = STT()
    tts = TTS()

    while(1): 
        text = stt.get_audio()
        
        if (wake_word(text) == True):
            tts.assistant_speaks("How may I help you?") 
            text = stt.get_audio()
            inputType = 'speech'
            print(text, inputType)

def textfunc():
    ttt = TTT()

    while(1):
        text = ttt.get_input() 
        inputType = 'text'   
        print(text, inputType)

if __name__ == "__main__":
    speech = threading.Thread(target = speechfunc)
    text = threading.Thread(target = textfunc)
    text.start()
    speech.start()
