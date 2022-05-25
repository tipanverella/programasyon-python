"""
Module dessaie
"""
import matplotlib.pyplot as plt
from energie_mecanique import li_dokuman

lecture = li_dokuman(file_path="/c/Users/dedea/git/programasyon-python")
transposed = zip(lecture)
print(transposed)


VALUE_A = 1 / 1000  # Pour éviter 0
VALUE_B = 1
x = []
y = []
x1 = []
y1 = []
PAS = (VALUE_B - VALUE_A) / 200
ABSCISSE = VALUE_A
for k in range(0, 201):  # On fait une seule boucle
    x.append(ABSCISSE)  # ABSCISSE représente les abscisses à droite de 0
    y.append(1 / ABSCISSE)
    x1.append(-ABSCISSE)  # -ABSCISSE représente les abscisses à gauche de 0
    y1.append(-1 / ABSCISSE)
    ABSCISSE += PAS
plt.plot(x, y, x1, y1)
plt.axis([-1, 1, -10, 10])
plt.show()
plt.close()
