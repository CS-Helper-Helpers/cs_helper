def wake_word(text):
    WAKE_WORDS = ['a i have a question', 'hey c s helper', 'okay computer', 'i have a question', 'helper'] 
    text = text.lower()  # Convert the text to all lower case words
  # Check to see if the users command/text contains a wake word    
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
  # If the wake word was not found return false
    return False