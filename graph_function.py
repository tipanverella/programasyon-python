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

    pas1 = x[-1] / 100
    value1 = x[0]
    abscisse = [value1]
    while value1 != x[-1]:
        value1 += pas1
        abscisse.append(value1)

    pas2 = y[-1]/ 100
    value2 = y[0]
    ordonnee = [value2]
    while value2 != y[-1]:
        value2 += pas2
        ordonnee.append(value2)

    plt.plot(abscisse, ordonnee, "k-", lw=2.5)
    plt.title(title)
    plt.rcParams["figure.figsize"] = (10, 8)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid("equal", axis="both", color="g", lw=2.5)
    plt.axis("equal" ,xmin=-100, xmax=100, ymin=-100, ymax=100)
    plt.legend()
    plt.show()
    plt.close()

    
    

        
