# EXERCICE : Écris une fonction qui prend une liste en entrée et retourne une nouvelle liste contenant les éléments qui apparaissent plus d'une fois.

def plus_d_une_fois(liste):
    a = []
    i = 0
    while i <= len(liste) :
        if liste[i] == liste [i + 1] :
            a += liste [i]
        i += 1
    return a
print(plus_d_une_fois([1,2,1,5,5,7,8,7]))
            
