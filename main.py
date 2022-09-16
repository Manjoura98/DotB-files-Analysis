#Auteurs: Mehdi MANJOURA & Lamia Ammarkhodja
from math import *


def benchmark(texte,texte2):

    a = texte.count('(')
    aa = texte.count(')')
    b = texte2.count('(')
    bb = texte2.count(')')
    list1 = []
    list2 = []
    n = len(texte)
    i = 0
    listpairs1 = []
    listpairs2 = []
    if (len(texte) == len(texte2)) and (a == aa) and (b == bb):
        while i < n:
            while texte[i] == '(':
                list1.append(i)
                i += 1
            if texte[i] == '.':
                i += 1

            else:

                listpairs1.append((list1[-1],i))
                list1.pop(-1)
                i += 1

        i=0
        while i < n:
            while texte2[i] == '(':
                list2.append(i)
                i += 1
            if texte2[i] == '.':
                i += 1

            else:

                listpairs2.append((list2[-1],i))
                list2.pop(-1)
                i += 1

    
    #print(len(listpairs2))


    #calculer le nombre de pairs en commun
    TP = 0
    for i in listpairs1:
        for j in listpairs2:
            if i == j:
                TP = TP + 1
                break

    #lblresultat['text'] = TP
    listresultats = []
    global listMCC
    global MCC
    listMCC = []

    listresultats.append(TP)

    #calucler FP et FN
    #FP : le nombre de paires présentes dans la 2ème mais absentes dans la 1ère.
    FP = len(listpairs2) - TP
    #lblresultat1['text'] = FP
    listresultats.append(FP)
    #FN : le nombre de paires présentes dans la 1ère mais absentes dans la 2ème.
    FN = len(listpairs1) - TP
    listresultats.append(FN)
    #lblresultat2['text'] = FN
    #les autres calculs
    PPV = TP / (TP + FP)
    listresultats.append(PPV)
    #lblresultat3['text'] = PPV
    STY = TP / (TP + FN)
    listresultats.append(STY)
    # lblresultat4['text'] = STY
    MCC = sqrt(STY * PPV)
    listresultats.append(MCC)
    #lblresultat5['text'] = MCC
    return print("liste des résultats:", "TP:",listresultats[0],"FP:",listresultats[1],"FN:",listresultats[2],"PPV:",listresultats[3],"STY:",listresultats[4],"MCC:",listresultats[5])
strucRef = input("Entrez votre structure de référence:")
fname = input("Entrez le nom du fichier avec l'ensemble des structues:")
f = open( fname, "r" )
lines = []
#ajouter les lignes à une liste
for line in f:
    lines.append(line)
f.close()
#enlever les \n de chaque fin de structure
lst = [x[:-1] for x in lines]
#enlever le dernier \n dans la liste
lst.pop()
texte2 = ''
#structure de référence
texte = strucRef
#liste avec les valeurs MCC de toutes les structures
listMCCC = []
#assign chaque élément de la liste à la variable texte2 et comparer avec la structure de référence
for x in lst:
    texte2 = x
    benchmark(texte, texte2)
    listMCCC.append(MCC)
    #print le plus grand MCC après chaque itération
    print("Le plus grand MCC, jusqu'à date est:", max(listMCCC))
#liste des structures zippée avec la liste des MCC correspondantes
listMCStruct = list(zip(listMCCC,lst))
#retourne la structure avec le plus grand MCC
print("La structure la plus proche de la référence et son MCC, sont les suivants:",max(listMCStruct))

