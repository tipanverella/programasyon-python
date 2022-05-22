from itertools import zip_longest

from energie_mecanique import li_dokuman

lecture = li_dokuman(file_path="/c/Users/dedea/git/programasyon-python")
transposed = zip_longest[lecture]
print(transposed)



if x <= 465:
    pas_abs = x / 1000
    value_abs1 = -x
    value_abs2 = 1 / 1000
elif x <= :




import matplotlib.pyplot as plt

a = 1 / 1000 # Pour éviter 0
b = 1
x = []
y = []
x1 = []
y1 = []
pas = (b - a) / 200
abscisse = a
for k in range(0, 201): # On fait une seule boucle
    x.append(abscisse) # abscisse représente les abscisses à droite de 0
    y.append(1 / abscisse)
    x1.append(-abscisse) # -abscisse représente les abscisses à gauche de 0
    y1.append(-1 / abscisse)
    abscisse += pas
plt.axis([-1, 1, -10, 10])
plt.plot(x, y, x1, y1)
plt.show()
plt.close()
