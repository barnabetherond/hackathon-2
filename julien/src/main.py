import flet as ft

class Board:
    def __init__(self, chaine):
        self.plateau = chaine
    
    def __eq__(self, chaine):
        return self.plateau == chaine.plateau

header = ft.Text(value="Bienvenue sur CCsolution2025byBaJu2Os (taquin resolver) !", color="white", weight=ft.FontWeight.BOLD)
squares = [ft.Image(src=f"{i}.jpg",width=10,height=10,border_radius=10, fit=ft.ImageFit.COVER) for i in range(1,9)]
squares.append(ft.Container(content=ft.Text(value="-", color="white",weight=ft.FontWeight.BOLD,size=24),width=10,height=10,border_radius=10,bgcolor='#32353d',alignment=ft.Alignment(0, 0)))
bottom = [ft.Image(src="shuf.png",width=50,height=50),ft.Image(src="sol.png",width=50,height=50)]

def reset(board):
    for i, square in zip(board, squares):
        square.value = i

def main(page):
    page.window_width = 600
    page.window_height = 400
    page.add(
        ft.Column([header]),
        ft.GridView(squares, expand=False ,max_extent=100,spacing=10,run_spacing=10),
        ft.Row(bottom,alignment=ft.MainAxisAlignment.CENTER, spacing=50)
            )

ft.app(main)

#ft.Text(value=str(i), color="white",weight=ft.FontWeight.BOLD,size=24),width=10,height=10,border_radius=10,bgcolor=ft.colors.BLUE,alignment=ft.Alignment(0, 0)