from .assistantSpeaks import assistant_speaks
from .getAudio import get_audio

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