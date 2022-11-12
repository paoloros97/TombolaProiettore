
from gtts import gTTS

language = 'en'

for i in range(1,91):
    testo = str(i)
    myobj = gTTS(text=testo, lang=language, slow=False, )
    nomeFile = 'numeriSintenticiEng/' + testo + '.mp3'
    myobj.save(nomeFile)