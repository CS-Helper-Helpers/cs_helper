import threading
from Speech.getAudio import get_audio
from Speech.assistantSpeaks import assistant_speaks
from Speech.listening import listening
from Speech.wakeWord import wake_word
from Speech.getAudio import get_audio
from ProcessInput.processInput import process_text

def speechfunc():
    while(1): 
        text = listening()
        # print(wake_word(text))
        if (wake_word(text) == True):
            assistant_speaks("What can i do for you?") 
            text = get_audio().lower()
            inputType = 'speech'
            process_text(text, inputType)

def textfunc():
    while(1):
        text = input("How may I help you?") 
        inputType = 'text'   
        process_text(text, inputType)

if __name__ == "__main__":
    speech = threading.Thread(target = speechfunc)
    text = threading.Thread(target = textfunc)
    text.start()
    speech.start()