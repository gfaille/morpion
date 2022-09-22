def verification():
    # verification des lignes
    for liste_case in range(3):
        if liste_case[0][0] == liste_case[0][1] == liste_case[0][2] != "_" \
        or liste_case[1][0] == liste_case[1][1] == liste_case[1][2] != "_" \
        or liste_case[2][0] == liste_case[2][1] == liste_case[2][2] != "_" :
            return print("Gagné")
    # verification des colonnes

        if liste_case[0][0] == liste_case[1][0] == liste_case[2][0] != "_" \
        or liste_case[1][0] == liste_case[1][1] == liste_case[1][2] != "_" \
        or liste_case[2][0] == liste_case[2][1] == liste_case[2][2] != "_":
            return print("Gagné")
    # verification des diagonales
        if liste_case[0][0] == liste_case [1][1] == liste_case[2][2] != "_" \
        or liste_case[2][2] == liste_case [1][1] == liste_case [0][0] != "_":
            return print("Gagné")

liste_case = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

def afficher_grille (grille) :
    """ fonction pour créer la grille du morpion sur une ligne de 3X3. """
    for i in grille :
        print (i)

def jouer_coups () :
    """fonction pour demander au joueur de jouer un coups entre 1 à 9."""

    afficher_grille(liste_case)
    print("tour du joueur. "  + "tapez de 1 à 9")
    coups_jouer = int(input())
    if coups_jouer >= 7:
        #if coups_jouer == "_" :

        liste_case[0][coups_jouer-7] = "X"
        afficher_grille(liste_case)
    elif coups_jouer >= 4:
        liste_case[1][coups_jouer-4] = "C"
        afficher_grille(liste_case)
    elif coups_jouer >= 1:
        liste_case[2][coups_jouer-1] = "V"
        afficher_grille(liste_case)
    else:
        print("erreur 2")

jouer_coups()