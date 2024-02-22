import sys
#In una stanza entrano, uno dopo l'altro, 10 persone, rispettivamente:
#antonio, marco, andrea, luigi, tony, bruno, laura, anita, annarita, lucia
#le prime due vanno via dopo un pochino di tempo ma entrano altre tre persone
#john, alice, mary
#altre due vanno via, sempre in ordine di ingresso (primo entrato, primo a uscire)
#stampare l'elenco delle persone presenti
lista=["Antonio", "Marco", "Andrea", "luigi", "tony", "bruno", "laura", "anita", "annarita", "lucia"]
print(lista)
lista.pop(0)
lista.pop(0)
print (lista)

lista.append("john") 
lista.append ("alice")
lista.append ("mary")

lista.pop(0)
lista.pop(0)

print(lista)

lista.sort()

print(lista)
