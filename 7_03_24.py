import random
import time

"""start = time.time_ns()
lista = []
for v in range (1, 100000000):
    lista.append(random.randint(1,1000))
    end = time.time_ns()
    print (((end-start)/10000000000))

start = time.time_ns()
trovati=0
for v in range (1,10000000):
    if random.randint(1,100000000) in lista:
        trovati=+1
end= time.time_ns()
print ( (end-start)/100000000, {trovati})
"""


"""start = time.time_ns()
aSet= set()
for v in range (1, 100000000):
    aSet.add(random.randint(1,1000))
    end = time.time_ns()
    print (((end-start)/10000000000))

start = time.time_ns()
trovati=0
for v in range (1,10000000):
    if random.randint(1,100000000) in aSet:
        trovati=+1
end= time.time_ns()
print (f"il tempo richiesto per cercare è: ", (end-start)/100000000, "e ne ha trovati", {trovati})
lista_dispari = [x*2+1 for x in range (0,10)]
lista_numeri = [x for x in range (0,10)]
print(lista_numeri)
print(lista_dispari)
print(list(zip(lista_numeri, lista_dispari)))

nomi = ["mario", "Andrea", "Gianluca"]
cognomi = ["Rossi", "Marquez", "Dovizioso"]
print(nomi)
print (cognomi)
print(list(zip(nomi, cognomi)))"""






numero=""
counter = 0
while True:
    c=input ("digita 0-9 ,+-*/=")
    if c == ",":
        if counter >= 1:
            print("Nun se po fa")
            continue
        counter=counter + 1
    if len (c)>0:
        c=c[0]
    #dovete leggere sia un numero intero, sia decimale e stamparlo
    #nella sua interezza quando viene 
    #digitato un simbolo non numerico (+-*/)
    #
    #Terminerete quando varrà la 
    if  c not in ["0","1","2","3","4","5","6","7","8","9", ","]:
        #stampate il vostro numero letto
        print("Il numero è: ", numero)
        break
    else:
        #costruzione del numero...
        numero=numero+c