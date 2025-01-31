import numpy as np
import copy
import heapq
class Board:
    def __init__(self, chaine):
        self.plateau = chaine
        
    
    def __eq__(self, chaine):
        return self.plateau == chaine.plateau
    
    def __hash__(self):
        return hash(tuple[self.plateau])
    
    def __repr__(self):
        print(self.plateau)


class deque:
    def __init__(self, list):
        self.list = list

    def popy(self):
        return self.list.popleft()
    
    
        

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
    file = deque([])
    file.list.append(board_init)
    dico = {}
    visited = set()
    while file:
        board = file.popy()
        visited.add(board)
        V = voisins(board.plateau)
        for plateau in V:
            if plateau in visited:
                V.pop(plateau)
        dico[board] = V
        for voisin in V:
            file.list.append(voisin)
        if board == goal:
            return dico
        

def dijkstra(graph, start, target):
    # Initialisation
    priority_queue = [(0, start, [])]  # (distance, node, path)
    visited = set()
    
    while priority_queue:
        (current_distance, current_node, path) = heapq.heappop(priority_queue)
        
        if current_node in visited:
            continue
        
        path = path + [current_node]
        visited.add(current_node)
        
        # Arrêt si on atteint la cible
        if current_node == target:
            return current_distance, path
        
        # Exploration des voisins
        for neighbor, weight in graph.get(current_node, {}).items():
            if neighbor not in visited:
                heapq.heappush(priority_queue, (current_distance + weight, neighbor, path))
    
    return float("inf"), []
    

goal = Board([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]])

start = Board([[1, 2, 3],
              [4, 5, 0],
              [7, 8, 6]])

graph = crea(start, goal)
print(dijkstra(graph, start, goal))
    
