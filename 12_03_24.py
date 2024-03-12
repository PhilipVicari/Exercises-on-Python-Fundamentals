"""
a = 10
b = 20
c = 30
if a % 2 == 0:
    print(b+c)

else:
    print (b-c)

def Arit (a,b,c):
    if a % 2 == 0:
        print(b+c)

    else:
        print (b-c)

Arit(10, 11, 12)
Arit(11, 2, 3)
Arit(101, 1000, 2)
a,b,c=10, 20, 30
Arit (b,c,a)
"""



import random
def ColoreCasuale():
    Colori=["rosso", "giallo", "verde", "blu", "arancio", "ciano"]
    return Colori[random.randint(0, len (Colori) -1)]
print(ColoreCasuale())
print(ColoreCasuale())
print(ColoreCasuale())
print(ColoreCasuale())