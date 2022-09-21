liste_case = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

def afficher_grille () :
    """ fonction pour créer la grille du morpion sur une ligne de 3X3. """
    for i in range (3) :
        print (liste_case[i])

def jouer () :
    """ fonction pour jouer, remplace les case vide par un X si c'est joueur 1 ou O si c'est joueur 2. """

    joueur = "X"
    tour = 0

    while True :

        afficher_grille()
        print("tour du joueur " + joueur + ". Entrez un nombre entre 1 à 9 .")

        placer = int(input()) - 1 # Le tableau commence à 0 donc j'enleve 1

        if [placer] == "_" :
            liste_case[placer] = joueur
            tour += 1
        else :
            print("Case occuper ! jouer autre par.")
            continue
        
        if [0] == [1] == [2] != "_" \
        or [3] == [4] == [5] != "_" \
        or [6] == [7] == [8] != "_" \
        or [0] == [3] == [6] != "_" \
        or [1] == [4] == [7] != "_" \
        or [2] == [5] == [8] != "_" \
        or [0] == [4] == [8] != "_" \
        or [2] == [4] == [6] != "_" :
            afficher_grille(joueur)
            break 
    
jouer()
