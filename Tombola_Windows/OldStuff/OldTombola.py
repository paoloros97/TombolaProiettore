from tkinter import *
from tkinter import font as tkFont
import random

#___ PARAMETRI DA MODIFICARE___
grandezzaFont = 60 # Cambiare per ingrandire o rimpicciolire i numeri
famigliaFont = "" # Oppure , Times, Courier
coloreEstratto = "#3cff00"
coloreBase = "#ffffff"
#___ FINE PARAMETRI DA MODIFICARE___

# Genera un array causale di 90 numeri da 0 a 89 (ovvero gli indici)
giocata = random.sample(range(90), 90) 

print("Numeri estratti:")

#"posizione" serve per scorrere l'array dei NumeriEstratti
posizione = 0 

# Finestra tabellone
root = Tk()
root.title('Tabellone Tombola')
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
root.geometry ("%dx%d"%(window_width,window_height))

helv36 = tkFont.Font(family = famigliaFont, size = grandezzaFont, weight=tkFont.BOLD)

def Estrai():
    global posizione

    if posizione == 90:
        status_label.config(text = "Fine")
        print("Fine") # Tabellone completo
        print("")
        return

    indice = giocata[posizione]
    print(indice + 1)
    
    if indice < 10: 
        d = "changeColor0" + str(indice)
    else:
        d = "changeColor" + str(indice)

    globals()[d]() # "Preme" il pulsante corrispondente
    
    status_label.config(text = str(indice + 1))

    posizione += 1 #Pronto per il successivo

def schermoIntero():
    root.attributes("-fullscreen", True)
    
def Spoiler():
    global giocata
    NumeriEstratti = [x+1 for x in giocata] 
    print(NumeriEstratti)
    
def Ricomincia():
    global giocata
    global posizione
    print("Numeri estratti:")
    giocata = random.sample(range(90), 90)
    
    posizione = 0 
    status_label.config(text = "Numero estratto")
    button_0_0["bg"] = coloreBase
    button_0_1["bg"] = coloreBase
    button_0_2["bg"] = coloreBase
    button_0_3["bg"] = coloreBase
    button_0_4["bg"] = coloreBase
    button_0_5["bg"] = coloreBase
    button_0_6["bg"] = coloreBase
    button_0_7["bg"] = coloreBase
    button_0_8["bg"] = coloreBase
    button_0_9["bg"] = coloreBase
    button_1_0["bg"] = coloreBase
    button_1_1["bg"] = coloreBase
    button_1_2["bg"] = coloreBase
    button_1_3["bg"] = coloreBase
    button_1_4["bg"] = coloreBase
    button_1_5["bg"] = coloreBase
    button_1_6["bg"] = coloreBase
    button_1_7["bg"] = coloreBase
    button_1_8["bg"] = coloreBase
    button_1_9["bg"] = coloreBase
    button_2_0["bg"] = coloreBase
    button_2_1["bg"] = coloreBase
    button_2_2["bg"] = coloreBase
    button_2_3["bg"] = coloreBase
    button_2_4["bg"] = coloreBase
    button_2_5["bg"] = coloreBase
    button_2_6["bg"] = coloreBase
    button_2_7["bg"] = coloreBase
    button_2_8["bg"] = coloreBase
    button_2_9["bg"] = coloreBase
    button_3_0["bg"] = coloreBase
    button_3_1["bg"] = coloreBase
    button_3_2["bg"] = coloreBase
    button_3_3["bg"] = coloreBase
    button_3_4["bg"] = coloreBase
    button_3_5["bg"] = coloreBase
    button_3_6["bg"] = coloreBase
    button_3_7["bg"] = coloreBase
    button_3_8["bg"] = coloreBase
    button_3_9["bg"] = coloreBase
    button_4_0["bg"] = coloreBase
    button_4_1["bg"] = coloreBase
    button_4_2["bg"] = coloreBase
    button_4_3["bg"] = coloreBase
    button_4_4["bg"] = coloreBase
    button_4_5["bg"] = coloreBase
    button_4_6["bg"] = coloreBase
    button_4_7["bg"] = coloreBase
    button_4_8["bg"] = coloreBase
    button_4_9["bg"] = coloreBase
    button_5_0["bg"] = coloreBase
    button_5_1["bg"] = coloreBase
    button_5_2["bg"] = coloreBase
    button_5_3["bg"] = coloreBase
    button_5_4["bg"] = coloreBase
    button_5_5["bg"] = coloreBase
    button_5_6["bg"] = coloreBase
    button_5_7["bg"] = coloreBase
    button_5_8["bg"] = coloreBase
    button_5_9["bg"] = coloreBase
    button_6_0["bg"] = coloreBase
    button_6_1["bg"] = coloreBase
    button_6_2["bg"] = coloreBase
    button_6_3["bg"] = coloreBase
    button_6_4["bg"] = coloreBase
    button_6_5["bg"] = coloreBase
    button_6_6["bg"] = coloreBase
    button_6_7["bg"] = coloreBase
    button_6_8["bg"] = coloreBase
    button_6_9["bg"] = coloreBase
    button_7_0["bg"] = coloreBase
    button_7_1["bg"] = coloreBase
    button_7_2["bg"] = coloreBase
    button_7_3["bg"] = coloreBase
    button_7_4["bg"] = coloreBase
    button_7_5["bg"] = coloreBase
    button_7_6["bg"] = coloreBase
    button_7_7["bg"] = coloreBase
    button_7_8["bg"] = coloreBase
    button_7_9["bg"] = coloreBase
    button_8_0["bg"] = coloreBase
    button_8_1["bg"] = coloreBase
    button_8_2["bg"] = coloreBase
    button_8_3["bg"] = coloreBase
    button_8_4["bg"] = coloreBase
    button_8_5["bg"] = coloreBase
    button_8_6["bg"] = coloreBase
    button_8_7["bg"] = coloreBase
    button_8_8["bg"] = coloreBase
    button_8_9["bg"] = coloreBase
    
    
