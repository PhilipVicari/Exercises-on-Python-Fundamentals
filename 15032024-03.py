import json

#Per leggere un file json 
filejson = open("all-world-cup-players.json", "r")
worldcup = json.load(filejson)
filejson.close()

print(len(worldcup))

print(worldcup[1200])
print(worldcup[1200]['DateOfBirth'])

#Esempio:
quantiCalciatori = dict()
"""
for v in worldcup:
    # se v.Team è già presente, sommo 1, altrimenti metto a 1
    if v["Team"] in quantiCalciatori.keys():
        quantiCalciatori[v["Team"]]=quantiCalciatori[v["Team"]]+1
    else:
        quantiCalciatori[v["Team"]]=1

print(quantiCalciatori)

# !!!! SONO TUTTE OPERAZIONI SU LISTE !!!!
# 1) contare quanti calciatori hanno giocato per l'Italia
cal_ita = []
for c in worldcup:
    if c["Team"] in ["Italy", "ITA"]:
        cal_ita.append(c["FullName"])
cal_ita_no_rip=set(cal_ita)
print("Giocatori Italiani:", len(cal_ita_no_rip))

# 2) contare quanti calciatori hanno giocato per il Brasile

cal_bra = []
for c in worldcup:
    if c["Team"] in ["Brazil", "BRA"]:
        cal_bra.append(c["FullName"])
cal_bra_no_rip=set(cal_bra)
print("Giocatori Brasiliani:", len(cal_bra_no_rip))

# 3) contare quanti calciatori hanno giocato per l'Argentina
cal_arg = []
for c in worldcup:
    if c["Team"] in ["Argentina", "ARG"]:
        cal_arg.append(c["FullName"])
cal_arg_no_rip=set(cal_arg)

print("Giocatori Argentini:", len(cal_arg_no_rip))
# 4) Indicare quali calciatori hanno giocato sia per il Brasile, sia per l'Italia
# 5) Indicare quali calciatori hanno giocato sia per l'Argentina, sia per l'Italia
def CalciatoriSquadra(elenco, squadra):
    calciatoriSquadra = []
    for c in elenco:
        if c["Team"] in squadra:
            calciatoriSquadra.append(c["FullName"])
    calciatoriSquadraSenzaRipetizioni = set(calciatoriSquadra)
    return calciatoriSquadraSenzaRipetizioni


calciatoriItalia = CalciatoriSquadra(worldcup, ["ITA", "Italy"])
calciatoriBrasile = CalciatoriSquadra(worldcup, ["BRA", "Brazil"])
calciatoriArgentina = CalciatoriSquadra(worldcup, ["ARG", "Argentina"])

print("Calciatori italia e brasile: ", calciatoriItalia.intersection(calciatoriBrasile))
print( "Calciatori italia e argentina: ",calciatoriItalia.intersection(calciatoriArgentina),)

# 6) Trovare qual'è il calciatore più giovane che ha partecipato alla coppa del mondo
annoMondiale=[]
AnnoNascita=[]
eta=0
for a in worldcup:
    annoMondiale.append(a["Year"])
    AnnoNascita.append(a["DateOfBirth"])
    int(AnnoNascita[0])
print(type(AnnoNascita[0]))
"""
# 7) Trovare qual'è il calciatore più anziano che ha partecipato alla coppa del mondo
# 8) Trovare quale calciatore ha partecipato a più edizioni della coppa del mondo
calciatore=[]
annoComp=[]
for cal in worldcup:
    calciatore.append(cal["FullName"])
    calciatore.append(cal["Year"])
    if calciatore in :
        
print(calciatore)
# 9) Trovare quale squadra di calcio ha fornito più calciatori per la coppa del mondo
#    Organizzare per nazione. Cioè quale squadra italiana ha fornito più calciatori per la coppa del mondo e quanti, quale squadra francese, ...