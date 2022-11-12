# Import the required module for text 
# to speech conversion
from gtts import gTTS

# This module is imported so that we can 
# play the converted audio
#import os

# The text that you want to convert to audio
#mytext = '1. L\'italia.'
mytext = '33. L\'anni de Cristo.'
  
# Language in which you want to convert
language = 'it'
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
  
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("numeriSintentici/welcome.mp3")
  
# Playing the converted file
#os.system("welcome.mp3")

for i in range(1,91):
    testo = str(i)
    myobj = gTTS(text=testo, lang=language, slow=False, )
    nomeFile = 'numeriSintentici/' + testo + '.mp3'
    myobj.save(nomeFile)