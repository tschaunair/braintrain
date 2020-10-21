import random
import time

x = int(input("Wie viel Rechnungen moechtest du machen "))
a = input("Plus oder Mal ? ")
y = x
c = 0
w = 0

    
gesamt = time.time()
def aufgabe_add(a):
    zahl1 = random.randrange(1,100)
    zahl2 = random.randrange(1,100)
    print (zahl1, a, zahl2)
    start = time.time()
    
    ergebnis_in = int(input("Gib die Loesung ein: "))
    ergebnis = zahl1 + zahl2
  
    if  ergebnis == ergebnis_in:
        print ("Korrekt")
        ende = time.time()
        global c
        c = c + 1
    else:
        print ("Falsch")
        ende = time.time()
        global w
        w = w + 1
    print("Loesungsdauer:")
    print('{:5.3f}s'.format(ende-start))
    
while x >= 1:
    aufgabe_add(a)
    x = x - 1
gesamt_ende = time.time()


print("Durchschnittliche Loesungsdauer:")
print('{:5.3f}s'.format((gesamt_ende-gesamt)/y))
print("Falsche:",w)
print("Richtige:",c)

