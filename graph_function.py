"""
Module sa baw zouti pouw kalkule carre nonb ou vle a,
e li ka baw graph avek li tou.
"""

from matplotlib import pyplot as plt
from typing import List


def graph1(param_value) -> list[float]:
    """
    Fonction sa a manipuler done pou ou, de telles
    sortes keu ou kapab fe yon bon courbe ki approchee
    vrai courbe fonction ou an.
    """

    pas1 = param_value / 10000
    pas = round(pas1, 4)
    value1 = round(-param_value, 4)
    abscisse = [value1]
    while value1 <= param_value:
        value1 += pas
        abscisse.append(value1)

    return abscisse


def graph2(abscisse:list, ordonnee:list):
    """
    Fonction sa fe graphe pou ou.
    """

    title = input("Donnez le titre de votre graphique: ")
    x_label = input("Ki tit axe abscisse ou an: ")
    y_label = input("Ki tit axe ordonnee ou an: ")

    graph = plt.plot(abscisse, ordonnee, "k-", lw=2.5)
    plt.title(title)
    plt.rcParams["figure.figsize"] = (8, 8)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid("equal", axis="both", color="k", lw=1)
    plt.show()
    plt.close()

    return graph


if __name__ == "__main__":
    __all__ = ["graph1", "graph2"]
