#Mastermind

Réalisation d'un jeu du Mastermind en Python 3.7 pour le compte du CESI de Lille.
Le jeu doit comporter deux joueurs.

Le premier joueur choisit 4 pions de couleurs de son choix parmis un panel définit à l'avance, dans un ordre précis et sans être vu.
Ce choix correspond à la solution de la partie. Il devra donc se faire à l'abri des regards.

Une fois la solution définie, le second joueur à la possibilité de proposer 4 pions de couleurs.
Une fois la proposition entrée, le programme peut retourner jusqu'à 4 pions:
    - Rouge : Un pion est bien placé
    - Blanc : Une couleur est bonne
    - Vide  : Mauvaise réponse

Le programme continu tant que la solution n'a pas été trouvé, ou que le nombre d'essai n'exède pas.
Une fois la partie fini, les joueurs inverse les rôles.

Le jeux doit comporter deux niveau de difficultés:
    - Normal    : 4 cases à trouver, 8 couleurs possible.
    - Difficile : 6 cases à trouver, 10 couleurs possible.

Le jeu doit comporter 2 modes :
    - Normal : La solution est cachée.
    - Debug  : La solution est affichée.

Le jeu ne comportera pas d'interface graphique, par conséquent un affichage console agréable sera priorisé. 