def ChiudiTutto():
    root.quit()
    root2.quit()

def changeColor00():
    global coloreEstratto 
    global coloreBase
    if button_0_0.cget('bg') == coloreBase:
        button_0_0["bg"] = coloreEstratto
        #playsound('numerivocali/1.mp3', False)
    else:
        button_0_0["bg"] = coloreBase
def changeColor01():
    global coloreEstratto 
    global coloreBase
    if button_0_1.cget('bg') == coloreBase:
        button_0_1["bg"] = coloreEstratto
        #playsound('numerivocali/2.mp3', False)
    else:
        button_0_1["bg"] = coloreBase
def changeColor02():
    global coloreEstratto 
    global coloreBase
    if button_0_2.cget('bg') == coloreBase:
        button_0_2["bg"] = coloreEstratto
        #playsound('numerivocali/3.mp3', False)
    else:
        button_0_2["bg"] = coloreBase
def changeColor03():
    global coloreEstratto 
    global coloreBase
    if button_0_3.cget('bg') == coloreBase:
        button_0_3["bg"] = coloreEstratto
        #playsound('numerivocali/4.mp3', False)
    else:
        button_0_3["bg"] = coloreBase
def changeColor04():
    global coloreEstratto 
    global coloreBase
    if button_0_4.cget('bg') == coloreBase:
        button_0_4["bg"] = coloreEstratto
        #playsound('numerivocali/5.mp3', False)
    else:
        button_0_4["bg"] = coloreBase
def changeColor05():
    global coloreEstratto 
    global coloreBase
    if button_0_5.cget('bg') == coloreBase:
        button_0_5["bg"] = coloreEstratto
        #playsound('numerivocali/6.mp3', False)
    else:
        button_0_5["bg"] = coloreBase
def changeColor06():
    global coloreEstratto 
    global coloreBase
    if button_0_6.cget('bg') == coloreBase:
        button_0_6["bg"] = coloreEstratto
        #playsound('numerivocali/7.mp3', False)
    else:
        button_0_6["bg"] = coloreBase
def changeColor07():
    global coloreEstratto 
    global coloreBase
    if button_0_7.cget('bg') == coloreBase:
        button_0_7["bg"] = coloreEstratto
        #playsound('numerivocali/8.mp3', False)
    else:
        button_0_7["bg"] = coloreBase
def changeColor08():
    global coloreEstratto 
    global coloreBase
    if button_0_8.cget('bg') == coloreBase:
        button_0_8["bg"] = coloreEstratto
        #playsound('numerivocali/9.mp3', False)
    else:
        button_0_8["bg"] = coloreBase
def changeColor09():
    global coloreEstratto 
    global coloreBase
    if button_0_9.cget('bg') == coloreBase:
        button_0_9["bg"] = coloreEstratto
        #playsound('numerivocali/10.mp3', False)
    else:
        button_0_9["bg"] = coloreBase
def changeColor10():
    global coloreEstratto 
    global coloreBase
    if button_1_0.cget('bg') == coloreBase:
        button_1_0["bg"] = coloreEstratto
        #playsound('numerivocali/11.mp3', False)
    else:
        button_1_0["bg"] = coloreBase
def changeColor11():
    global coloreEstratto 
    global coloreBase
    if button_1_1.cget('bg') == coloreBase:
        button_1_1["bg"] = coloreEstratto
        #playsound('numerivocali/12.mp3', False)
    else:
        button_1_1["bg"] = coloreBase
def changeColor12():
    global coloreEstratto 
    global coloreBase
    if button_1_2.cget('bg') == coloreBase:
        button_1_2["bg"] = coloreEstratto
        #playsound('numerivocali/13.mp3', False)
    else:
        button_1_2["bg"] = coloreBase
def changeColor13():
    global coloreEstratto 
    global coloreBase
    if button_1_3.cget('bg') == coloreBase:
        button_1_3["bg"] = coloreEstratto
        #playsound('numerivocali/14.mp3', False)
    else:
        button_1_3["bg"] = coloreBase
def changeColor14():
    global coloreEstratto 
    global coloreBase
    if button_1_4.cget('bg') == coloreBase:
        button_1_4["bg"] = coloreEstratto
        #playsound('numerivocali/15.mp3', False)
    else:
        button_1_4["bg"] = coloreBase
def changeColor15():
    global coloreEstratto 
    global coloreBase
    if button_1_5.cget('bg') == coloreBase:
        button_1_5["bg"] = coloreEstratto
        #playsound('numerivocali/16.mp3', False)
    else:
        button_1_5["bg"] = coloreBase
def changeColor16():
    global coloreEstratto 
    global coloreBase
    if button_1_6.cget('bg') == coloreBase:
        button_1_6["bg"] = coloreEstratto
        #playsound('numerivocali/17.mp3', False)
    else:
        button_1_6["bg"] = coloreBase
def changeColor17():
    global coloreEstratto 
    global coloreBase
    if button_1_7.cget('bg') == coloreBase:
        button_1_7["bg"] = coloreEstratto
        #playsound('numerivocali/18.mp3', False)
    else:
        button_1_7["bg"] = coloreBase
