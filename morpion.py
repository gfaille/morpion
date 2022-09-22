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
    """fonction pour demander au joueur de jouer un coups entre 1 à 9 et vérifier si le coups est valide."""

    afficher_grille(liste_case)
    print("tour du joueur. "  + "tapez de 1 à 9")
    coups_jouer = int(input())
    if coups_jouer >= 7:
        if liste_case[0][coups_jouer-7] == "_" :
            liste_case[0][coups_jouer-7] = "X"
            afficher_grille(liste_case)
    elif coups_jouer >= 4:
        if liste_case[1][coups_jouer-4] == "_" :
            liste_case[1][coups_jouer-4] = "C"
            afficher_grille(liste_case)
    elif coups_jouer >= 1:
        if liste_case[1][coups_jouer-4] == "_" :
            liste_case[2][coups_jouer-1] = "V"
            afficher_grille(liste_case)
    else:
        print("erreur 2")


jouer_coups()