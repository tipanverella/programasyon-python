import matplotlib.pyplot as plt


def energie_mecanique() -> float:
    """Cette fonction vous permet de caculer l'energie
    mecanique d'un systeme. Elle vous demande tout d'abord
    la valeur de la masse de l'objet en Kilogramme(Kg), son altitude qui doit etre en metre(m),
    puis celle de sa vitesse en metres par seconde(m/s), ce qui lui permettra de calculer
    l'energie mecanique de l'objet en Joules(J).
    """
    m = float(input("Donner la valeur de la masse de l'objet en Kilogramme: "))
    h = float(input("Entrez l'altitude de l'objet par rapport au sol en metre: "))
    v = float(input("Entrez la vitesse de l'objet en metre par seconde: "))
    g = 9.81  # ATTRACTION DE LA PESANTEUR en Newton par Kilogramme
    if v == 0:
        energie_potentielle = m * g * h
        print(f"L'energie potentielle du systeme est {energie_potentielle} Joules.")
    elif h == 0:
        energie_cinetique = m * v**2
        print(f"L'energie cinetique du systeme est {energie_cinetique} Joules.")
    else:
        energie_mecanique = m * v**2 + m * g * h
        print(f"L'energie mecanique du systeme est {energie_mecanique} Joules.")

    ask = str(input("Voulez vous un graphique du systeme?: "))
    ask.lower
    if ask in ("y", "yes", "oui"):
        """Cette partie de la fonction permet de construire un graphe en
        fonction des donnees de la premiere partie, mais pour cela il va devoir
        vous demander des informations supplementaires, qui lui permettront de
        de calculer des valeurs d'energies supplementaires, afin d'en creer
        une liste et ainsi faire le graphique.
        Les axes a representer seront l'axe des abscisses sur lequel sera
        represente l'evolution du temps, et l'axe des ordonnees, qui representera
        les energies en question.
        """
        EP = []  # liste d'energie potentielle
        EC = []  # liste d'energie cinetique
        EM = []  # liste d'energie mecanique
        H = [h]  # liste d'altitude
        V = [v]  # liste de vitesse
        ask2 = str(
            input(
                "Voulez-vous avoir un graphe pour l'energie potentielle de l'objet?  "
            )
        )
        ask2.lower
        ask3 = str(
            input("Voulez-vous avoir un graphe pour l'energie cinetique de l'objet?  ")
        )
        ask3.lower
        ask4 = str(
            input("Voulez-vous avoir un graphe pour l'energie mecanique de l'objet?  ")
        )
        ask4.lower
        demand = int(
            input(
                "Combien de valeurs supplementaires voulez vous donner pour l'altitude et la vitesse de l'objet?  "
            )
        )
        T = []  # liste de temps generee
        t = 0
        while t <= demand:
            T.append(t)
            t += 1

        if ask2 in ("y", "yes", "oui"):

            def graph_epp():
                a = 0
                while a < demand:
                    a += 1
                    h1 = int(input("Entrez l'altitude de l'objet par rapport au sol: "))
                    H.append(h1)
                print(f"Voici la liste des altitudes donnee: {H}.")
                for k in H:
                    ep = m * g * k
                    EP.append(ep)
                print(f"Voici la liste des energies potentielles calculees: {EP}.")
                plt.plot(T, EP, "b*-", lw=4)
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

        if ask3 in ("y", "yes", "oui"):

            def graph_ec():
                list_vit = []
                a = 0
                while a < demand:
                    a += 1
                    v1 = int(input("Entrez la vitesse de l'objet: "))
                    V.append(v1)
                print(f"Voici la liste de vitesses donnee: {V}.")
                for i in V:
                    ec = (m * (i**2)) / 2
                    EC.append(ec)
                print(f"Voici la liste des energies cinetiques calculees: {EC}.")
                plt.plot(T, EP, "g*-", lw=4)
                plt.title("Evolution de l'energie cinetique en fonction du temps")
                plt.rcParams["figure.figsize"] = (10, 8)
                plt.xlabel("Temps")
                plt.ylabel("Energie cinetique")
                plt.grid("equal", axis="both")
                plt.show()
                plt.close()

            if __name__ == "__main__":
                graph_ec()

        if ask4 in ("y", "yes", "oui"):
            for k in range(demand + 1):
                em = EP[k] + EC[k]
                EM.append(em)
            print(f"Voici la liste des energies mecaniques obtenues: {EM}.")
            plt.plot(T, EM, "k*10-", lw=4)
            plt.title("L'evolution de l'energie mecanique en fonction du temps")
            plt.rcParams["figure.figsize"] = (10, 8)
            plt.xlabel("Temps")
            plt.ylabel("Energie mecanique")
            plt.grid("equal", axis="both")
            plt.show()
            plt.close()
    else:
        pass


if __name__ == "__main__":
    energie_mecanique()
