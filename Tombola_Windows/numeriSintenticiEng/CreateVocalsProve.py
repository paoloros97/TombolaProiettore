from gtts import gTTS

testo = 'grazie al cazzo'

tts = gTTS(testo, lang='it')

tts.save('hello.mp3')