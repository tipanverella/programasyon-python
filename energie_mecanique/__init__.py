"""
Ce programme vous permet de calculer l'energie mecanique d'un objet ou d'une
personne quelconque.
"""
import csv
from itertools import zip_longest
import sys
from typing import Tuple, List
import matplotlib.pyplot as plt

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
        return [
            (float(row["masse"]), float(row["hauteur"]), float(row["vitesse"]))
            for row in reader
        ]


def reformattage(ell: List[Tuple[float, float, float]]):
    """
    fonksyon sa a,  transfome yon list triple an 4 list ki gen menm longe ak
    list triple a.
    """
    rangee = zip(ell)
    # changement de l'organisation des donnees
    # du fichier csv en une liste de trois "tuples"...
    transposed = [[idx, elem] for idx, elem in rangee]
    idx = [list(ell)]
    masse = [transposed[0]]
    hauteur = [transposed[1]]
    vitesse = [transposed[2]]
    return idx, masse, hauteur, vitesse


def calcul_energie_pour_graphes(idx: list, masse: list, hauteur: list, vitesse: list):
    """
    ette fonction effectue les calculs sur les valeurs donnees pour la
    masse, la hauteur et la vitesse de l'objet en question et renvoie des
    listes d'energie potentielle, cinetique et mecanique.
    """
    # fonction permettant de calculer
    # les energies potentielle, cinetique et mecanique.
    e_potent = [(i * GRAVITE * k) for i in masse for k in hauteur]
    e_cine = [(i * (v**2) / 2) for i in masse for v in vitesse]
    e_mecan = [(i + g) for i in e_potent for g in e_cine]
    return idx, e_potent, e_cine, e_mecan


def etude_systeme(idx: list, e_potent: list, e_cine: list, e_mecan: list):
    """
    Cette fonction construis des graphiques.
    """
    graph_ep = plt.plot(idx, e_potent, "b-", lw=4)
    graph_ec = plt.plot(idx, e_cine, "g-", lw=4)
    graph_em = plt.plot(idx, e_mecan, "k-", lw=4)
    plt.title("Evolution des energies")
    plt.rcParams["figure.figsize"] = (20, 15)
    plt.xlabel("Valeurs indexes")
    plt.ylabel("Energies")
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
        # pylint: disable = no-value-for-parameter   # Disables the pylint check for the next line
        idx, masse, hauteur, vitesse = reformattage()
        idx, e_potent, e_cine, e_mecan = calcul_energie_pour_graphes(
            idx, masse, hauteur, vitesse
        )
        graph_ep, graph_ec, graph_em = etude_systeme(idx, e_potent, e_cine, e_mecan)
        print(graph_ep, graph_ec, graph_em, "Voila vos graphiques! Bonne analyse!")
        print("Energie mecanique en noir,")
        print("Energie cinetique en vert,")
        print("Energie potentielle en bleu.")
    else:
        pass


if __name__ == "__main__":
    systeme_mecanique()