def changeColor18():
    global coloreEstratto 
    global coloreBase
    if button_1_8.cget('bg') == coloreBase:
        button_1_8["bg"] = coloreEstratto
        #playsound('numerivocali/19.mp3', False)
    else:
        button_1_8["bg"] = coloreBase
def changeColor19():
    global coloreEstratto 
    global coloreBase
    if button_1_9.cget('bg') == coloreBase:
        button_1_9["bg"] = coloreEstratto
        #playsound('numerivocali/20.mp3', False)
    else:
        button_1_9["bg"] = coloreBase
def changeColor20():
    global coloreEstratto 
    global coloreBase
    if button_2_0.cget('bg') == coloreBase:
        button_2_0["bg"] = coloreEstratto
        #playsound('numerivocali/21.mp3', False)
    else:
        button_2_0["bg"] = coloreBase
def changeColor21():
    global coloreEstratto 
    global coloreBase
    if button_2_1.cget('bg') == coloreBase:
        button_2_1["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_2_1["bg"] = coloreBase
def changeColor22():
    global coloreEstratto 
    global coloreBase
    if button_2_2.cget('bg') == coloreBase:
        button_2_2["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_2_2["bg"] = coloreBase
def changeColor23():
    global coloreEstratto 
    global coloreBase
    if button_2_3.cget('bg') == coloreBase:
        button_2_3["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_2_3["bg"] = coloreBase
def changeColor24():
    global coloreEstratto 
    global coloreBase
    if button_2_4.cget('bg') == coloreBase:
        button_2_4["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_2_4["bg"] = coloreBase
def changeColor25():
    global coloreEstratto 
    global coloreBase
    if button_2_5.cget('bg') == coloreBase:
        button_2_5["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_2_5["bg"] = coloreBase
def changeColor26():
    global coloreEstratto 
    global coloreBase
    if button_2_6.cget('bg') == coloreBase:
        button_2_6["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_2_6["bg"] = coloreBase
def changeColor27():
    global coloreEstratto 
    global coloreBase
    if button_2_7.cget('bg') == coloreBase:
        button_2_7["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_2_7["bg"] = coloreBase
def changeColor28():
    global coloreEstratto 
    global coloreBase
    if button_2_8.cget('bg') == coloreBase:
        button_2_8["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_2_8["bg"] = coloreBase
def changeColor29():
    global coloreEstratto 
    global coloreBase
    if button_2_9.cget('bg') == coloreBase:
        button_2_9["bg"] = coloreEstratto
        #playsound('numerivocali/30.mp3', False)
    else:
        button_2_9["bg"] = coloreBase
def changeColor30():
    global coloreEstratto 
    global coloreBase
    if button_3_0.cget('bg') == coloreBase:
        button_3_0["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_3_0["bg"] = coloreBase
def changeColor31():
    global coloreEstratto 
    global coloreBase
    if button_3_1.cget('bg') == coloreBase:
        button_3_1["bg"] = coloreEstratto
        #playsound('numerivocali/32.mp3', False)
    else:
        button_3_1["bg"] = coloreBase
def changeColor32():
    global coloreEstratto 
    global coloreBase
    if button_3_2.cget('bg') == coloreBase:
        button_3_2["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_3_2["bg"] = coloreBase
def changeColor33():
    global coloreEstratto 
    global coloreBase
    if button_3_3.cget('bg') == coloreBase:
        button_3_3["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_3_3["bg"] = coloreBase
def changeColor34():
    global coloreEstratto 
    global coloreBase
    if button_3_4.cget('bg') == coloreBase:
        button_3_4["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_3_4["bg"] = coloreBase
def changeColor35():
    global coloreEstratto 
    global coloreBase
    if button_3_5.cget('bg') == coloreBase:
        button_3_5["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_3_5["bg"] = coloreBase
def changeColor36():
    global coloreEstratto 
    global coloreBase
    if button_3_6.cget('bg') == coloreBase:
        button_3_6["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_3_6["bg"] = coloreBase
def changeColor37():
    global coloreEstratto 
    global coloreBase
    if button_3_7.cget('bg') == coloreBase:
        button_3_7["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_3_7["bg"] = coloreBase
def changeColor38():
    global coloreEstratto 
    global coloreBase
    if button_3_8.cget('bg') == coloreBase:
        button_3_8["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_3_8["bg"] = coloreBase
def changeColor39():
    global coloreEstratto 
    global coloreBase
    if button_3_9.cget('bg') == coloreBase:
        button_3_9["bg"] = coloreEstratto
        #playsound('numerivocali/40.mp3', False)
    else:
        button_3_9["bg"] = coloreBase
def changeColor40():
    global coloreEstratto 
    global coloreBase
    if button_4_0.cget('bg') == coloreBase:
        button_4_0["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_4_0["bg"] = coloreBase
def changeColor41():
    global coloreEstratto 
    global coloreBase
    if button_4_1.cget('bg') == coloreBase:
        button_4_1["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_4_1["bg"] = coloreBase
def changeColor42():
    global coloreEstratto 
    global coloreBase
    if button_4_2.cget('bg') == coloreBase:
        button_4_2["bg"] = coloreEstratto
        #playsound('numerivocali/43.mp3', False)
    else:
        button_4_2["bg"] = coloreBase
def changeColor43():
    global coloreEstratto 
    global coloreBase
    if button_4_3.cget('bg') == coloreBase:
        button_4_3["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_4_3["bg"] = coloreBase
def changeColor44():
    global coloreEstratto 
    global coloreBase
    if button_4_4.cget('bg') == coloreBase:
        button_4_4["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_4_4["bg"] = coloreBase
def changeColor45():
    global coloreEstratto 
    global coloreBase
    if button_4_5.cget('bg') == coloreBase:
        button_4_5["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_4_5["bg"] = coloreBase
def changeColor46():
    global coloreEstratto 
    global coloreBase
    if button_4_6.cget('bg') == coloreBase:
        button_4_6["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_4_6["bg"] = coloreBase
def changeColor47():
    global coloreEstratto 
    global coloreBase
    if button_4_7.cget('bg') == coloreBase:
        button_4_7["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_4_7["bg"] = coloreBase
def changeColor48():
    global coloreEstratto 
    global coloreBase
    if button_4_8.cget('bg') == coloreBase:
        button_4_8["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_4_8["bg"] = coloreBase
def changeColor49():
    global coloreEstratto 
    global coloreBase
    if button_4_9.cget('bg') == coloreBase:
        button_4_9["bg"] = coloreEstratto
        #playsound('numerivocali/50.mp3', False)
    else:
        button_4_9["bg"] = coloreBase
def changeColor50():
    global coloreEstratto 
    global coloreBase
    if button_5_0.cget('bg') == coloreBase:
        button_5_0["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_5_0["bg"] = coloreBase
def changeColor51():
    global coloreEstratto 
    global coloreBase
    if button_5_1.cget('bg') == coloreBase:
        button_5_1["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_5_1["bg"] = coloreBase
def changeColor52():
    global coloreEstratto 
    global coloreBase
    if button_5_2.cget('bg') == coloreBase:
        button_5_2["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_5_2["bg"] = coloreBase
def changeColor53():
    global coloreEstratto 
    global coloreBase
    if button_5_3.cget('bg') == coloreBase:
        button_5_3["bg"] = coloreEstratto
        #playsound('numerivocali/54.mp3', False)
    else:
        button_5_3["bg"] = coloreBase
def changeColor54():
    global coloreEstratto 
    global coloreBase
    if button_5_4.cget('bg') == coloreBase:
        button_5_4["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_5_4["bg"] = coloreBase
def changeColor55():
    global coloreEstratto 
    global coloreBase
    if button_5_5.cget('bg') == coloreBase:
        button_5_5["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_5_5["bg"] = coloreBase
def changeColor56():
    global coloreEstratto 
    global coloreBase
    if button_5_6.cget('bg') == coloreBase:
        button_5_6["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_5_6["bg"] = coloreBase
def changeColor57():
    global coloreEstratto 
    global coloreBase
    if button_5_7.cget('bg') == coloreBase:
        button_5_7["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_5_7["bg"] = coloreBase
def changeColor58():
    global coloreEstratto 
    global coloreBase
    if button_5_8.cget('bg') == coloreBase:
        button_5_8["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_5_8["bg"] = coloreBase
def changeColor59():
    global coloreEstratto 
    global coloreBase
    if button_5_9.cget('bg') == coloreBase:
        button_5_9["bg"] = coloreEstratto
        #playsound('numerivocali/60.mp3', False)
    else:
        button_5_9["bg"] = coloreBase
def changeColor60():
    global coloreEstratto 
    global coloreBase
    if button_6_0.cget('bg') == coloreBase:
        button_6_0["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_6_0["bg"] = coloreBase
def changeColor61():
    global coloreEstratto 
    global coloreBase
    if button_6_1.cget('bg') == coloreBase:
        button_6_1["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_6_1["bg"] = coloreBase
def changeColor62():
    global coloreEstratto 
    global coloreBase
    if button_6_2.cget('bg') == coloreBase:
        button_6_2["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_6_2["bg"] = coloreBase
def changeColor63():
    global coloreEstratto 
    global coloreBase
    if button_6_3.cget('bg') == coloreBase:
        button_6_3["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_6_3["bg"] = coloreBase
def changeColor64():
    global coloreEstratto 
    global coloreBase
    if button_6_4.cget('bg') == coloreBase:
        button_6_4["bg"] = coloreEstratto
        #playsound('numerivocali/65.mp3', False)
    else:
        button_6_4["bg"] = coloreBase
def changeColor65():
    global coloreEstratto 
    global coloreBase
    if button_6_5.cget('bg') == coloreBase:
        button_6_5["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_6_5["bg"] = coloreBase
def changeColor66():
    global coloreEstratto 
    global coloreBase
    if button_6_6.cget('bg') == coloreBase:
        button_6_6["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_6_6["bg"] = coloreBase
def changeColor67():
    global coloreEstratto 
    global coloreBase
    if button_6_7.cget('bg') == coloreBase:
        button_6_7["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_6_7["bg"] = coloreBase
def changeColor68():
    global coloreEstratto 
    global coloreBase
    if button_6_8.cget('bg') == coloreBase:
        button_6_8["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_6_8["bg"] = coloreBase
def changeColor69():
    global coloreEstratto 
    global coloreBase
    if button_6_9.cget('bg') == coloreBase:
        button_6_9["bg"] = coloreEstratto
        #playsound('numerivocali/70.mp3', False)
    else:
        button_6_9["bg"] = coloreBase
def changeColor70():
    global coloreEstratto 
    global coloreBase
    if button_7_0.cget('bg') == coloreBase:
        button_7_0["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_7_0["bg"] = coloreBase
def changeColor71():
    global coloreEstratto 
    global coloreBase
    if button_7_1.cget('bg') == coloreBase:
        button_7_1["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_7_1["bg"] = coloreBase
def changeColor72():
    global coloreEstratto 
    global coloreBase
    if button_7_2.cget('bg') == coloreBase:
        button_7_2["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_7_2["bg"] = coloreBase
def changeColor73():
    global coloreEstratto 
    global coloreBase
    if button_7_3.cget('bg') == coloreBase:
        button_7_3["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_7_3["bg"] = coloreBase
def changeColor74():
    global coloreEstratto 
    global coloreBase
    if button_7_4.cget('bg') == coloreBase:
        button_7_4["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_7_4["bg"] = coloreBase
def changeColor75():
    global coloreEstratto 
    global coloreBase
    if button_7_5.cget('bg') == coloreBase:
        button_7_5["bg"] = coloreEstratto
        #playsound('numerivocali/76.mp3', False)
    else:
        button_7_5["bg"] = coloreBase
def changeColor76():
    global coloreEstratto 
    global coloreBase
    if button_7_6.cget('bg') == coloreBase:
        button_7_6["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_7_6["bg"] = coloreBase
def changeColor77():
    global coloreEstratto 
    global coloreBase
    if button_7_7.cget('bg') == coloreBase:
        button_7_7["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_7_7["bg"] = coloreBase
def changeColor78():
    global coloreEstratto 
    global coloreBase
    if button_7_8.cget('bg') == coloreBase:
        button_7_8["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_7_8["bg"] = coloreBase
def changeColor79():
    global coloreEstratto 
    global coloreBase
    if button_7_9.cget('bg') == coloreBase:
        button_7_9["bg"] = coloreEstratto
        #playsound('numerivocali/80.mp3', False)
    else:
        button_7_9["bg"] = coloreBase
def changeColor80():
    global coloreEstratto 
    global coloreBase
    if button_8_0.cget('bg') == coloreBase:
        button_8_0["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_8_0["bg"] = coloreBase
def changeColor81():
    global coloreEstratto 
    global coloreBase
    if button_8_1.cget('bg') == coloreBase:
        button_8_1["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_8_1["bg"] = coloreBase
def changeColor82():
    global coloreEstratto 
    global coloreBase
    if button_8_2.cget('bg') == coloreBase:
        button_8_2["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_8_2["bg"] = coloreBase
def changeColor83():
    global coloreEstratto 
    global coloreBase
    if button_8_3.cget('bg') == coloreBase:
        button_8_3["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_8_3["bg"] = coloreBase
def changeColor84():
    global coloreEstratto 
    global coloreBase
    if button_8_4.cget('bg') == coloreBase:
        button_8_4["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_8_4["bg"] = coloreBase
def changeColor85():
    global coloreEstratto 
    global coloreBase
    if button_8_5.cget('bg') == coloreBase:
        button_8_5["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_8_5["bg"] = coloreBase
def changeColor86():
    global coloreEstratto 
    global coloreBase
    if button_8_6.cget('bg') == coloreBase:
        button_8_6["bg"] = coloreEstratto
        #playsound('numerivocali/87.mp3', False)
    else:
        button_8_6["bg"] = coloreBase
def changeColor87():
    global coloreEstratto 
    global coloreBase
    if button_8_7.cget('bg') == coloreBase:
        button_8_7["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_8_7["bg"] = coloreBase
def changeColor88():
    global coloreEstratto 
    global coloreBase
    if button_8_8.cget('bg') == coloreBase:
        button_8_8["bg"] = coloreEstratto
        #playsound('numerivocali/beep.mp3', False)
    else:
        button_8_8["bg"] = coloreBase
def changeColor89():
    global coloreEstratto 
    global coloreBase
    if button_8_9.cget('bg') == coloreBase:
        button_8_9["bg"] = coloreEstratto
        #playsound('numerivocali/90.mp3', False)
    else:
        button_8_9["bg"] = coloreBase

Grid.rowconfigure(root, 0, weight = 1)
Grid.rowconfigure(root, 1, weight = 1)
Grid.rowconfigure(root, 2, weight = 1)
Grid.rowconfigure(root, 3, weight = 1)
Grid.rowconfigure(root, 4, weight = 1)
Grid.rowconfigure(root, 5, weight = 1)
Grid.rowconfigure(root, 6, weight = 1)
Grid.rowconfigure(root, 7, weight = 1)
Grid.rowconfigure(root, 8, weight = 1)

Grid.columnconfigure(root, 0, weight = 1)
Grid.columnconfigure(root, 1, weight = 1)
Grid.columnconfigure(root, 2, weight = 1)
Grid.columnconfigure(root, 3, weight = 1)
Grid.columnconfigure(root, 4, weight = 1)
Grid.columnconfigure(root, 5, weight = 1)
Grid.columnconfigure(root, 6, weight = 1)
Grid.columnconfigure(root, 7, weight = 1)
Grid.columnconfigure(root, 8, weight = 1)
Grid.columnconfigure(root, 9, weight = 1)

button_0_0 = Button(root, bg = coloreBase, text="1", font=helv36, command = changeColor00 )
button_0_1 = Button(root, bg = coloreBase, text="2", font=helv36, command = changeColor01 )
button_0_2 = Button(root, bg = coloreBase, text="3", font=helv36, command = changeColor02 )
button_0_3 = Button(root, bg = coloreBase, text="4", font=helv36, command = changeColor03 )
button_0_4 = Button(root, bg = coloreBase, text="5", font=helv36, command = changeColor04 )
button_0_5 = Button(root, bg = coloreBase, text="6", font=helv36, command = changeColor05 )
button_0_6 = Button(root, bg = coloreBase, text="7", font=helv36, command = changeColor06 )
button_0_7 = Button(root, bg = coloreBase, text="8", font=helv36, command = changeColor07 )
button_0_8 = Button(root, bg = coloreBase, text="9", font=helv36, command = changeColor08 )
button_0_9 = Button(root, bg = coloreBase, text="10", font=helv36, command = changeColor09 )
button_1_0 = Button(root, bg = coloreBase, text="11", font=helv36, command = changeColor10 )
button_1_1 = Button(root, bg = coloreBase, text="12", font=helv36, command = changeColor11 )
button_1_2 = Button(root, bg = coloreBase, text="13", font=helv36, command = changeColor12 )
button_1_3 = Button(root, bg = coloreBase, text="14", font=helv36, command = changeColor13 )
button_1_4 = Button(root, bg = coloreBase, text="15", font=helv36, command = changeColor14 )
button_1_5 = Button(root, bg = coloreBase, text="16", font=helv36, command = changeColor15 )
button_1_6 = Button(root, bg = coloreBase, text="17", font=helv36, command = changeColor16 )
button_1_7 = Button(root, bg = coloreBase, text="18", font=helv36, command = changeColor17 )
button_1_8 = Button(root, bg = coloreBase, text="19", font=helv36, command = changeColor18 )
button_1_9 = Button(root, bg = coloreBase, text="20", font=helv36, command = changeColor19 )
button_2_0 = Button(root, bg = coloreBase, text="21", font=helv36, command = changeColor20 )
button_2_1 = Button(root, bg = coloreBase, text="22", font=helv36, command = changeColor21 )
button_2_2 = Button(root, bg = coloreBase, text="23", font=helv36, command = changeColor22 )
button_2_3 = Button(root, bg = coloreBase, text="24", font=helv36, command = changeColor23 )
button_2_4 = Button(root, bg = coloreBase, text="25", font=helv36, command = changeColor24 )
button_2_5 = Button(root, bg = coloreBase, text="26", font=helv36, command = changeColor25 )
button_2_6 = Button(root, bg = coloreBase, text="27", font=helv36, command = changeColor26 )
button_2_7 = Button(root, bg = coloreBase, text="28", font=helv36, command = changeColor27 )
button_2_8 = Button(root, bg = coloreBase, text="29", font=helv36, command = changeColor28 )
button_2_9 = Button(root, bg = coloreBase, text="30", font=helv36, command = changeColor29 )
button_3_0 = Button(root, bg = coloreBase, text="31", font=helv36, command = changeColor30 )
button_3_1 = Button(root, bg = coloreBase, text="32", font=helv36, command = changeColor31 )
button_3_2 = Button(root, bg = coloreBase, text="33", font=helv36, command = changeColor32 )
button_3_3 = Button(root, bg = coloreBase, text="34", font=helv36, command = changeColor33 )
button_3_4 = Button(root, bg = coloreBase, text="35", font=helv36, command = changeColor34 )
button_3_5 = Button(root, bg = coloreBase, text="36", font=helv36, command = changeColor35 )
button_3_6 = Button(root, bg = coloreBase, text="37", font=helv36, command = changeColor36 )
button_3_7 = Button(root, bg = coloreBase, text="38", font=helv36, command = changeColor37 )
button_3_8 = Button(root, bg = coloreBase, text="39", font=helv36, command = changeColor38 )
button_3_9 = Button(root, bg = coloreBase, text="40", font=helv36, command = changeColor39 )
button_4_0 = Button(root, bg = coloreBase, text="41", font=helv36, command = changeColor40 )
button_4_1 = Button(root, bg = coloreBase, text="42", font=helv36, command = changeColor41 )
button_4_2 = Button(root, bg = coloreBase, text="43", font=helv36, command = changeColor42 )
button_4_3 = Button(root, bg = coloreBase, text="44", font=helv36, command = changeColor43 )
button_4_4 = Button(root, bg = coloreBase, text="45", font=helv36, command = changeColor44 )
button_4_5 = Button(root, bg = coloreBase, text="46", font=helv36, command = changeColor45 )
button_4_6 = Button(root, bg = coloreBase, text="47", font=helv36, command = changeColor46 )
button_4_7 = Button(root, bg = coloreBase, text="48", font=helv36, command = changeColor47 )
button_4_8 = Button(root, bg = coloreBase, text="49", font=helv36, command = changeColor48 )
button_4_9 = Button(root, bg = coloreBase, text="50", font=helv36, command = changeColor49 )
button_5_0 = Button(root, bg = coloreBase, text="51", font=helv36, command = changeColor50 )
button_5_1 = Button(root, bg = coloreBase, text="52", font=helv36, command = changeColor51 )
button_5_2 = Button(root, bg = coloreBase, text="53", font=helv36, command = changeColor52 )
button_5_3 = Button(root, bg = coloreBase, text="54", font=helv36, command = changeColor53 )
button_5_4 = Button(root, bg = coloreBase, text="55", font=helv36, command = changeColor54 )
button_5_5 = Button(root, bg = coloreBase, text="56", font=helv36, command = changeColor55 )
button_5_6 = Button(root, bg = coloreBase, text="57", font=helv36, command = changeColor56 )
button_5_7 = Button(root, bg = coloreBase, text="58", font=helv36, command = changeColor57 )
button_5_8 = Button(root, bg = coloreBase, text="59", font=helv36, command = changeColor58 )
button_5_9 = Button(root, bg = coloreBase, text="60", font=helv36, command = changeColor59 )
button_6_0 = Button(root, bg = coloreBase, text="61", font=helv36, command = changeColor60 )
button_6_1 = Button(root, bg = coloreBase, text="62", font=helv36, command = changeColor61 )
button_6_2 = Button(root, bg = coloreBase, text="63", font=helv36, command = changeColor62 )
button_6_3 = Button(root, bg = coloreBase, text="64", font=helv36, command = changeColor63 )
button_6_4 = Button(root, bg = coloreBase, text="65", font=helv36, command = changeColor64 )
button_6_5 = Button(root, bg = coloreBase, text="66", font=helv36, command = changeColor65 )
button_6_6 = Button(root, bg = coloreBase, text="67", font=helv36, command = changeColor66 )
button_6_7 = Button(root, bg = coloreBase, text="68", font=helv36, command = changeColor67 )
button_6_8 = Button(root, bg = coloreBase, text="69", font=helv36, command = changeColor68 )
button_6_9 = Button(root, bg = coloreBase, text="70", font=helv36, command = changeColor69 )
button_7_0 = Button(root, bg = coloreBase, text="71", font=helv36, command = changeColor70 )
button_7_1 = Button(root, bg = coloreBase, text="72", font=helv36, command = changeColor71 )
button_7_2 = Button(root, bg = coloreBase, text="73", font=helv36, command = changeColor72 )
button_7_3 = Button(root, bg = coloreBase, text="74", font=helv36, command = changeColor73 )
button_7_4 = Button(root, bg = coloreBase, text="75", font=helv36, command = changeColor74 )
button_7_5 = Button(root, bg = coloreBase, text="76", font=helv36, command = changeColor75 )
button_7_6 = Button(root, bg = coloreBase, text="77", font=helv36, command = changeColor76 )
button_7_7 = Button(root, bg = coloreBase, text="78", font=helv36, command = changeColor77 )
button_7_8 = Button(root, bg = coloreBase, text="79", font=helv36, command = changeColor78 )
button_7_9 = Button(root, bg = coloreBase, text="80", font=helv36, command = changeColor79 )
button_8_0 = Button(root, bg = coloreBase, text="81", font=helv36, command = changeColor80 )
button_8_1 = Button(root, bg = coloreBase, text="82", font=helv36, command = changeColor81 )
button_8_2 = Button(root, bg = coloreBase, text="83", font=helv36, command = changeColor82 )
button_8_3 = Button(root, bg = coloreBase, text="84", font=helv36, command = changeColor83 )
button_8_4 = Button(root, bg = coloreBase, text="85", font=helv36, command = changeColor84 )
button_8_5 = Button(root, bg = coloreBase, text="86", font=helv36, command = changeColor85 )
button_8_6 = Button(root, bg = coloreBase, text="87", font=helv36, command = changeColor86 )
button_8_7 = Button(root, bg = coloreBase, text="88", font=helv36, command = changeColor87 )
button_8_8 = Button(root, bg = coloreBase, text="89", font=helv36, command = changeColor88 )
button_8_9 = Button(root, bg = coloreBase, text="90", font=helv36, command = changeColor89 )

button_0_0.grid(row=0, column=0, sticky="EWNS")
button_0_1.grid(row=0, column=1, sticky="EWNS")
button_0_2.grid(row=0, column=2, sticky="EWNS")
button_0_3.grid(row=0, column=3, sticky="EWNS")
button_0_4.grid(row=0, column=4, sticky="EWNS")
button_0_5.grid(row=0, column=5, sticky="EWNS")
button_0_6.grid(row=0, column=6, sticky="EWNS")
button_0_7.grid(row=0, column=7, sticky="EWNS")
button_0_8.grid(row=0, column=8, sticky="EWNS")
button_0_9.grid(row=0, column=9, sticky="EWNS")
button_1_0.grid(row=1, column=0, sticky="EWNS")
button_1_1.grid(row=1, column=1, sticky="EWNS")
button_1_2.grid(row=1, column=2, sticky="EWNS")
button_1_3.grid(row=1, column=3, sticky="EWNS")
button_1_4.grid(row=1, column=4, sticky="EWNS")
button_1_5.grid(row=1, column=5, sticky="EWNS")
button_1_6.grid(row=1, column=6, sticky="EWNS")
button_1_7.grid(row=1, column=7, sticky="EWNS")
button_1_8.grid(row=1, column=8, sticky="EWNS")
button_1_9.grid(row=1, column=9, sticky="EWNS")
button_2_0.grid(row=2, column=0, sticky="EWNS")
button_2_1.grid(row=2, column=1, sticky="EWNS")
button_2_2.grid(row=2, column=2, sticky="EWNS")
button_2_3.grid(row=2, column=3, sticky="EWNS")
button_2_4.grid(row=2, column=4, sticky="EWNS")
button_2_5.grid(row=2, column=5, sticky="EWNS")
button_2_6.grid(row=2, column=6, sticky="EWNS")
button_2_7.grid(row=2, column=7, sticky="EWNS")
button_2_8.grid(row=2, column=8, sticky="EWNS")
button_2_9.grid(row=2, column=9, sticky="EWNS")
button_3_0.grid(row=3, column=0, sticky="EWNS")
button_3_1.grid(row=3, column=1, sticky="EWNS")
button_3_2.grid(row=3, column=2, sticky="EWNS")
button_3_3.grid(row=3, column=3, sticky="EWNS")
button_3_4.grid(row=3, column=4, sticky="EWNS")
button_3_5.grid(row=3, column=5, sticky="EWNS")
button_3_6.grid(row=3, column=6, sticky="EWNS")
button_3_7.grid(row=3, column=7, sticky="EWNS")
button_3_8.grid(row=3, column=8, sticky="EWNS")
button_3_9.grid(row=3, column=9, sticky="EWNS")
button_4_0.grid(row=4, column=0, sticky="EWNS")
button_4_1.grid(row=4, column=1, sticky="EWNS")
button_4_2.grid(row=4, column=2, sticky="EWNS")
button_4_3.grid(row=4, column=3, sticky="EWNS")
button_4_4.grid(row=4, column=4, sticky="EWNS")
button_4_5.grid(row=4, column=5, sticky="EWNS")
button_4_6.grid(row=4, column=6, sticky="EWNS")
button_4_7.grid(row=4, column=7, sticky="EWNS")
button_4_8.grid(row=4, column=8, sticky="EWNS")
button_4_9.grid(row=4, column=9, sticky="EWNS")
button_5_0.grid(row=5, column=0, sticky="EWNS")
button_5_1.grid(row=5, column=1, sticky="EWNS")
button_5_2.grid(row=5, column=2, sticky="EWNS")
button_5_3.grid(row=5, column=3, sticky="EWNS")
button_5_4.grid(row=5, column=4, sticky="EWNS")
button_5_5.grid(row=5, column=5, sticky="EWNS")
button_5_6.grid(row=5, column=6, sticky="EWNS")
button_5_7.grid(row=5, column=7, sticky="EWNS")
button_5_8.grid(row=5, column=8, sticky="EWNS")
button_5_9.grid(row=5, column=9, sticky="EWNS")
button_6_0.grid(row=6, column=0, sticky="EWNS")
button_6_1.grid(row=6, column=1, sticky="EWNS")
button_6_2.grid(row=6, column=2, sticky="EWNS")
button_6_3.grid(row=6, column=3, sticky="EWNS")
button_6_4.grid(row=6, column=4, sticky="EWNS")
button_6_5.grid(row=6, column=5, sticky="EWNS")
button_6_6.grid(row=6, column=6, sticky="EWNS")
button_6_7.grid(row=6, column=7, sticky="EWNS")
button_6_8.grid(row=6, column=8, sticky="EWNS")
button_6_9.grid(row=6, column=9, sticky="EWNS")
button_7_0.grid(row=7, column=0, sticky="EWNS")
button_7_1.grid(row=7, column=1, sticky="EWNS")
button_7_2.grid(row=7, column=2, sticky="EWNS")
button_7_3.grid(row=7, column=3, sticky="EWNS")
button_7_4.grid(row=7, column=4, sticky="EWNS")
button_7_5.grid(row=7, column=5, sticky="EWNS")
button_7_6.grid(row=7, column=6, sticky="EWNS")
button_7_7.grid(row=7, column=7, sticky="EWNS")
button_7_8.grid(row=7, column=8, sticky="EWNS")
button_7_9.grid(row=7, column=9, sticky="EWNS")
button_8_0.grid(row=8, column=0, sticky="EWNS")
button_8_1.grid(row=8, column=1, sticky="EWNS")
button_8_2.grid(row=8, column=2, sticky="EWNS")
button_8_3.grid(row=8, column=3, sticky="EWNS")
button_8_4.grid(row=8, column=4, sticky="EWNS")
button_8_5.grid(row=8, column=5, sticky="EWNS")
button_8_6.grid(row=8, column=6, sticky="EWNS")
button_8_7.grid(row=8, column=7, sticky="EWNS")
button_8_8.grid(row=8, column=8, sticky="EWNS")
button_8_9.grid(row=8, column=9, sticky="EWNS")


root.bind("<F11>", lambda event: root.attributes("-fullscreen",
                                    not root.attributes("-fullscreen")))
root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False)) 

root2 = Tk()
root2.title('Estrattore')
root2.geometry("320x150")

cbutton_0_0 = Button(root2, text="Estrai Numero", font=("", 25), command = Estrai )
cbutton_0_0.pack(pady=20)
status_label = Label(root2, text="Numero estratto", font=("", 20), bd = 1, relief = SUNKEN, anchor = E)
status_label.pack(fill=X, side=BOTTOM, ipady=2)

#ricominciaB = Button(root2, text="R", bg = "green", font=("", 6), command = Estrai )
#ricominciaB.pack(anchor = NW)

my_menu = Menu(root2)
root2.config(menu=my_menu)

#Menu items
GiocataMenu = Menu(my_menu, tearoff="off")
my_menu.add_cascade(label = "Giocata", menu = GiocataMenu)
GiocataMenu.add_command(label = "Nuova", command = Ricomincia)
GiocataMenu.add_command(label = "Spoiler", command = Spoiler)
#GiocataMenu.add_command(label = "Tabellone Fullscreen", command = schermoIntero)
GiocataMenu.add_separator()
GiocataMenu.add_command(label = "Chiudi tutto", command = ChiudiTutto)
#Fine items

root.mainloop()


## Note

#Esempio for MacOS - maybe - https://stackoverflow.com/questions/1529847/how-to-change-the-foreground-or-background-colour-of-a-tkinter-button-on-mac-os
    #
    #from tkinter import *
    #from tkmacosx import Button #pip3 install tkmacosx
    #
    #root = Tk()
    #
    #B1 = Button(root, text='Mac OSX', bg='black',fg='green', borderless=1)
    #B1.pack()
    #
    #root.mainloop()
# Fine esempio per MacOs

#Installare su mac 
#No: brew install python-tk
#Ni: pip3 install tk

#  Da Installare come admin (sia PC che Mac):
#  pip install playsound==1.2.2