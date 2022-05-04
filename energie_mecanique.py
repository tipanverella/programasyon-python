"""Ce programme vous permet de calculer l'energie mecanique d'un objet ou d'une
personne quelconque.
"""
import csv
import sys
from typing import Tuple, List
import matplotlib.pyplot as plt

GRAVITE = 9.81  # ATTRACTION DE LA PESANTEUR en Newton par Kilogramme


def energie_mecanique() -> Tuple[float, float]:
    """Cette fonction vous permet de calculer l'energie
    mecanique d'un systeme. Elle vous demande tout d'abord
    la valeur de la masse de l'objet en Kilogramme(Kg), son altitude qui doit etre
    en metre, puis celle de sa vitesse en metres par seconde(metre/s), ce
    qui lui permettra de calculer l'energie mecanique de l'objet en Joules(J).
    """
    masse = float(input("Donner la valeur de la masse de l'objet en Kilogramme : "))
    hauteur = float(
        input("Entrez l'altitude de l'objet par rapport au sol en metre : ")
    )
    vitesse = float(input("Entrez la vitesse de l'objet en metre par seconde : "))
    kantite_eneji = 0.0
    if vitesse == 0:
        kantite_eneji = masse * GRAVITE * hauteur
        tip_eneji = "Energie Potentielle"
    elif hauteur == 0:
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


altitude = []  # liste d'altitude
celerite = []  # liste de vitesse


def recueil_donne():
    """Cette partie de la fonction permet de construire un graphe en
    fonction des donnees de la premiere partie, mais pour cela il va devoir
    vous demander des informations supplementaires, qui lui permettront de
    de calculer des valeurs d'energies supplementaires, afin d'en creer
    une liste et ainsi faire le graphique.
    Les axes a representer seront l'axe des abscisses sur lequel sera
    represente l'evolution du temps, et l'axe des ordonnees, qui
    representera les energies en question.
    """
    demand = int(
        input(
            "Combien de valeurs voulez-vous donner pour l'altitude"
            " et la vitesse de l'objet? : "
        )
    )
    e_potent = []  # liste d'energie potentielle
    e_cine = []  # liste d'energie cinetique
    e_mecan = []  # liste d'energie mecanique
    temps = []  # liste de temps
    temps1 = 0
    while temps1 < demand:
        temps.append(temps1)
        temps1 += 1
    masse = float(input("Donner la valeur de la masse de l'objet en Kilogramme : "))
    avancement = 0
    while avancement < demand:
        avancement += 1
        hauteur1 = float(input("Entrez l'altitude de l'objet par rapport au sol : "))
        altitude.append(hauteur1)
        vitesse1 = float(input("Entrez la vitesse de l'objet : "))
        celerite.append(vitesse1)
    for i in altitude:
        kantite_eneji = masse * GRAVITE * i
        e_potent.append(kantite_eneji)
    for i in celerite:
        kantite_eneji = (masse * (i**2)) / 2
        e_cine.append(kantite_eneji)
    for i in range(demand):
        kantite_eneji = e_potent[i] + e_cine[i]
        e_mecan.append(kantite_eneji)
    return temps, e_potent, e_cine, e_mecan


def etude_syst():
    """
    Cette fonction construis des graphiques.
    """
    temps, e_potent, e_cine, e_mecan = recueil_donne()
    graph_ep = plt.plot(temps, e_potent, "b-", lw=4)
    graph_ec = plt.plot(temps, e_cine, "g-", lw=4)
    graph_em = plt.plot(temps, e_mecan, "k-", lw=4)
    plt.title("Evolution des energies")
    plt.rcParams["figure.figsize"] = (10, 8)
    plt.xlabel("Temps")
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
        tip_eneji, kantite_eneji = energie_mecanique()
        print(f"L'{tip_eneji} du systeme est {kantite_eneji} joules.")
    elif chwa == "2":
        # fok li ofri enteraksyon pou konprann yon sistem mekanik
        graph_ep, graph_ec, graph_em = etude_syst()
        print(graph_ep, graph_ec, graph_em, "Voila vos graphiques! Bonne analyse!")
        print("Energie mecanique en noir,")
        print("Energie cinetique en vert,")
        print("Energie potentielle en bleu.")
    else:
        pass


if __name__ == "__main__":
    systeme_mecanique()
