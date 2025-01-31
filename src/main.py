import flet as ft
import random
import numpy as np
import copy
import heapq
from collections import deque
import time

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


header = ft.Text(value="Bienvenue sur CCsolution2025byBaJu2Os (taquin resolver)", color="white", weight=ft.FontWeight.BOLD)
squares = [ft.Image(src=f"{i}.jpg",width=10,height=10,border_radius=10, fit=ft.ImageFit.COVER) for i in range(1,10)]
#shuffle = ft.Image(src="shuf.png",width=50,height=50)
shuffle = ft.CupertinoFilledButton(content=ft.Text("Mélange"),opacity_on_click=0.3)
solution = ft.CupertinoFilledButton(content=ft.Text("Solution"),opacity_on_click=0.3)
#solution = ft.Image(src="sol.png",width=50,height=50)
bottom = [shuffle,solution]

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
        
def alea_10mov(goal):
    L = []
    for i in range(30):
        board = goal
        for j in range(40):
            V = voisins(board.plateau)
            board = Board(random.choice(V))
        L.append(board)
    return L

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

def main(page):  

    def rand_board():
        chiffres = list(range(0, 9))
        random.shuffle(chiffres)
        matrice = [chiffres[i:i + 3] for i in range(0, 9, 3)]
        global init
        init=Board(matrice)
        return init
    
    def board_5():
        L = alea_10mov(goal)
        i = random.randint(0, len(L)-1)
        global image
        image = L[i]
        return image

    def actu_squares(board):
        global squares
        list=board.plateau[0]+board.plateau[1]+board.plateau[2]
        for i in range(9):
            squares[i].src=f"{list[i]}.jpg"
        page.update()

    def anim_solution(init):
        indic_calc.visible=True
        page.update()
        graph = crea(init, goal)
        sol = dijkstra(graph, init, goal)
        indic_calc.visible=False
        page.update()
        for board in sol:
            #print(board)
            actu_squares(board)
            page.update()
            time.sleep(0.5)

    page.window.width = 300
    page.window.height = 500
    indic_calc=ft.Text(value="               Calcul de la solution...", color="white", visible=False)
    goal = Board([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]])
    actu_squares(board_5())
    page.add(
        ft.Column([header]),
        ft.GridView(squares, expand=False ,max_extent=100,spacing=10,run_spacing=10),
        ft.Row(bottom,alignment=ft.MainAxisAlignment.CENTER, spacing=20),
        indic_calc
            )
    
    shuffle.on_click=lambda e: actu_squares(board_5())
    solution.on_click=lambda e: anim_solution(image)


ft.app(main)