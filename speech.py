from gtts import gTTS
import os 

text = "Haii hw are You"
output = gTTS(text=text,lang='en',slow=False)
output.save('output.mp3')
os.system('mpg321 output.mp3')
