# hackathon-2

Bonjour à tous,
On a codé une sorte de Djikstra. L'idée est de d'abord dire que si on parcours en largeur le graphe depuis le plateau initial, la première fois qu'on 
atterit sur l'image finale sera le chemin le plus court. On parcourt donc dans un premier temps le graphe en largeur pour créer un dictionnaire jusqu'à 
trouver l'image finale. Ce dictionnaire représente le graphe dans lequel on applique djikstra ensuite. 
Ensuite, on a toute la partie codée à l'aide de flet. On a codé 2 fonctionalités. Un bouton de mélange et un bouton de résolution.
Pour le bouton de mélange on a 2 choix. En premier, une image vraiment aléatoire. Le problème est que notre Djikstra ne marche pas très bien (du moins
on pense), et trouver une solution prend trop de temps. Ainsi, pour voir si la partie flet marchait, on a programmé une partie qui génére une image "un
peu aléatoire". On part de la solution (goal) et on fait 30 mouvements aléatoires et on le refait 30 fois, et on choisit aléatoirement la dedans. Puis 
on part de cette solution pour résoudre. De cette manière, on voit que flet affiche bien. Pour utiliser la version "un peu aléatoire", il faut utiliser
la fonction broad_5(), la mettre en argument de actu_squares et mettre image en argument de anim_solution. 
Si vous souhaitez changer le "un peu aléatoire", vous pouvez changer la fonction alea_mov10 pour avoir plus de 30 mouvements tirés aléatoirement.

le fichier de code est `src/main.py` et pour le lancer il faut faire la commande `flet run` dans le dossier principal du repo