# importing speech recognition package from google api 
import speech_recognition as sr  
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files 
from tensorflow.keras.models import Sequential, load_model

from IntentClassifier.intent_classifier import predictions
from IntentClassifier.intent_classifier import get_final_output
from IntentClassifier.intent_classifier import unique_intent

from Speech.assistantSpeaks import assistant_speaks
from Speech.listening import listening
from Speech.wakeWord import wake_word
from Speech.getAudio import get_audio
from Speech.processInput import process_text


def textInput(text):
    WAKE_WORDS = ['text input'] 
    text = text.lower()  # Convert the text to all lower case words
  # Check to see if the users command/text contains a wake word    
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
  # If the wake word was not found return false
    return False


def process_text(input):
    try:
        if "who are you" in input or "define yourself" in input:
            speak = '''I am CS Helper. Virtual Office Assistant.
            I am here to answer your questions.'''
            assistant_speaks(speak)
            return

        elif "who made you" in input or "created you" in input:
            speak = "NMSU CS Students: Ari, Daniel, Cyrus, and Kay."
            assistant_speaks(speak)
            return

        elif 'open intent classifier' in input:

            intent_classifier(input.lower())
            return

        else:
            return
    except :

        assistant_speaks("I don't understand, Would you like to talk to a person?")
        ans = get_audio()
        if 'yes' in str(ans) or 'yeah' in str(ans):
            
            assistant_speaks("An office assistant will be in at ...")
            
def intent_classifier(input):
    if "intent" in input or "classifier" in input:
        assistant_speaks("Opening the intent classifier.")
        model = load_model("model.h5")
        assistant_speaks("What question would you like me to classify?")
        ans = get_audio()
        question = str(ans)
        pred = predictions(question)
        get_final_output(pred, unique_intent)
        
    else:
        assistant_speaks("Application not available.")
        return

  
# Driver Code 
if __name__ == "__main__":
    textFlag = False
    
    while(1): 
        # if (textFlag):
        #     textInput = input('How may I help you?')
        #     process_text(textInput)
        #     textFlag = False
        #     continue

        text = listening()
        # textFlag = textInput()
        print(wake_word(text))

        if (wake_word(text) == True):
  
            assistant_speaks("What can i do for you?") 
            text = get_audio().lower() 
    
            if text == 0: 
                assistant_speaks("Let me know if you need anything else") 
                continue
            
            if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text): 
                assistant_speaks("Ok bye") 
                break
            
            # calling process text to process the query 
            process_text(text) 
