import speech_recognition as sr  


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