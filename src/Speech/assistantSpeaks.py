from gtts import gTTS # google text to speech 
import playsound # to play saved mp3 file 
import os # to save/open files 

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
    print("CS Helper : ", output) 
  
    # Create gTTS instance 
    toSpeak = gTTS(text = output, lang ='en', slow = False)

    # Save the audio file given by Google Text to Speech
    file = str(num)+".mp3"  
    toSpeak.save(file) 
      
    # Playsound package is used to play the same file. 
    playsound.playsound(file, True)  
    os.remove(file)