"""
Module dessaie
"""
from math import *

def f(x):
    "fonction"
    return log(x)/(x**2)

def racine(f, x):
    "fonction racine"
    if 2*f(x)-1 >= 0:
        return sqrt(2*f(x)-1)
    else:
        return "Non defini!"

def bacteries(n:int, bact:float):
    "fonction sa alkule nomb bacteries ki  vivan nan yon culture apres yon kantite segond"
    bacteries_vivantes = 0.96**n*(bact)
    return bacteries_vivantes

def magnitude(E):
    "li kalkule magitude yon seisme connaissant kantite energie ki degaje ladann"
    M = round((log10(E) - 4.8)/ 1.5, 1)   #Energie : E, en joules
    return M

def age(L):
    """La scrobicularia plana est un mollusque bivalve qui vit dans la vase des estuaires
    Cete fonction nous permet de determiner la l'age de ce mollusque en fonction de sa taille.
    """
    t = (log(L) - log(37.2260)) / (-0.9789)    #age en annee
    return t


def sol(prec, alpha):
    x = (alpha)**0.5
    x = round(x, prec)
    return f"f(x) = {alpha}, for x = {x}"

def factorielle(n):
    resultat = 1
    for i in range(1, n+1):
        resultat = i * resultat
    return resultat

def factorielle2(n):
    if n == 0:
        resultat = 1
    else:
        resultat = n*factorielle2(n-1)
    return resultat

def combinaison(k, n):
    if k > n:
        resultat = False
    else:
        resultat = factorielle(n) / (factorielle(k) * (n-k) )
    return resultat

def nbres_parties(n):
    "definis le nombre de parties a p elements d'un ensemble a n elements"
    