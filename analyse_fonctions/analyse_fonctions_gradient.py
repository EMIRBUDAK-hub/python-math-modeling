# TP Probabilités — Code complété avec commentaires indiquant les questions

import math
import random as rd
import numpy as np
from scipy.stats import binom, geom, uniform
import matplotlib.pyplot as plt

###############################################################
# Question I.1 : fonction renvoyant les coefficients binomiaux
###############################################################
def Q_I_1(n):
    return [math.comb(n, k) for k in range(n+1)]

###############################################################
# Question I.2 : test de Q_I_1 pour n de 2 à 5
###############################################################
for n in range(2, 6):
    print(f"Coefficients pour n={n} :", Q_I_1(n))

###############################################################
# Question I.3 : fonction générant n tirages d'une urne 1..6
###############################################################
def Q_I_3(n):
    return [rd.randint(1, 6) for _ in range(n)]

###############################################################
# Question I.4 : test de Q_I_3 pour 5 tirages de taille 10
###############################################################
for _ in range(5):
    print(Q_I_3(10))

###############################################################
# Question I.5 : nombre de "Pile" dans n lancers
###############################################################
def Q_I_5(n):
    tirages = [rd.choice(["Pile", "Face"]) for _ in range(n)]
    return tirages.count("Pile")

###############################################################
# Question I.6 : test pour n = 10^k, k = 2..5
###############################################################
for k in range(2, 6):
    n = 10**k
    print(f"n={n}, nombre de Pile :", Q_I_5(n))

###############################################################
# Exercice II.1 : probabilité de 2 vertes (5V, 3B, 2 tirages sans remise)
###############################################################
# 1/ Formule théorique
p_theo = (5/8) * (4/7)
print("Probabilité théorique :", p_theo)

# 2/ Simulation
simu = 10000
cpt = 0
for _ in range(simu):
    urne = ["V"]*5 + ["B"]*3
    tirage = rd.sample(urne, 2)
    if tirage.count("V") == 2:
        cpt += 1
print("Probabilité simulée :", cpt/simu)

###############################################################
# Exercice II.2 : probas des 6 faces après 100 lancers
###############################################################
def proba_faces(N):
    tirages = [rd.randint(1, 6) for _ in range(N)]
    return [tirages.count(k)/N for k in range(1, 7)]

probas = proba_faces(100)
print("Probabilités :", probas)

# Graphique
plt.bar(range(1,7), probas)
plt.xlabel("Face")
plt.ylabel("Proportion")
plt.title("Distribution des faces sur 100 lancers")
plt.show()

# Probabilité d'un résultat pair
p_pair = probas[1] + probas[3] + probas[5]
print("Probabilité d'obtenir un nombre pair :", p_pair)

###############################################################
# Exercice III.1 : probabilité d'apparition du 1 en fonction des itérations
###############################################################
for N in [10, 50, 100, 500, 1000, 5000, 10000]:
    p1 = [rd.randint(1, 6) for _ in range(N)].count(1)/N
    print(f"N={N}, P(1)≈{p1}")

###############################################################
# Exercice III.2 : loi binomiale
###############################################################
x = np.arange(0, 101)

# 1/ n=30, p=0.3
n, p = 30, 0.3
plt.bar(range(n+1), binom.pmf(range(n+1), n, p))
plt.title("Loi binomiale n=30, p=0.3")
plt.show()

# 2/ n=30, p variant
for p in np.linspace(0.2, 0.8, 4):
    plt.plot(range(n+1), binom.pmf(range(n+1), n, p), label=f"p={p:.1f}")
plt.legend()
plt.title("Variation de p (n=30)")
plt.show()

# 3/ n=100, p variant
n = 100
for p in np.linspace(0.1, 0.9, 5):
    plt.plot(range(n+1), binom.pmf(range(n+1), n, p), label=f"p={p:.1f}")
plt.legend()
plt.title("Variation de p (n=100)")
plt.show()

###############################################################
# Exercice III.3 : Variable aléatoire X image = {0..9}
###############################################################
X_vals = np.arange(10)
P = np.ones(10)/10  # uniforme
E = np.sum(X_vals * P)
V = np.sum((X_vals - E)**2 * P)
print("Espérance :", E)
print("Variance :", V)

###############################################################
# Exercice III.4 : retrouver E et V d'une binomiale
###############################################################
n, p = 10, 0.3
print("E binomiale =", n*p)
print("V binomiale =", n*p*(1-p))

# %%
###############################################################

# Exercice III.5 : 10 implantations, p=0.7 -> Binomiale(10,0.7)
###############################################################
print("Distribution = Binomiale(n=10,p=0.7)")

###############################################################
# Exercice III.6 : temps d'attente de la première Face (p=0.3)
###############################################################
# 1/ Simulation

def attente_face():
    c = 1
    while rd.random() > 0.3:
        c += 1
    return c

print("Exemples simulations :", [attente_face() for _ in range(20)])

# 2/ Loi usuelle : loi géométrique(p=0.3)
print("Distribution = Géométrique(p=0.3)")
