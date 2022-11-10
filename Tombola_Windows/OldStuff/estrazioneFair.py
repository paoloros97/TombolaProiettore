import random
import time

estratti = set()
iterazione = 0

def nuovoNumero():
        attuali = len(estratti)
        numero = random.randrange(90)
        estratti.add(numero)
        print(estratti)
        if len(estratti) == attuali:
            nuovoNumero()
        else:
            return numero

while len(estratti) < 90:

    nuovoNumero()
    iterazione = iterazione + 1

print("Iterazione: ", iterazione)
