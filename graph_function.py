from matplotlib import pyplot as plt

def graphe(x = []):
    """
    Fonction sa a manipuler done pou ou, de telles
    sortes keu ou kapab fe yon bon courbe ki approchee
    vrai courbe fonction ou an.
    """

    pas1 = x[-1] / 100
    value1 = x[0]
    abscisse = [value1]
    while value1 != x[-1]:
        value1 += pas1
        abscisse.append(value1)
    
    return abscisse


def graph2(abscisse, ordonnee):
    """
    Fonction sa fe graphe pou ou.
    """

    title = input("Donnez le titre de votre graphique: ")
    x_label = input("Ki tit axe abscisse ou an: ")
    y_label  = input("Ki tit axe ordonnee ou an: ")

    plt.plot(abscisse, ordonnee, "k-", lw=2.5)
    plt.title(title)
    plt.rcParams["figure.figsize"] = (10, 8)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid("equal", axis="both", color="g", lw=2.5)
    plt.axis("equal", [abscisse[0], abscisse[-1], ordonnee[0], ordonnee[-1]])
    plt.show()
    plt.close()

    
    

        
