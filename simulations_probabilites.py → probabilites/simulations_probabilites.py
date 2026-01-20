
from sympy import Matrix, init_printing
from IPython.display import display



M = Matrix([[1, 2], [3, 4]])


print("Pour l'affichage de notre matrice M :")
print("avec l'affichage direct avec print :")
print(M)
print("avec display(M) :")
display(M) # ceci permet de créer un joli affichage en LaTeX dans Jupyter Notebook
init_printing(use_latex=True) # ceci permet d'activer le rendu LaTeX
# on peut définir une matrice en décrivant ses lignes
M = Matrix([[1, -2], [0, 4]])
M


# commandes à exécuter
# on peut préciser la matrice à partir de son format (nb lignes et nb colonnes) 
A = Matrix(3,2,[1,2,3,4,5,6])
display(A)
B = Matrix(2,3,[1,2,3,4,5,6])
display(B)
C = Matrix(6,1,[1,2,3,4,5,6])
display(C)
D = Matrix(1,6,[1,2,3,4,5,6])
display(D)


# commandes à exécuter
# une autre façon de définir la matrice B
M = Matrix([[1, 2, 3],
[4, 5, 6]])
display(M)


# commandes à exécuter
print("On observe les instructions sur cette matrice A :")
display(A)
print("Que renvoie l'instruction A.shape ?", A.shape) # (3, 2)
print("Que renvoie l'instruction A.shape[0] ?", A.shape[0]) #  3
print("Que renvoie l'instruction A.shape[1] ?", A.shape[1]) #  2

# commandes à exécuter
A = Matrix.zeros(3)
B = Matrix.zeros(2,4)
print("Que renvoie l'instruction Matrix.zeros(3) ?") # la matrice nul de dim 3x3
display(A)
print("Que renvoie l'instruction Matrix.zeros(2,4) ?") # la matrice nul de dim 4x2
display(B)


# commandes à exécuter
A = Matrix.eye(3)
B = Matrix.eye(2,4)
print("Que renvoie l'instruction Matrix.eye(3) ?") # la matrice identiter de dim 3x3
display(A)
print("Que renvoie l'instruction Matrix.eye(2,4) ?") # la matrice identiter de dim 4x2
display(B)


# commandes à exécuter
A = Matrix([[1,2,3],[0,-1,4],[0,0,5]])
B = Matrix([[1,2,3,4],[0,0,0,0],[0,0,5,6]])
print("Que renvoie l'instruction A.rank() ?", A.rank()) # 3
print("Que renvoie l'instruction B.rank() ?", B.rank()) # 2


# commandes à exécuter
A = Matrix([[1,2,3],[0,-1,4],[0,0,5]])
B = Matrix([[1,2],[3,4]])
print("Que renvoie l'instruction A.det() ?", A.det()) # -5
print("Que renvoie l'instruction B.det() ?", B.det()) # -2


# commandes à exécuter
A = Matrix([[1,2,3],[0,-1,4],[0,0,5]])
B = Matrix([[1,2],[3,4]])
print("Que renvoie l'instruction A.inv() ?")
display(A.inv()) # la matrice inverse de A
print("Que renvoie l'instruction B.inv() ?")
display(B.inv()) # la matrice inverse de B

# etude spectrale
M = Matrix([[4,0, 1],[0,2,0],[2,0, 3]])
print("\nValeurs propres :")
vals = M.eigenvals() #{5: 1, 2: 2}
print(vals)
print("\nVecteurs propres :")
vects = M.eigenvects() # [(2, 2, [Matrix([[0],[1],[0]]), Matrix([[-1/2],[   0],[   1]])]), (5, 1, [Matrix([[1],[0],[1]])])]
print(vects)


# question 1
#voici un exemple de matrice pour tester votre script
M = Matrix([[4,1, 1],[0,4,1],[0,0, 2]])
display(M)

# question 2
def generateurs_sous_espaces_propres(M):
    vects = M.eigenvects()
    for val, mult, basis in vects:
        print(f"Valeur propre : {val}")
        print(f"Générateurs du sous-espace propre : {basis}")
# question 3
def est_valeur_propre_rang(M, lam):
    return M - lam*Matrix.eye(M.shape[0]).rank() != M.rank()

def est_valeur_propre_det(M, lam):
    return (M - lam*Matrix.eye(M.shape[0])).det() == 0
#question 4
def racines_evidentes(M):
    poly = M.charpoly()
    x = poly.free_symbol       # récupère le bon symbole !
    expr = poly.as_expr()

    racines = []
    for k in range(-5, 6):
        if expr.subs(x, k) == 0:
            racines.append(k)
    return racines

# question 5
def spectre_reel(M):
    vals = M.eigenvals()
    for val, mult in vals.items():
        if val.is_real:
            print(f"Valeur propre réelle : {val}, multiplicité : {mult}")

# question 6
def dimension_sous_espace_propre(M, lam):
    vects = M.eigenvects()
    for val, mult, basis in vects:
        if val == lam:
            return len(basis)
    return 0
# question 7 
def multiplicite_egales(M, lam):
    vals = M.eigenvals()
    mult_alg = vals.get(lam, 0)
    mult_geo = dimension_sous_espace_propre(M, lam)
    return mult_alg == mult_geo
# question 8
def est_diagonalisable(M):
    vals = M.eigenvals()
    for lam in vals:
        if not multiplicite_egales(M, lam):
            return False
    return True

#◘ question 9 
def puissance_matrice(M, n):
    R = Matrix.eye(M.shape[0])
    for _ in range(n):
        R = R * M
    return R

def puissance_matrice_diag(M, n):
    if not est_diagonalisable(M):
        raise ValueError("La matrice n'est pas diagonalisable")

    P, D = M.diagonalize()
    Dn = D**n
    return P * Dn * P.inv()
