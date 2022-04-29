"""Ce programme vous permet de calculer l'energie mecanique d'un objet ou d'une
personne quelconque.
"""
import sys
import csv
from glob import glob
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
    masse = float(input("Donner la valeur de la masse de l'objet en Kilogramme: "))
    hauteur = float(input("Entrez l'altitude de l'objet par rapport au sol en metre: "))
    vitesse = float(input("Entrez la vitesse de l'objet en metre par seconde: "))
    tip_eneji = ""
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


def li_dokuman(filename: str) -> List[Tuple[float, float, float]]:
    """
    Fonksyon sa a li done ki lan dokuman an
    """
    with open(filename, "r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        return [
            (float(row["masse"]), float(row["hauteur"]), float(row["vitesse"]))
            for row in reader
        ]


def lot_fonksyon():
    ask = input("Voulez-vous un graphique du systeme?: ")
    if ask in ("y", "yes", "oui"):
        # Cette partie de la fonction permet de construire un graphe en
        # fonction des donnees de la premiere partie, mais pour cela il va devoir
        # vous demander des informations supplementaires, qui lui permettront de
        # de calculer des valeurs d'energies supplementaires, afin d'en creer
        # une liste et ainsi faire le graphique.
        # Les axes a representer seront l'axe des abscisses sur lequel sera
        # represente l'evolution du temps, et l'axe des ordonnees, qui
        # representera les energies en question.

        e_potent = []  # liste d'energie potentielle
        e_cine = []  # liste d'energie cinetique
        e_mecan = []  # liste d'energie mecanique
        altitude = [hauteur]  # liste d'altitude
        celerite = [vitesse]  # liste de vitesseitesse
        reponse = ["y", "yes", "oui"]
        ask2 = input(
            "Voulez-vous avoir un grapre pour l'energie potentielle de l'objet?"
        )
        ask3 = input(
            "Voulez-vous avoir un grape pour l'energie cinetique de l'objet?  "
        )
        ask4 = input(
            "Voulez-vous avoir un graphe pour l'energie mecanique de l'objet?  "
        )
        demand = int(
            input(
                "Combien de valeurs supplementaires voulez-vous donner pour l'altitude"
                "et la vitesse de l'objet?"
            )
        )
        temps = []  # liste de temps
        temps1 = 0
        while temps1 <= demand:
            temps.append(temps)
            temps1 += 1

        if ask2 in reponse:

            def graph_epp():
                avancement = 0
                while avancement < demand:
                    avancement += 1
                    hauteur1 = int(
                        input("Entrez l'altitude de l'objet par rapport au sol: ")
                    )
                    altitude.append(hauteur1)
                print(f"Voici la liste des altitudes donnee: {altitude}.")
                for k in altitude:
                    energie_potentielle = masse * GRAVITE * k
                    e_potent.append(energie_potentielle)
                print(
                    f"Voici la liste des energies potentielles calculees: {e_potent}."
                )
                plt.plot(temps, e_potent, "b-", lw=4)
                plt.title(
                    "Evolution de l'energie potentielle de pesanteur en fonction du temps"
                )
                plt.rcParams["figure.figsize"] = (10, 8)
                plt.xlabel("Temps")
                plt.ylabel("Energie potentielle de pesanteur")
                plt.grid("equal", axis="both")
                plt.show()
                plt.close()

            if __name__ == "__main__":
                graph_epp()

        if ask3 in reponse:

            def graph_ec():
                avancement = 0
                while avancement < demand:
                    avancement += 1
                    vitesse1 = int(input("Entrez la vitesse de l'objet: "))
                    celerite.append(vitesse1)
                print(f"Voici la liste de vitesses donnee: {celerite}.")
                for i in celerite:
                    energie_cinetique = (masse * (i**2)) / 2
                    e_cine.append(energie_cinetique)
                print(f"Voici la liste des energies cinetiques calculees: {e_cine}.")
                plt.plot(temps, e_cine, "g-", lw=4)
                plt.title("Evolution de l'energie cinetique en fonction du temps")
                plt.rcParams["figure.figsize"] = (10, 8)
                plt.xlabel("Temps")
                plt.ylabel("Energie cinetique")
                plt.grid("equal", axis="both")
                plt.show()
                plt.close()

            if __name__ == "__main__":
                graph_ec()

        if ask4 in reponse:
            for k in range(demand + 1):
                e_mecan = e_potent[k] + e_cine[k]
                e_mecan.append(energie_mecanique)
            print(f"Voici la liste des energies mecaniques obtenues: {e_mecan}.")
            plt.plot(temps, e_mecan, "k-", lw=4)
            plt.title("L'evolution de l'energie mecanique en fonction du temps")
            plt.rcParams["figure.figsize"] = (10, 8)
            plt.xlabel("Temps")
            plt.ylabel("Energie mecanique")
            plt.grid("equal", axis="both")
            plt.show()
            plt.close()
    else:
        pass


def sistem_mekanik():
    """
    Command line interface for a mecanical system
    """
    chwa = input(
        """
        Eske ou vle:
        1) kalkule yon eneji mekanik
        2) etudye yon sistem mekanik
        q) femen program la
        ?
        """
    )
    while chwa not in ("1", "2", "q"):
        chwa = input(
            """
            Opsyon yo se 1, 2 ou q!
            Eske ou vle:
            1) kalkule yon eneji mekanik
            2) etudye yon sistem mekanik
            q) femen program la
            ?
            """
        )
    if chwa == "q":
        print("Oke! Map femen program la.")
        sys.exit()
    if chwa == "1":
        # fok li kalkule eneji mekanik lan
        tip_eneji, kantite_eneji = energie_mecanique()
        print(f"L'{tip_eneji} du systeme est {kantite_eneji} joules.")
    elif chwa == "2":
        # fok li ofri enteraksyon pou konprann yon sistem mekanik
        non_dokuman_an = input("Banm non dokuman ki gen done sou sistem lan: ")
        if non_dokuman_an not in glob("*"):
            print("Dokuman ou a pa la, map jete m!")
            sys.exit()
        done_sistem = li_dokuman(non_dokuman_an)
    else:
        pass


if __name__ == "__main__":
    sistem_mekanik()
