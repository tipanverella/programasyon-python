"""
Ce programme vous permet de calculer l'energie mecanique d'un objet ou d'une
personne quelconque.
"""
from cProfile import label
import csv
import sys
from typing import Tuple, List
from matplotlib import pyplot as plt

GRAVITE = 9.81  # ATTRACTION DE LA PESANTEUR en Newton par Kilogramme


def done_sistem() -> Tuple[float, float, float]:
    """
    Kolekte done lan men utilizate a
    """
    masse = float(input("Donner la valeur de la masse de l'objet en Kilogramme : "))
    hauteur = float(
        input("Entrez l'altitude de l'objet par rapport au sol en metre : ")
    )
    vitesse = float(input("Entrez la vitesse de l'objet en metre par seconde : "))
    return masse, hauteur, vitesse


def energie_mecanique(
    masse: float, hauteur: float, vitesse: float
) -> Tuple[str, float]:
    """
    Cette fonction vous permet de calculer l'energie
    mecanique d'un systeme. Elle vous demande tout d'abord
    la valeur de la masse de l'objet en Kilogramme(Kg), son altitude qui doit etre
    en metre, puis celle de sa vitesse en metres par seconde(metre/s), ce
    qui lui permettra de calculer l'energie mecanique de l'objet en Joules(J).
    """
    kantite_eneji = 0.0
    if vitesse == 0 and hauteur > 0:
        kantite_eneji = masse * GRAVITE * hauteur
        tip_eneji = "Energie Potentielle"
    elif hauteur == 0 and vitesse > 0:
        kantite_eneji = (masse * (vitesse**2)) / 2
        tip_eneji = "Energie Cinetique"
    else:
        kantite_eneji = (masse * (vitesse**2)) / 2 + masse * GRAVITE * hauteur
        tip_eneji = "Energie Mecanique"
    return tip_eneji, kantite_eneji


def li_dokuman(file_path: str) -> List[Tuple[float, float, float]]:
    """
    Fonksyon sa a li done ki lan dokuman an
    """
    with open(file_path, "r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row)
            return [
                (float(row["masse"]), float(row["hauteur"]), float(row["vitesse"]))
                for row in reader
            ]


def transfome_struktu_done(ell: List[Tuple[float, float, float]]):
    """
    fonksyon sa a,  transfome yon list triple an 4 list ki gen menm longe ak
    list triple a.
    """
    if not ell:
        idx, masse, hauteur, vitesse = [], [], [], []
    else:
        idx = [i for i, _ in enumerate(ell)]
        rangee = list(zip(*ell))
        # changement de l'organisation des donnees
        # du fichier csv en une liste de trois "tuples"...
        masse, hauteur, vitesse = rangee
        masse = list(masse)
        hauteur = list(hauteur)
        vitesse = list(vitesse)
    return idx, masse, hauteur, vitesse


def calcul_energie_pour_graphes(
    idx: list, masse: list, hauteur: list, vitesse: list, /
):
    """
    Cette fonction effectue les calculs sur les valeurs donnees pour la
    masse, la hauteur et la vitesse de l'objet en question et renvoie des
    listes d'energie potentielle, cinetique et mecanique.
    """
    # fonction permettant de calculer
    # les energies potentielle, cinetique et mecanique.
    e_idx = idx
    e_pote = [energie_mecanique(_m, _h, 0)[1] for _m, _h in zip(masse, hauteur)]
    e_cine = [energie_mecanique(_m, 0, _v)[1] for _m, _v in zip(masse, vitesse)]
    e_meca = [
        energie_mecanique(_m, _h, _v)[1] for _m, _h, _v in zip(masse, hauteur, vitesse)
    ]
    return e_idx, e_pote, e_cine, e_meca


def etude_systeme(idx: list, e_potent: list, e_cine: list, e_mecan: list):
    """
    Cette fonction construis des graphiques.
    """
    plt.figure(figsize=(15,10), layout="constrained")
    graph_ep = plt.plot(idx, e_potent, "b-", lw=4, label="Energie Potentielle")
    graph_ec = plt.plot(idx, e_cine, "g-", lw=4, label="Energie Cinetique")
    graph_em = plt.plot(idx, e_mecan, "k-", lw=4, label="Energie Mecanique")
    plt.title("Evolution des energies")
    plt.xlabel("Valeurs indexes")
    plt.ylabel("Energies")
    plt.legend()
    plt.grid("equal", axis="both")
    plt.show()
    plt.close()
    return graph_ep, graph_ec, graph_em



def systeme_mecanique():
    """
    Command line interface for a mecanical system
    """
    chwa = input(
        """
        Voulez-vous:
        1) Calculer une energie mecanique
        2) Etudier un systeme mecanique
        q) Fermer la sequence
           ?
        """
    )
    while chwa not in ("1", "2", "q"):
        chwa = input(
            """
            Les options disponible sont 1, 2 ou q!
            Voulez-vous:
            1) Calculer une energie mecanique
            2) Etudier un systeme mecanique
            q) Fermer la sequence
               ?
            """
        )
    if chwa == "q":
        print("Oke! Fermeture de la sequence.")
        sys.exit()
    if chwa == "1":
        # fok li kalkule eneji mekanik lan
        masse, hauteur, vitesse = done_sistem()
        tip_eneji, kantite_eneji = energie_mecanique(masse, hauteur, vitesse)
        print(f"L'{tip_eneji} du systeme est {kantite_eneji} joules.")
    elif chwa == "2":
        # fok li ofri enteraksyon pou konprann yon sistem mekanik
        # 1. mande utilizate a non fichye ki gen done yo
        emplacement_fichye_a = input("Kote done yo ye? ")
        # 2. li fichye a ak fonksyon li_dokuman e anrejistre rezulta yo lan yon
        # list
        done_list = li_dokuman(emplacement_fichye_a)
        # 3. transfome list la ak fonksyon transfome_struktu_done e mete rezulta
        idx, masse, hauteur, vitesse = transfome_struktu_done(done_list)
        # yo lan idx, masse, hauteur, vitesse
        idx, e_potent, e_cine, e_mecan = calcul_energie_pour_graphes(
            idx, masse, hauteur, vitesse
        )
        graph_ep, graph_ec, graph_em = etude_systeme(idx, e_potent, e_cine, e_mecan)
        print("Voila vos graphiques! Bonne analyse!")
    else:
        pass
    
    return graph_ep, graph_ec, graph_em


if __name__ == "__main__":
    systeme_mecanique()
