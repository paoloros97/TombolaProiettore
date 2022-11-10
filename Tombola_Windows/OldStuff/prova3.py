import tkinter as tk
from tkinter import messagebox
import random

class Tabellone:
    def __init__(self, master):

        self.coloreEstratto = "#3cff00"
        self.coloreBase = "#ffffff"

        # Tabellone
        self.master = master
        
        self.master.title('Tombola by Ros')
        window_width = self.master.winfo_screenwidth()
        window_height = self.master.winfo_screenheight()
        self.master.geometry ("%dx%d"%(window_width,window_height))

        self.button = []
        num = 0
        for i in range(0, 9):
            for j in range(0, 10):
                num = num + 1
                self.button.append(tk.Button(self.master, text=str(num), bg = '#ffffff', font=("", 60), command = lambda c = num-1: self.changeColor(c)))
                self.button[-1].grid(row=i, column=j, sticky="EWNS")
                tk.Grid.rowconfigure(self.master, i, weight = 1)
                tk.Grid.columnconfigure(self.master, j, weight = 1)
        
        # Estrattore
        self.estrattore = tk.Toplevel(self.master)
        self.estrattore.protocol("WM_DELETE_WINDOW", self.disable_event) # Disabilita il pulsante X della finestra
        self.frame = tk.Frame(self.estrattore)

        New_btn = tk.Button(self.frame, text="Pulisci Tabellone", command = lambda : self.nuovaGiocataFair() )
        New_btn.grid(sticky = tk.NW)

        Estrai_btn = tk.Button(self.frame, text="Estrai Numero", font=("", 30), command = lambda : self.EstraiFair())
        Estrai_btn.grid()

        self.status_label = tk.Label(self.frame, text="", font=("", 30))
        self.status_label.grid(sticky = tk.S)
        
        self.frame.pack() # Tappo della finestra dell'estrattore

        self.nuovaGiocataFair() # Prepara nuova giocata
        #self.nuovaGiocata() # Prepara nuova giocata


    def disable_event(self): # Disabilita il pulsante X della finestra
        messagebox.showwarning('Warning', 'Per terminare il programma chiudere la finestra del Tabellone.')
        pass

    # def nuovaGiocata(self):

    #     self.giocata = random.sample(range(90), 90) # Prepara una nuova stiga di numeri casuali
    #     self.posizione = 0 # Azzera il contatore che indicizza il numero estratto
    #     #print(self.giocata)

    #     for btn_number in range(len(self.button)):
    #         self.button[btn_number]["bg"] = self.coloreBase

    #     self.status_label.config(text = "N° estratto") # Reimposta il visualizzatore nell'estrattore

    def nuovaGiocataFair(self):
        
        self.estratti = set()
        
        for btn_number in range(len(self.button)):
            self.button[btn_number]["bg"] = self.coloreBase

        self.status_label.config(text = "N° estratto") # Reimposta il visualizzatore nell'estrattore


    def changeColor(self, btn_number): # Toggle del colore sul tabellone

        if self.button[btn_number].cget('bg') == self.coloreBase:
            self.button[btn_number]["bg"] = self.coloreEstratto
        else:
            self.button[btn_number]["bg"] = self.coloreBase
    
    # def Estrai(self):

    #     if self.posizione == 90:
    #         self.status_label.config(text = "Fine")
    #         print("Fine") # Tabellone completato
    #         return

    #     indice = self.giocata[self.posizione]
    #     print(indice + 1)
    #     self.changeColor(indice) #Colora il numero estratto sul tabellone  
    #     self.status_label.config(text = str(indice + 1)) #Stampa il numero estratto sulla finestra dell'Estrattore
    #     self.posizione += 1 #Pronto per il successivo
    
    def EstraiFair(self):
        attuali = len(self.estratti)

        if attuali == 90:
            self.status_label.config(text = "Fine")
            print("Fine") # Tabellone completato
            return

        numero = random.randrange(90) # Estrae un numero casuale intero tra 0 e 89
        self.estratti.add(numero) # Aggiunge il numero estratto al Set

        if len(self.estratti) == attuali: # Se il numero era già stato estratto, si ripete l'estrazione.
            self.EstraiFair() 
        else: # Altrimenti lo si mostra sul tabellone.
            print(numero)
            self.changeColor(numero) #Colora il numero estratto sul tabellone  
            self.status_label.config(text = str(numero + 1)) #Stampa il numero estratto sulla finestra dell'Estrattore

def main(): 
    root = tk.Tk()
    Tabellone(root)
    root.mainloop()

if __name__ == '__main__':
    main()