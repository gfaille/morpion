liste_case = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

def afficher_grille () :
    """ fonction pour créer la grille du morpion sur une ligne de 3X3. """
    for i in range (3) :
        print (liste_case[i])

def jouer_coups () :
    """fonction pour jouer un coups soit "X" soit "O" dans la grille"""

    print("tour du joueur. " + joueur + " tapez de 1 à 9")
    placer = int(input()) - 1

    if liste_case[placer] == "_" :
        placer = joueur 
    else :
        print("case occuper veuillez recommencez ailleur")
        continue 
    
jouer_coups()