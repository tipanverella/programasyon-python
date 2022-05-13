from energie_mecanique import (
    energie_mecanique,
    GRAVITE,
    transfome_struktu_done,
    calcul_energie_pour_graphes,
)


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


def test_calcul_energie_pour_graphes():
    idx = [0]
    masse = [0]
    hauteur = [0]
    vitesse = [0]
    e_idx, e_pote, e_cine, e_meca = calcul_energie_pour_graphes(
        idx, masse, hauteur, vitesse
    )
    assert e_idx == idx
    assert e_pote == [0.0]
    assert e_cine == [0.0]
    assert e_meca == [0.0]


def test_transfome_struktu_done():
    ell = [(1.0, 2.0, 3.0)]
    idx, masse, hauteur, vitesse = transfome_struktu_done(ell)
    assert idx == [
        0,
    ]
    assert masse == [
        1.0,
    ]
    assert hauteur == [
        2.0,
    ]
    assert vitesse == [
        3.0,
    ]

    ell = [(1.0, 2.0, 3.0), (7.0, 8.0, 9.0), (4.0, 5.0, 6.0)]
    idx, masse, hauteur, vitesse = transfome_struktu_done(ell)
    assert idx == [0, 1, 2]
    assert masse == [1.0, 7.0, 4.0]
    assert hauteur == [2.0, 8.0, 5.0]
    assert vitesse == [3.0, 9.0, 6.0]

    ell = []
    idx, masse, hauteur, vitesse = transfome_struktu_done(ell)
    assert idx == []
    assert masse == []
    assert hauteur == []
    assert vitesse == []
