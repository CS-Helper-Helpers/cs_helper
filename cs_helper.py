# importing speech recognition package from google api 
import speech_recognition as sr  
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files 
from selenium import webdriver # to control browser operations 
from tensorflow.keras.models import Sequential, load_model

from intent_classifier import predictions
from intent_classifier import get_final_output
from intent_classifier import unique_intent

num = 1
"""num: used to rename every audio file to remove ambiguity  
"""

def assistant_speaks(output):
    """Speaking function to output audio file

    Args:
        output (IDK TYPE): The first parameter.

    Returns:
        None
        
    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    """    
    global num 
    num += 1    # Increase counter for successive audio file creation

    # Debug
    print("Person : ", output) 
  
    # Create gTTS instance 
    toSpeak = gTTS(text = output, lang ='en', slow = False)

    # Save the audio file given by Google Text to Speech
    file = str(num)+".mp3"  
    toSpeak.save(file) 
      
    # Playsound package is used to play the same file. 
    playsound.playsound(file, True)  
    os.remove(file) 
  
def wakeWord(text):
    WAKE_WORDS = ['ai have a question', 'hey c s helper', 'okay computer', 'hey i have a question'] 
    text = text.lower()  # Convert the text to all lower case words
  # Check to see if the users command/text contains a wake word    
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
  # If the wake word was not found return false
    return False

def textInput(text):
    WAKE_WORDS = ['text input'] 
    text = text.lower()  # Convert the text to all lower case words
  # Check to see if the users command/text contains a wake word    
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
  # If the wake word was not found return false
    return False
  
def get_audio(): 
    """get_audio gets the audio


    Returns:

    Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions
            that are relevant to the interface.
        ValueError: If `param2` is equal to `param1`.

    """
    # Declare speech recognition recognizer object  
    rObject = sr.Recognizer() 
    audio = '' 
  
    with sr.Microphone() as source: 
        print("Speak...") 
          
        # recording the audio using speech recognition 
        audio = rObject.listen(source, phrase_time_limit = 5)  
    print("Stop.") # limit 5 secs 
  
    try: 
  
        text = rObject.recognize_google(audio, language ='en-US') 
        print("You : ", text) 
        return text 
  
    except: 
  
        assistant_speaks("Could not understand your audio, PLease try again !") 
        return ''

def listening(): 
    """get_audio gets the audio


    Returns:

    Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions
            that are relevant to the interface.
        ValueError: If `param2` is equal to `param1`.

    """
    # Declare speech recognition recognizer object  
    rObject = sr.Recognizer() 
    audio = '' 
  
    with sr.Microphone() as source: 
        print("Listening...") 
          
        # recording the audio using speech recognition 
        audio = rObject.listen(source, phrase_time_limit = 5)  
  
    try: 
  
        text = rObject.recognize_google(audio, language ='en-US') 
        print("You : ", text) 
        return text 
  
    except: 
        return ''

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
        if (textFlag):
            textInput = input('How may I help you?')
            process_text(textInput)
            textFlag = False
            continue

        text = listening()
        textFlag = textInput()
        print(wakeWord(text))

        if (wakeWord(text) == True):
  
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
