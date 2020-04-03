import tkinter as tk

from cs_helper import *

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

def getText ():  
    x1 = entry1.get()
    text = True
    label1 = tk.Label(root, text= x1)
    canvas1.create_window(200, 230, window=label1)
    return text, x1

button1 = tk.Button(text='Submit', command=getText)
canvas1.create_window(200, 180, window=button1)

text = False
    
while(1): 
    if (text):
        textInput = input('How may I help you?')
        process_text(textInput)
        text = False
        continue
    text = listening()
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
root.mainloop()