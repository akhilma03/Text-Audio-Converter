from gtts import gTTS
import os 

text = open('text.txt','r',encoding='utf-8').read()
language =  'hi'
output= gTTS(text=text,lang=language,slow=False)
output.save('fileoutput.mp4')
os.system('start fileoutput.mp4')