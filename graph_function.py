"""
Module sa baw zouti pouw fe yon bon graph.
"""

import sys
from matplotlib import pyplot as plt


def graph1(
    param_value, *, start_seq: float = None, stop_seq: float = None
) -> list[float]:
    """
    Fonction sa a manipuler done pou ou, de telles
    sortes keu ou kapab fe yon bon courbe ki approchee
    vrai courbe fonction ou vle graf la.
    """

    # checking the type of the parameter value

    try:
        do1 = isinstance(param_value, int or float)
        do2 = isinstance(param_value, list)
    except TypeError:
        pass

    # nap defini pi piti interval ki separe 2 points

    if do1 is True:
        pas = param_value / 10000
        value1 = round(-param_value, 4)
    elif do2 is True:
        param_value = param_value[-1]
        try:
            pas = (param_value[-1] - param_value[0]) / 10000
            value1 = round(-param_value[-1], 4)
        except IndexError:
            print("Ouppsss....your list doesn't have enough elements. Kind of empty!")
            sys.exit()

    # redefining the parameter value

    pas = round(pas, 4)
    abscisse = []

    # nan pati sa nap defini valeur keu liste abscisse
    # la ap gen ladann

    if start_seq is not None and stop_seq is not None:
        value1 = start_seq
        while start_seq <= value1 < stop_seq:
            value1 += pas
            value1 = round(value1, 5)
            abscisse.append(value1)

    elif start_seq is not None and stop_seq is None:
        value1 = start_seq
        abscisse.append(value1)
        while value1 < param_value:
            value1 += pas
            value1 = round(value1, 5)
            abscisse.append(value1)

    elif start_seq is None and stop_seq is not None:
        while value1 < stop_seq:
            value1 += pas
            value1 = round(value1, 5)
            abscisse.append(value1)

    else:
        while value1 < param_value:
            value1 += pas
            value1 = round(value1, 5)
            abscisse.append(value1)

    return abscisse


def graph2(
    abscisse: list, ordonnee: list, abscisse1: list = None, ordonnee1: list = None
):
    """
    Fonction sa fe graphe pou ou.
    """

    title = input("Donnez le titre de votre graphique: ")
    x_label = input("Ki tit axe abscisse ou an: ")
    y_label = input("Ki tit axe ordonnee ou an: ")

    graph = plt.plot(abscisse, ordonnee, "k-", lw=2.5)

    if abscisse1 is not None and ordonnee1 is not None:
        subgraph = plt.plot(abscisse1, ordonnee1, "k-", lw=2.5)
    else:
        subgraph = None

    plt.title(title)
    plt.rcParams["figure.figsize"] = (8, 8)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid("equal", axis="both", color="k", lw=1)
    plt.show()
    plt.close()

    return graph, subgraph


if __name__ == "__main__":
    __all__ = ["graph1", "graph2"]
