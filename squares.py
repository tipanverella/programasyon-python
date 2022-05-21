def squares1(x):
    """
    This function calculate the square value of 
    any number that u give
    """
    carre = [i**2 for i in range(x+1)]
    X = [i for i in range(x+1)]
    from graph_function import graphe
    graph = graphe(X, carre)
    return carre, graph


def squares(x):
    """
    fonksyon sa baw yon list de carre tout valeur 
    ki inferieur a sa ou ba li a, rive nan saw bay la.
    """
    return(x**2)



def squares2(X)->dict:
    """
    Fonksyon sa li menm, baw repons yo sou forme
    dictionnaire. Li etabli correspondance ant valeur yo, ak carre yo.
    """
    return {x:x**2 for x in range(X+1)}

__all__ = ['squares', 'squares1', 'squares2']