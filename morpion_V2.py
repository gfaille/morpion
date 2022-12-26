import pygame

# initialise le module pygame
pygame.init()

# affiche la fenêtre 
fenetre = pygame.display.set_mode((500, 500))

liste_case = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

def afficher_grille () :
    pygame.draw.line(fenetre, (145, 145, 145), (166, 0), (166, 500))
    pygame.draw.line(fenetre, (145, 145, 145), (332, 0), (332, 500))
    pygame.draw.line(fenetre, (145, 145, 145), (0, 166), (500, 166))
    pygame.draw.line(fenetre, (145, 145, 145), (0, 332), (500, 332))

def dessiner_croix (rect) :
    pygame.draw.line(fenetre, (195, 195, 195), (rect.x + rect.w*0.2, rect.y + rect.h*0.2), (rect.x + rect.w*0.8, rect.y + rect.h*0.8), 2)
    pygame.draw.line(fenetre, (195, 195, 195), (rect.x + rect.w*0.8, rect.y + rect.h*0.2), (rect.x + rect.w*0.2, rect.y + rect.h*0.8), 2)

def dessiner_cercle (rect) :
    pygame.draw.circle(fenetre, (195, 195, 195), (rect.center), radius=10)


rect_1 = pygame.draw.rect(fenetre, (0, 0, 0), (0, 0, 166, 166))
rect_2 = pygame.draw.rect(fenetre, (0, 0, 0), (166, 0, 166, 166))
rect_3 = pygame.draw.rect(fenetre, (0, 0, 0), (332, 0, 166, 166))

rect_4 = pygame.draw.rect(fenetre, (0, 0, 0), (0, 166, 166, 166))
rect_5 = pygame.draw.rect(fenetre, (0, 0, 0), (166, 166, 166, 166))
rect_6 = pygame.draw.rect(fenetre, (0, 0, 0), (332, 166, 166, 166))

rect_7 = pygame.draw.rect(fenetre, (0, 0, 0), (0, 332, 166, 166))
rect_8 = pygame.draw.rect(fenetre, (0, 0, 0), (166, 332, 166, 166))
rect_9 = pygame.draw.rect(fenetre, (0, 0, 0), (332, 332, 166, 166))


joueur = 1
continuer = True

# boucle principale
while continuer :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            continuer = False

        elif event.type == pygame.MOUSEBUTTONDOWN :

            if rect_1.collidepoint(event.pos) :
                if liste_case[0][0] == 0 :
                    coups = True
                    if joueur == 1 :
                        dessiner_croix(rect_1)
                        liste_case[0][0] = joueur
                    else :
                        dessiner_cercle(rect_1)
                        liste_case[0][0] = joueur
                else : 
                    coups = False

            elif rect_2.collidepoint(event.pos) :
                if liste_case[0][1] == 0 :
                    coups = True
                    if joueur == 1 :
                        dessiner_croix(rect_2)
                        liste_case[0][1] = joueur
                    else :
                        dessiner_cercle(rect_2)
                        liste_case[0][1] = joueur
                else : 
                    coups = False

            elif rect_3.collidepoint(event.pos) :
                if liste_case[0][2] == 0 :
                    coups = True
                    if joueur == 1 :
                        dessiner_croix(rect_3)
                        liste_case[0][2] = joueur
                    else :
                        dessiner_cercle(rect_3)
                        liste_case[0][2] = joueur
                else : 
                    coups = False

            elif rect_4.collidepoint(event.pos) :
                if liste_case[1][0] == 0 :
                    coups = True
                    if joueur == 1 :
                        dessiner_croix(rect_4)
                        liste_case[1][0] = joueur
                    else :
                        dessiner_cercle(rect_4)
                        liste_case[1][0] = joueur
                else : 
                    coups = False

            elif rect_5.collidepoint(event.pos) :
                if liste_case[1][1] == 0 :
                    coups = True
                    if joueur == 1 :
                        dessiner_croix(rect_5)
                        liste_case[1][1] = joueur
                    else :
                        dessiner_cercle(rect_5)
                        liste_case[1][1] = joueur
                else : 
                    coups = False

            elif rect_6.collidepoint(event.pos) :
                if liste_case[1][2] == 0 :
                    coups = True
                    if joueur == 1 :
                        dessiner_croix(rect_6)
                        liste_case[1][2] = joueur
                    else :
                        dessiner_cercle(rect_6)
                        liste_case[1][2] = joueur
                else : 
                    coups = False

            elif rect_7.collidepoint(event.pos) :
                if liste_case[2][0] == 0 :
                    coups = True
                    if joueur == 1 :
                        dessiner_croix(rect_7)
                        liste_case[2][0] = joueur
                    else :
                        dessiner_cercle(rect_7)
                        liste_case[2][0] = joueur
                else : 
                    coups = False

            elif rect_8.collidepoint(event.pos) :
                if liste_case[2][1] == 0 :
                    coups = True
                    if joueur == 1 :
                        dessiner_croix(rect_8)
                        liste_case[2][1] = joueur
                    else :
                        dessiner_cercle(rect_8)
                        liste_case[2][1] = joueur
                else : 
                    coups = False

            elif rect_9.collidepoint(event.pos) :
                if liste_case[2][2] == 0 :
                    coups = True
                    if joueur == 1 :
                        dessiner_croix(rect_9)
                        liste_case[2][2] = joueur
                    else :
                        dessiner_cercle(rect_9)
                        liste_case[2][2] = joueur
                else : 
                    coups = False

            # changement de joueur   
            if coups != False :        
                if joueur == 1 :
                    joueur = 2
                else :
                    joueur = 1  

    afficher_grille()
    pygame.display.flip()

print(liste_case)
pygame.quit()