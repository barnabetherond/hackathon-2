import numpy as np
import copy
import heapq
from collections import deque

class Board:
    def __init__(self, chaine):
        self.plateau = chaine
        id = ''
        for i in range(3):
            for j in range(3):
                id += str(self.plateau[i][j])
        self.id = id

    
    def __eq__(self, chaine):
        return self.plateau == chaine.plateau
    
    def __hash__(self):
        return hash((self.id))
    
    def __repr__(self):
        return str(self.plateau)



    
    
        

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

def voisins(matrice):
    position_zero = trouver_position_zero(matrice)
    deplacements = mouvements_possibles(position_zero)

    matrices_resultantes = []
    for nouvelle_position in deplacements:
        nouvelle_matrice = echanger_positions(matrice, position_zero, nouvelle_position)
        matrices_resultantes.append(nouvelle_matrice)

    return matrices_resultantes


def crea(board_init, goal):
    file = deque()
    file.append(board_init)
    dico = {}
    visited = set()
    while file:
        board = file.popleft()
        if board not in dico.keys():
            dico[board] = []
        visited.add(board)
        V = voisins(board.plateau)
        for voisin in V:
            if voisins not in visited:
                file.append(Board(voisin))
                dico[board].append(Board(voisin))
                
        if board == goal:
           return dico
        

import heapq
from collections import deque

def dijkstra(graph, start, target):
    queue = deque([(start, 0, [])])  # (node, distance, path)
    visited = set()
    
    while queue:
        current_node, current_distance, path = queue.popleft()
        
        if current_node in visited:
            continue
        
        path = path + [current_node]
        visited.add(current_node)
        
        if current_node == target:
            return  path
        
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                queue.append((neighbor, current_distance + 1, path))
    
    return float("inf"), []
    
    

goal = Board([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]])

start = Board([[1, 2, 3],
              [4, 5, 0],
              [7, 8, 6]])

graph = crea(start, goal)
M = dijkstra(graph, start, goal)
for i in M:
    print(i)
    
