import numpy as np
import deque
class Board:
    def __init__(self, chaine):
        self.plateau = chaine
    
    def __eq__(self, chaine):
        return self.plateau == chaine.plateau
    
def solution(board_init):
    file = deque()
    file.append(board_init)

    while file:
        board = file.pop()
        for voisins in voisins(board):