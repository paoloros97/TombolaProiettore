import tkinter as tk
from tkinter import messagebox
import random

# To build the .exe
#pyinstaller --clean --onefile --icon icona.ico .\Tombola.py

class Tabellone:
    def __init__(self, master):

        self.coloreEstratto = "#ff0000" # Colorazione del numero sul tabellone estratto
        self.coloreBase = "#ffffff" # Colorazione base del numero sul tabellone (non estratto)

        # Finestra Tabellone
        self.master = master
        self.master.title('Tombola by Ros')
        self.master.bind("<F11>", lambda event: self.master.attributes("-fullscreen", not self.master.attributes("-fullscreen")))
        self.master.bind("<Escape>", lambda event: self.master.attributes("-fullscreen", False)) 

        # Dimensione automatica della finestra
        window_width = self.master.winfo_screenwidth()
        window_height = self.master.winfo_screenheight()
        self.master.geometry ("%dx%d"%(window_width,window_height))

        self.button = [] # Inizializzazione della griglia di numeri (Buttons)
        num = 0 # Contatore che poi sarà utilizzato come indice della lista button
        for i in range(0, 9):
            for j in range(0, 10):
                num = num + 1
                self.button.append(tk.Button(self.master, text=str(num), bg = '#ffffff', font=("", 60), command = lambda c = num-1: self.changeColor(c)))
                self.button[-1].grid(row=i, column=j, sticky="EWNS")
                tk.Grid.rowconfigure(self.master, i, weight = 1)
                tk.Grid.columnconfigure(self.master, j, weight = 1)
        
        # Finestra Estrattore
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

        self.nuovaGiocataFair() # Prepara la prima giocata


    def disable_event(self): # Disabilita il pulsante X della finestra -mostra una finestra di warning.
        messagebox.showwarning('Warning', 'Per terminare il programma chiudere la finestra del Tabellone.')
        pass

    def nuovaGiocataFair(self):
        print('Nuova estrazione.')
        self.estratti = set() #Re-inizializza il set di deposito numeri estratti
        
        for btn_number in range(len(self.button)):
            self.button[btn_number]["bg"] = self.coloreBase

        self.status_label.config(text = "N° estratto") # Reimposta il visualizzatore nell'estrattore

    def EstraiFair(self):
        attuali = len(self.estratti) # Conta il totale dei numeri estratti fin'ora
        
        if attuali == 90: # Esce se è stato completato il tabellone
            self.status_label.config(text = "Fine")
            print("Fine")
            return

        numero = random.randrange(90) # Estrae un numero casuale intero tra 0 e 89
        self.estratti.add(numero) # Aggiunge il numero estratto al Set

        if len(self.estratti) == attuali: # Se il numero era già stato estratto prima, si ripete l'estrazione.
            self.EstraiFair() # Chiamata ricorsiva
        else: # Altrimenti lo si mostra sul tabellone.
            print(numero + 1) # +1 perchè il "numero" rappresenta l'indice
            self.changeColor(numero) # Colora il numero estratto sul tabellone  
            self.status_label.config(text = str(numero + 1)) # Stampa il numero estratto sulla finestra dell'Estrattore
   
    def changeColor(self, btn_number): # Toggle del colore sul tabellone
        if self.button[btn_number].cget('bg') == self.coloreBase: # Se il colore attuale è uguale al colore base imposta il coloreEstratto
            self.button[btn_number]["bg"] = self.coloreEstratto
        else: # Altrimenti imposta il coloreBase
            self.button[btn_number]["bg"] = self.coloreBase

def main(): 
    root = tk.Tk()
    Tabellone(root)
    root.mainloop()

if __name__ == '__main__':
    main()