from gtts import gTTS

testo = 'grazie al ca'

tts = gTTS(testo, lang='it')

tts.save('hello.mp3')