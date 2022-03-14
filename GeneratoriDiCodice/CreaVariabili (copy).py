numero = 0

print("helv36 = tkFont.Font(size = 40, weight=tkFont.BOLD)")

for riga in range(10):
    for colonna in range(10):
        #print(f"def changeColor{riga}{colonna}():")
        #print(f"    button_{riga}_{colonna}[\"bg\"] = \"red\"")

        print(f"def changeColor{riga}{colonna}():")  
        print(f"    if button_{riga}_{colonna}.cget('bg') == \"SystemButtonFace\":")
        print(f"        button_{riga}_{colonna}[\"bg\"] = \"red\"")
        print(f"        playsound('numerivocali/beep.mp3', False)")
        print(f"    else:")
        print(f"        button_{riga}_{colonna}[\"bg\"] = \"SystemButtonFace\"")

for riga in range(10):
    print(f"Grid.rowconfigure(root, {riga}, weight = 1)")

for colonna in range(10):
    print(f"Grid.columnconfigure(root, {colonna}, weight = 1)")



for riga in range(10):
    for colonna in range(10):
        numero += 1
        print(f"button_{riga}_{colonna} = Button(root, text=\"{numero}\", font=helv36, command = changeColor{riga}{colonna} )")

for riga in range(10):
    for colonna in range(10):
        numero += 1
        print(f"button_{riga}_{colonna}.grid(row={riga}, column={colonna}, sticky=\"EWNS\")")
        #print(f"button_{riga}_{colonna}.grid(row={riga}, column={colonna}, sticky=\"nsew\")") #Old


print(f"root.mainloop()")


for riga in range(10):
    print(f"Grid.rowconfigure(root, {riga}, weight = 1)")

for colonna in range(10):
    print(f"Grid.columnconfigure(root, {colonna}, weight = 1)")



for riga in range(10):
    for colonna in range(10):
        numero += 1
        print(f"button_{riga}_{colonna} = Button(root, text=\"{numero}\", font=helv36, command = changeColor{riga}{colonna} )")

for riga in range(10):
    for colonna in range(10):
        numero += 1
        print(f"button_{riga}_{colonna}.grid(row={riga}, column={colonna}, sticky=\"EWNS\")")
        #print(f"button_{riga}_{colonna}.grid(row={riga}, column={colonna}, sticky=\"nsew\")") #Old


print(f"root1.mainloop()")




