from gtts import gTTS
import os 
from tkinter import *

root= Tk()
canvas = Canvas(root,width=400,height=400)
canvas.pack()
def texttospeech():
    text=entry.get()
    output= gTTS(text=text,lang='en',slow=False)
    output.save('output.mp4')
    os.system('start output.mp4')    
entry =Entry(root)
canvas.create_window(200,180,window=entry )
button= Button(text="start",command=texttospeech)
canvas.create_window(300,180,window=button )
root.mainloop()



