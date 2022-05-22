"""
Module sa baw des fonction ki pou kalkule carre nonb,
e fe graph.
"""

import matplotlib.pyplot as plt
from graph_function import graph1, graph2


def squares(arg_x):
    """
    fonksyon sa baw yon list de carre tout valeur
    ki inferieur a sa ou ba li a, rive nan saw bay la.
    """
    return arg_x**2


def squares1(arg_x):
    """
    This function calculate the square value of
    any number that u give
    """

    carre = [(i**2) for i in range(arg_x + 1)]

    abscisse = graph1(arg_x)

    ordonnee = [(i**2) for i in abscisse]

    graph = graph2(abscisse, ordonnee)

    return carre, graph
    

def squares2(param) -> dict:
    """
    Fonksyon sa li menm, baw repons yo sou forme
    dictionnaire. Li etabli correspondance ant valeur yo, ak carre yo.
    """
    return {arg_x: arg_x**2 for arg_x in range(param + 1)}


def squares3(arg_x):
    """
    Fonksyon sa aksepte yon grenn argument. Li pranl kom yon valeur
    maximal de yon serie de valeur ki pati de 0, pou rive nan valeur
    ou bay la. Li fe kalkil carre yo sou li, li remet ou yon lis de
    valeur au carre yo, et li bay yon graphe de valeur sa yo.
    """

    carre = [i**2 for i in range(arg_x + 1)]
    print(carre)

    pas_abs = arg_x / 10000
    value_abs = -arg_x
    abscisse = [value_abs]
    while value_abs <= arg_x:
        value_abs += pas_abs
        abscisse.append(value_abs)

    ordonnee = [i**2 for i in abscisse]

    graph = plt.plot(abscisse, ordonnee, "k-", lw=2.5)
    plt.title("Courbe d'evolution de la fonction carree")
    plt.xlabel("arg_x values")
    plt.ylabel("squares")
    plt.grid("equal", axis="both", color="k", lw=1)
    plt.rcParams["figure.figsize"] = (6, 6)
    plt.axis([-arg_x, arg_x, 0, carre[-1]])
    plt.show()
    plt.close()

    return graph


if __name__ == "__main__":
    __all__ = ["squares", "squares1", "squares2", "squares3"]
