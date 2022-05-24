"""
Module sa baw zouti pou kalkule inverse yon valeur 
keu ou bali.
"""

import matplotlib.pyplot as plt
from graph_function import graph1, graph2
def inverse(x)->float:
    """
    Fonction sa a kalkule inverse nonb ou ba li an
    """
    return(1/x)




def inverse1(x):
    """
    Cette fonction permet de calculer toutes les valeurs
    allant de 0 a la valeur donnee en argument.
    """
    inv = []
    i = 1
    while i <= x:
        f_inv = 1 / i
        tip = type(f_inv)
        if tip == float:
            f_inv = round(f_inv, 5)
            inv.append(f_inv)
        else:
            inv.append(f_inv)
        i += 1
    return inv




def inverse2(X):
    """
    Fonction sa kapab kalkule inverse yon nonb 
    ou bali.
    Apre sa, li kapab baw yon graph...
    """
    
    x = 0
    pas_abs = X / 1000
    Inverse = []

    while x <= X:
        x += pas_abs
        inverse = (1 / x)
        Inverse.append(inverse)
    
    value_abs1 = -x
    value_abs2 = 1 / 10000

    abscisse1 = [value_abs1]

    while value_abs1 <= -value_abs2:
        value_abs1 += pas_abs
        abscisse1.append(value_abs1)
    
    
    abscisse2 = [value_abs2]

    while value_abs2 <= x:
        value_abs2 += pas_abs
        abscisse2.append(value_abs2)

    ordonnee1 = [(1 / i) for i in abscisse1]
    ordonnee2 = [(1 / i) for i in abscisse2]

    graph1 = plt.plot(abscisse1, ordonnee1, "r-", lw=2.5)
    graph2 = plt.plot(abscisse2, ordonnee2, "r-", lw=2.5)
    plt.title("Courbe d'evolution de la fonction inverse")
    plt.xlabel("X values")
    plt.ylabel("inverse")
    plt.grid("equal", axis="both", color="k", lw=1)
    plt.rcParams["figure.figsize"] = (8, 8)
    plt.axis([-x, x, -x, x])
    plt.show()
    plt.close()
    return graph1, graph2




def inverse3(X):
    """
    Cette prend un argument de type numerique en entree. Il cacule ainsi
    la valeur inverse exacte de l'argument pris en entree. Ensuite il
    calcule une liste de valeur partant de l'oppose de l'argument pris en entree,
    s'arretant a l'argument lui meme, pouvant ainsi porduire une representation
    graphique de la fonction pour les valeurs extremales de l'argument et de son
    oppose.
    """

    resultat = inverse(X)
    print(resultat)

    pas = 1 / 1000
    x1 = 0
    x2 = -X

    #Tracer de la partie positive de la fonction inverse

    abscisse1 = []
    while x1 <= X:
        x1 += pas
        abscisse1.append(x1)
    ordonnee1 = []
    for value in abscisse1:
        ordonnee1.append(1 / value)

    graph1 = plt.plot(abscisse1, ordonnee1, "b-", lw=2.5)

    #Tracer de la partie negative de la fonction inverse

    abscisse2 = []
    while x2 <= 0:
        x2 += pas
        abscisse2.append(x2)
    ordonnee2 = []
    for value in abscisse2:
        ordonnee2.append(1 / value)

    graph2 = plt.plot(abscisse2, ordonnee2, "b-", lw=2.5)

    #Tracer de la fonction

    lim_x = 1+X
    lim_y = 2.71**X

    courbe1 = graph1
    courbe2 = graph2
    
    plt.title("Evolution de la fonction inverse")
    plt.rcParams["figure.figsize"] = (8, 8)
    plt.xlabel("abscisse")
    plt.ylabel("Inverse")
    plt.grid("equal", axis="both", color="k", lw=1.5)
    plt.axis([-lim_x, lim_x, -lim_y, lim_y])
    plt.show()
    plt.close()

    return courbe1, courbe2

    






__all__ = ['inverse', 'inverse1']