def inverse(x)->float:
    """
    Fonction sa a kalkule inverse nonb ou ba li an
    """
    return(1/x)




def inverse1(x):
    fonction_inverse = 1/x
    return fonction_inverse




def inverse2(X):
    """
    Fonction sa kapab kalkule inverse yon nonb 
    ou bali.
    Apre sa, li kapab baw yon graph...
    """
    import matplotlib.pyplot as plt
    
    x = 0
    pas_abs = X / 1000
    Inverse = []

    while x <= X:
        x += pas_abs
        inverse = (1 / x)
        Inverse.append(inverse)
    
    value_abs1 = -x
    value_abs2 = 1 / 1000

    abscisse1 = [value_abs1]

    while value_abs1 <= -value_abs2:
        value_abs1 += pas_abs
        abscisse1.append(value_abs1)
    
    
    abscisse2 = [value_abs2]

    while value_abs2 <= x:
        value_abs2 += pas_abs
        abscisse2.append(value_abs2)

    ordonnee1 = [(1 / i) for i in abscisse1]
    ordonnee2 = [(1 / i) for i in abscisse2]

    graph1 = plt.plot(abscisse1, ordonnee1, "r-", lw=2.5)
    graph2 = plt.plot(abscisse2, ordonnee2, "r-", lw=2.5)
    plt.title("Courbe d'evolution de la fonction inverse")
    plt.xlabel("X values")
    plt.ylabel("inverse")
    plt.grid("equal", axis="both", color="k", lw=1)
    plt.rcParams["figure.figsize"] = (8, 8)
    plt.axis([-x, x, -x, x])
    plt.show()
    plt.close()
    return graph1, graph2


__all__ = ['inverse', 'inverse1']