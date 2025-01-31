# import random

# def generer_matrice_3x3():
#     chiffres = list(range(0, 9))  # Liste des chiffres de 0 à 8
#     random.shuffle(chiffres)      # Mélanger les chiffres aléatoirement

#     # Générer une matrice 3x3
#     matrice = [chiffres[i:i + 3] for i in range(0, 9, 3)]
#     return matrice

# def afficher_matrice(matrice):
#     for ligne in matrice:
#         print(ligne)

# # Exemple d'utilisation
# matrice = generer_matrice_3x3()
# print("Matrice 3x3 aléatoire avec 0 à 8 :")
# afficher_matrice(matrice)


import copy

def trouver_position_zero(matrice):
    for i, ligne in enumerate(matrice):
        if 0 in ligne:
            return (i, ligne.index(0))
    return None

def mouvements_possibles(position):
    i, j = position
    deplacements = []

    # Vérification des mouvements possibles (haut, bas, gauche, droite)
    if i > 0:  # Haut
        deplacements.append((i - 1, j))
    if i < 2:  # Bas
        deplacements.append((i + 1, j))
    if j > 0:  # Gauche
        deplacements.append((i, j - 1))
    if j < 2:  # Droite
        deplacements.append((i, j + 1))

    return deplacements

def echanger_positions(matrice, pos1, pos2):
    nouvelle_matrice = copy.deepcopy(matrice)
    i1, j1 = pos1
    i2, j2 = pos2
    nouvelle_matrice[i1][j1], nouvelle_matrice[i2][j2] = nouvelle_matrice[i2][j2], nouvelle_matrice[i1][j1]
    return nouvelle_matrice

def generer_matrices_possibles(matrice):
    position_zero = trouver_position_zero(matrice)
    deplacements = mouvements_possibles(position_zero)

    matrices_resultantes = []
    for nouvelle_position in deplacements:
        nouvelle_matrice = echanger_positions(matrice, position_zero, nouvelle_position)
        matrices_resultantes.append(nouvelle_matrice)

    return matrices_resultantes

matrices_possibles = generer_matrices_possibles(matrice)

print("Matrices résultantes après échanges possibles :")
for idx, matrice_resultante in enumerate(matrices_possibles):
    print(f"Mouvement {idx + 1} :")
    afficher_matrice(matrice_resultante)


