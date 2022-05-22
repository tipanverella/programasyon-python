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


def squares3(x):
    """
    Fonksyon sa aksepte yon grenn argument. Li pranl kom yon valeur
    maximal de yon serie de valeur ki pati de 0, pou rive nan valeur
    ou bay la. Li fe kalkil carre yo sou li, li remet ou yon lis de
    valeur au carre yo, et li bay yon graphe de valeur sa yo.
    """

    import matplotlib.pyplot as plt

    carre = [i**2 for i in range(x+1)]

    pas_abs = x / 100
    value_abs = 0
    abscisse = [value_abs]
    while value_abs <= x:
        value_abs += pas_abs
        abscisse.append(value_abs)
    
    abscisse.copy()
    ordonnee = [i**2 for i in abscisse]

    graph = plt.plot(abscisse, ordonnee, "k-*", lw=2.5)
    plt.title("Courbe d'evolution de la fonction carree")
    plt.xlabel("x values")
    plt.ylabel("squares")
    plt.grid("equal", axis="both", color="g", lw=2.5)
    plt.axis("equal" ,xmin=-100, xmax=100, ymin=-100, ymax=100)
    plt.legend()
    plt.show()
    plt.close()

    return carre, graph




def squares2(X)->dict:
    """
    Fonksyon sa li menm, baw repons yo sou forme
    dictionnaire. Li etabli correspondance ant valeur yo, ak carre yo.
    """
    return {x:x**2 for x in range(X+1)}

__all__ = ['squares', 'squares1', 'squares2']