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
    while True :

        #1afficher_grille(liste_case)
        print("tour du joueur. "  + joueur + " tapez de 1 à 9")
        coups_jouer = int(input())
        if coups_jouer >= 7 :
            if liste_case[0][coups_jouer-7] == "_" :
                liste_case[0][coups_jouer-7] = joueur
                return afficher_grille(liste_case)
            else :
                print("case déjâ utiliser !")
        elif coups_jouer >= 4:
            if liste_case[1][coups_jouer-4] == "_" :
                liste_case[1][coups_jouer-4] = joueur
                return afficher_grille(liste_case)
            else :
                print("case déjâ utiliser !")
        elif coups_jouer >= 1:
            if liste_case[2][coups_jouer-1] == "_" :
                liste_case[2][coups_jouer-1] = joueur
                return afficher_grille(liste_case)
            else :
                print("case déjâ utiliser !")
        else:
            print("erreur 2")

joueur = "X"
tour = 0

while True :
    tour += 1

 # verification des lignes
    if liste_case[0][0] == liste_case[0][1] == liste_case[0][2] != "_" \
    or liste_case[1][0] == liste_case[1][1] == liste_case[1][2] != "_" \
    or liste_case[2][0] == liste_case[2][1] == liste_case[2][2] != "_" :
        if joueur == "O" :
            joueur = "joueur 1"
        else :
            joueur = "joueur 2"
        print(joueur + " Gagné")
        break

# verification des colonnes
    if liste_case[0][0] == liste_case[1][0] == liste_case[2][0] != "_" \
    or liste_case[1][0] == liste_case[1][1] == liste_case[1][2] != "_" \
    or liste_case[2][0] == liste_case[2][1] == liste_case[2][2] != "_":
        if joueur == "O" :
            joueur = "joueur 1"
        else :
            joueur = "joueur 2"
        print(joueur + " Gagné")
        break

# verification des diagonales
    if liste_case[0][0] == liste_case [1][1] == liste_case[2][2] != "_" \
    or liste_case[2][0] == liste_case [1][1] == liste_case [0][2] != "_":
        if joueur == "O" :
            joueur = "joueur 1"
        else :
            joueur = "joueur 2"
        print(joueur + " Gagné")
        break

    jouer_coups()
    if tour == 9 :
        print ("égality")
        break
    
    if joueur == "X" :
        joueur = "O"
    else :
        joueur = "X"