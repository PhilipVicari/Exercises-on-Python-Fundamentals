import json

#Per leggere un file json 
filejson = open("all-world-cup-players.json", "r")
worldcup = json.load(filejson)
filejson.close()

print(len(worldcup))

print(worldcup[1200])
print(worldcup[1200]['DateOfBirth'])


# !!!! SONO TUTTE OPERAZIONI SU LISTE !!!!
# 1) contare quanti calciatori hanno giocato per l'Italia
# 2) contare quanti calciatori hanno giocato per il Brasile
# 3) contare quanti calciatori hanno giocato per l'Argentina
# 4) Indicare quali calciatori hanno giocato sia per il Brasile, sia per l'Italia
# 5) Indicare quali calciatori hanno giocato sia per l'Argentina, sia per l'Italia
# 6) Trovare qual'è il calciatore più giovane che ha partecipato alla coppa del mondo
# 7) Trovare qual'è il calciatore più anziano che ha partecipato alla coppa del mondo
# 8) Trovare quale calciatore ha partecipato a più edizioni della coppa del mondo
# 9) Trovare quale squadra di calcio ha fornito più calciatori per la coppa del mondo
#    Organizzare per nazione. Cioè quale squadra italiana ha fornito più calciatori per la coppa del mondo e quanti, quale squadra francese, ...

#Esempio:
quantiCalciatori = dict()
for v in worldcup:
    # se v.Team è già presente, sommo 1, altrimenti metto a 1
    if v["Team"] in quantiCalciatori.keys():
        quantiCalciatori[v["Team"]]=quantiCalciatori[v["Team"]]+1
    else:
        quantiCalciatori[v["Team"]]=1

print(quantiCalciatori)


cal_ita=0
for Fballer in worldcup:
    if Fballer["ClubCountry"]=="Italy":
        cal_ita+=1
print(cal_ita)


cal_bra=0
for Fballer in worldcup:
    if Fballer["ClubCountry"]=="Brazil":
        cal_bra+=1
print(cal_bra)

cal_arg=0
for Fballer in worldcup:
    if Fballer["ClubCountry"]=="Argentina":
        cal_arg+=1
print(cal_arg)

for annoMondiale in worldcup:
    if annoMondiale["Year"] in quantiCalciatori.keys():
        etacalciatore=quantiCalciatori["Year"]-quantiCalciatori["DateOfBirth"]<=18
        print(quantiCalciatori["FullName"])
    