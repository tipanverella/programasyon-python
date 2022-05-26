"""
Module sa baw zouti pouw kalkule carre nonb ou vle a,
e li ka baw graph avek li tou.
"""

from matplotlib import pyplot as plt
from typing import List
import sys

def graph1(param_value, *, start_seq:float = None, stop_seq:float = None) -> list[float]:
    """
    Fonction sa a manipuler done pou ou, de telles
    sortes keu ou kapab fe yon bon courbe ki approchee
    vrai courbe fonction ou vle graf la.
    """
    
    #checking the type of the parameter value

    try:
        do = type(param_value) == int or float
        do1 = type(param_value) == list
    except TypeError:
        pass
    
    #defining the shorter interval between two points

    if do == True:
        pas = param_value / 10000
        value1 = round(-param_value, 4)
    elif do1 == True:
        try:
            pas = (param_value[-1] - param_value[0]) / 10000
            value1 = round(-param_value[-1], 4)
        except IndexError:
            print("Ouppsss....your list doesn't have enough elements.")
            sys.exit()
    else:
        raise TypeError
    
    #redefining the parameter value

    if type(param_value) == list:
        param_value = param_value[-1]
    
    pas = round(pas, 4)
    abscisse = []

    #nan pati sa nap defini valeur keu lsite abscisse
    #la ap gen ladann

    if start_seq != None and stop_seq != None:
        value1 = start_seq
        while value1 >= start_seq and value1 <= stop_seq:
            value1 += pas
            value1 = round(value1, 5)
            abscisse.append(value1)

    elif start_seq != None and stop_seq == None:
        value1 = start_seq
        while value1 <= param_value:
            value1 += pas
            value1 = round(value1, 5)
            abscisse.append(value1)

    elif start_seq == None and stop_seq != None:
        while value1 <= stop_seq:
            value1 += pas
            value1 = round(value1, 5)
            abscisse.append(value1)

    else:
        while value1 <= param_value:
            value1 += pas
            value1 = round(value1, 5)
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
 