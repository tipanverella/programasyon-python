from energie_mecanique import energie_mecanique, GRAVITE


def test_energie_mecanique():
    masse = 0
    hauteur = 0
    vitesse = 0
    tip_eneji, kantite_eneji = energie_mecanique(masse, hauteur, vitesse)
    assert kantite_eneji == 0
    assert tip_eneji == "Energie Mecanique"

    masse = 1
    hauteur = 1
    vitesse = 0
    tip_eneji, kantite_eneji = energie_mecanique(masse, hauteur, vitesse)
    assert kantite_eneji == GRAVITE
    assert tip_eneji == "Energie Potentielle"

    masse = 1
    hauteur = 0
    vitesse = 1
    tip_eneji, kantite_eneji = energie_mecanique(masse, hauteur, vitesse)
    assert kantite_eneji == 0.5
    assert tip_eneji == "Energie Cinetique"

    masse = 0
    hauteur = 1
    vitesse = 1
    tip_eneji, kantite_eneji = energie_mecanique(masse, hauteur, vitesse)
    assert kantite_eneji == 0
    assert tip_eneji == "Energie Mecanique"
