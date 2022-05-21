from typing import List
from matplotlib import pyplot as plt

def graphe(x = [], y = []):
    """
    Cette fonction cree des graphes en 
    fonction des donnees qui lui sont 
    transmises.
    """

    title = input("Donnez le titre de votre graphique: ")
    x_label = input("Ki tit axe abscisse ou an: ")
    y_label  = input("Ki tit axe ordonnee ou an: ")
    graph = plt.plot(x, y, "k-", lw=2.5)
    plt.title(title)
    plt.rcParams["figure.figsize"] = (20, 18)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid("equal", axis="both")
    plt.show()
    plt.close()
    return graph


