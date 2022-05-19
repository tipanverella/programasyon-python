def inverse(x)->float:
    return(1/x)

def inverse1(x):
    fonction_inverse = 1/x
    return fonction_inverse

def inverse2(X = []):
    import matplotlib.pyplot as plt
    x = []
    y = []
    abscisse = 0
    for elem in X:
        pas = elem/50
        for idx in X:
            abscisse += pas 
            x.append(abscisse)
            y = [(1/valeur) for valeur in x]
    graph = plt.plot(x, y, "k-*", lw=1.5)
    plt.title("Fonction inverse")
    plt.rcParams["figure.figsize"] = (20, 18)
    plt.xlabel("abscisse")
    plt.ylabel("fonction_inverse")
    plt.grid("equal", axis="both")
    plt.show()
    plt.close()
    return graph

__all__ = ['inverse', 'inverse1']