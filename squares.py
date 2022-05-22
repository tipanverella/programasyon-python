def squares(x):
    """
    fonksyon sa baw yon list de carre tout valeur 
    ki inferieur a sa ou ba li a, rive nan saw bay la.
    """
    return(x**2)



def squares1(x):
    """
    This function calculate the square value of 
    any number that u give
    """
    carre = [i**2 for i in range(x+1)]
    return carre



def squares2(X)->dict:
    """
    Fonksyon sa li menm, baw repons yo sou forme
    dictionnaire. Li etabli correspondance ant valeur yo, ak carre yo.
    """
    return {x:x**2 for x in range(X+1)}

__all__ = ['squares', 'squares1', 'squares2']



def squares3(x):
    """
    Fonksyon sa aksepte yon grenn argument. Li pranl kom yon valeur
    maximal de yon serie de valeur ki pati de 0, pou rive nan valeur
    ou bay la. Li fe kalkil carre yo sou li, li remet ou yon lis de
    valeur au carre yo, et li bay yon graphe de valeur sa yo.
    """

    import matplotlib.pyplot as plt

    carre = [i**2 for i in range(x+1)]
    print(carre)

    pas_abs = x / 10000
    value_abs = -x
    abscisse = [value_abs]
    while value_abs <= x:
        value_abs += pas_abs
        abscisse.append(value_abs)
    
    ordonnee = [i**2 for i in abscisse]

    graph = plt.plot(abscisse, ordonnee, "k-", lw=2.5)
    plt.title("Courbe d'evolution de la fonction carree")
    plt.xlabel("x values")
    plt.ylabel("squares")
    plt.grid("equal", axis="both", color="k", lw=1)
    plt.rcParams["figure.figsize"] = (6, 6)
    plt.axis([-x, x, 0, carre[-1]])
    plt.show()
    plt.close()

    return graph
