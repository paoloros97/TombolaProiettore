from pygame import mixer
import time

#Instantiate mixer
mixer.init()
mixer.music.set_volume(1)

for i in range(70,91):
    nomeFile = 'numeriSintentici/' + str(i) + '.mp3'
    mixer.music.load(nomeFile)
    print(str(i) + '.mp3')
    mixer.music.play()
    time.sleep(1.5)    
