import tkinter as tk

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

root.mainloop()