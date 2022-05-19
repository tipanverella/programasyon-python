def squares(x):
    carre = [i**2 for i in range(x+1)]
    return carre


def squares1(x):
    return(x**2)


def squares2(X)->dict:
    return {x:x**2 for x in range(X+1)}