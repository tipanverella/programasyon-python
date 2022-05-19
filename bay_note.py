import random as rdm

def bay_note(list_non):
    """
    Fonksyon sa bay elev note au hasard
    """
    i = 0
    Note = []
    for idx in list_non:
        note = rdm.randint(0, 21)
        i += 1
        Note.append(note)
    resultat = zip(list_non, Note)
    return resultat