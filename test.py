#EXERCICE 1

def inverse_chaine(chaine):
    chaine_inverse = ''
    for i in range(len(chaine) - 1, -1, -1):
        chaine_inverse += chaine[i]
    return chaine_inverse

print (inverse_chaine("bonjour"))

#EXERCICE 2

def somme_liste(liste):
    somme = 0
    i = 0
    while i < len(liste):
        somme += liste[i]
        i += 1
    return somme

    

print(somme_liste([1,2,3,4]))

#EXERCICE 3

def plus_grand(liste):
    max = liste[0]
    for nombre in liste:
        if nombre > max:
            max = nombre
    return max

print(plus_grand([3,58,11,21]))

#EXERCICE 4

def factorielle(nombre):
    resu = 1
    i = nombre
    while i > 1 :
        resu *= i
        i -= 1
    return resu

print(factorielle(5))

#EXERCICE 5

def palindrome(mot):
    debut = 0
    fin = len(mot) - 1
    while debut < fin:
        if mot[debut] != mot[fin]:
            return False 
        debut += 1
        fin -= 1
    return True

print(palindrome("radar"))

#EXERCICE 6

def nombre_mot(mot):
    phrase = len(mot)
    compteur = 1
    i = 0
    while i < phrase : 
        if mot[i] == ' ' : 
            compteur += 1
        i += 1
    return compteur

print(nombre_mot("le test logiciel est essentiel"))