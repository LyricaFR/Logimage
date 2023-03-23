#QUACH Kevin & RAJON Lionel
#Tdc TP5 L1
#2019-2020 UPEM

from upemtk import*

#Dimension du jeu
taille_case = 70
largeur_plateau = 9  # en nombre de cases
hauteur_plateau = 9  # en nombre de cases



def case_vers_pixel(case):
    """
    Fonction recevant les coordonnées d'une case du plateau sous la
    forme d'un couple d'entiers (ligne, colonne) et renvoyant les
    coordonnées du pixel se trouvant au centre de cette case. Ce calcul
    prend en compte la taille de chaque case, donnée par la variable
    globale taille_case.
    """
    i, j = case
    return (i + .5) * taille_case, (j + .5) * taille_case


def pixel_vers_case(x, y, taille_case):
    '''
    Fonction recevant les coordonnées en pixel et la taille des cases du
    plateau et renvoie un couple d'entier correspondant aux coordonnée en
    case sur le plateau.
    param x : int
    param y : int
    param taille_case : int
    sortie : tuple

    >>>pixel_vers_case(180,456,100)
    (1, 4)
    >>>pixel_vers_case(625,321,100)
    (6, 3)
    '''
    return x//taille_case, y//taille_case



#----------------------selection-de-la-case------------------------------------------------------------


def case_select(board, history, abscisse, ordonnee):
    '''Fonction permettant de selectionner une case de la grille.
    Si on appuis sur la flèche retour en haut à gauche, on annule le coup le plus récent.
    param board: list
    param history: list
    param abscisse: int
    param ordonnee: int
    '''
    x,y = pixel_vers_case(abscisse - espace_cote, ordonnee - espace_haut,taille_case)  #Coordonnée en case
    if x < 0 or y < 0 or x >= len(board[0]) or y >= len(board):
        pass
    else:
        if board[y][x] == 0:
            board[y][x] = 1
        elif board[y][x] == 1:
            board[y][x] = 0
        history.append((x,y))
    if abscisse > 106 and abscisse < 194 and ordonnee > 32 and ordonnee < 118:
        if history == []:
            pass
        else:
            a,b = history[len(history) - 1]
            if board[b][a] == 0:
                board[b][a] = 1
            elif board[b][a] == 1:
                board[b][a] = 0
            history.pop(len(history) - 1)


def remplissage_plateau(board):
    '''Fonction permettant de colorier la grille en fonction des éléments de la liste board.
    param board: list'''
    for ligne in range(len(board)):
        for colonne in range(len(board[ligne])):
            if board[ligne][colonne] == 1:
                rectangle(colonne* taille_case + espace_cote + 2, ligne * taille_case + espace_haut + 2, (colonne+1)* taille_case + espace_cote - 1,(ligne+1) * taille_case + espace_haut - 1, epaisseur =0,couleur='blue',remplissage='red', tag='rect')
            if board[ligne][colonne] == 0:
                rectangle(colonne* taille_case + espace_cote + 2, ligne * taille_case + espace_haut + 2,(colonne+1)* taille_case + espace_cote - 1,(ligne+1) * taille_case + espace_haut - 1, epaisseur =0,couleur='blue',remplissage='white', tag='rect')
    mise_a_jour()


def check_board(board, goal):
    '''Fonction qui vérifie si la grille a été complétée.
    param board: list
          goal : list
    '''
    if board == goal:
        return True
    if board != goal:
        return False



#-------------------------Plateau--------------------------------------------------------------------------------------------------
#creation_du_plateau


def plateau(board):
    '''Fonction permettant l'affichage du plateau de jeu.
    param board: list
    '''
    for i in range(len(board)):
        for j in range(len(board[i])):
            rectangle((j*taille_case)+espace_cote , (i*taille_case)+espace_haut , ((j+1) *taille_case)+espace_cote , ((i+1) *taille_case)+espace_haut ,couleur='black', epaisseur = 3, tag='rectangle')
            rectangle(j* taille_case + espace_cote + 3, i * taille_case + espace_haut + 3,(j+1)* taille_case + espace_cote - 1,(i+1)* taille_case + espace_haut - 1, epaisseur =0,couleur='blue',remplissage='white', tag='rect')


def affiche_num_colonne(colonnes_canard,x=0,y=-1):
    '''Fonction qui affiche au dessus de chaque colonne
    leur indice, le nombre de case coloriée sur celle-ci.
    param colonnes_canard: list
    param x: int
    param y: int
    '''
    for colonne in colonnes_canard :
        i,j=case_vers_pixel((x,y))
        texte(i+espace_cote-20,j+espace_haut ,str(colonne),taille=12,police='Segoe Script',couleur='snow')
        x+=1
#-20 permet de bien avoir les coord sur la case


def affiche_num_ligne(lignes_canard,x=-1,y=0):
    '''Fonction qui affiche à coté de chaque ligne
    leur indice, le nombre de case coloriée sur celle-ci.
    param lignes_canard: list
    param x: int
    param y: int
    '''
    for ligne in lignes_canard :
        i,j=case_vers_pixel((x,y))
        texte(i+espace_cote-20,j+espace_haut ,str(ligne),taille=12,police='Segoe Script',couleur='snow')
        y+=1


canard = [[0, 1, 1, 1, 0, 0, 0, 0],
          [1, 1, 0, 1, 0, 0, 0, 0],
          [0, 1, 1, 1, 0, 0, 1, 1],
          [0, 0, 1, 1, 0, 0, 1, 1],
          [0, 0, 1, 1, 1, 1, 1, 1],
          [1, 0, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 1, 1, 0, 0, 0]]

colonnes_canard = [(1, 2), (3, 1), (1, 5), (7, 1), (5), (3), (4), (3)]
lignes_canard = [(3), (2, 1), (3, 2), (2, 2), (6), (1, 5), (6), (1), (2)]


chat=     [[0, 0, 0, 0, 1, 0, 0, 1],
           [0, 0, 0, 0, 1, 1, 1, 1],
           [0, 0, 0, 0, 1, 1, 1, 1],
           [0, 0, 0, 0, 1, 1, 1, 1],
           [1, 1, 0, 0, 0, 1, 1, 0],
           [1, 0, 0, 0, 1, 1, 1, 1],
           [1, 0, 0, 1, 1, 1, 1, 1],
           [1, 0, 0, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1]]

colonnes_chat = [(5), (1, 1), (1), (3), (4 ,4), (8), (8), (4 ,4)]
lignes_chat = [(1, 1), (4), (4), (4), (2 , 2), (1, 4), (1,5), (1,5), (8)]


note_musique=  [[0, 0, 0, 0, 1, 1, 1, 0],
                [0, 0, 0, 0, 1, 1, 1, 1],
                [0, 0, 0, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 1, 0, 1, 0],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 1, 1, 1, 1, 0, 0, 0],
                [1, 1, 1, 1, 1, 0, 0, 0],
                [1, 1, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 1, 0, 0, 0, 0]]

colonnes_note = [(2), (4), (4), (4), (8), (2), (2, 1), (2)]
lignes_note = [(3), (4), (1, 1), (1, 1), (1), (4), (5), (5), (3)]



#-------------------------Solveur---------------------------------------------------------------------------------------------------------------------------------


def icone_solveur(x,y,solveur):
    '''Fonction qui dessine un cercle rouge autour de
    l'icone du solveur lorsqu'il est OFF et un cercle
    vert lorsqu'il est ON.
    param x: int
    param y: int
    param solveur: bool
    '''
    if x > 260 and x < 380 and y > 15 and y < 135:
        if solveur == False:
            solveur = True
        elif solveur == True:
            solveur = False
    if solveur == False:
        cercle(320,75,60, couleur = 'red', epaisseur = 2)
    if solveur == True:
        cercle(320,75,60, couleur = 'green', epaisseur = 2)
    mise_a_jour()
    return solveur


def solver(board, colonne, ligne, grille, line, case):              #J'ai commenté la majorité des remplissage_plateau + mise_a_jour pour accélérer la vitesse du solveur.
    '''Fonction qui permet de résoudre une grille logimage
    en explorant chaque possibilité possible.
    param board: list
    param colonne: list
    param ligne: list
    param grille: liste
    param line: int
    param case: int
    '''
    lignes = ligne
    colonnes = colonne
    total_ligne = total_line(board,line)
    for col in range(len(colonnes)):
        if isinstance(colonnes[col], tuple) == True:
            col1,col2 = colonnes[col]
            colonnes[col] = col1 + col2
    for i in range(case,len(board[line])):
        total_ligne = total_line(board,line)
        case_ref = i
        remplissage_plateau(board)
        mise_a_jour()
        if isinstance(lignes[line],tuple) == False:    # Si l'indice est un nombre unique
            if case_ref + lignes[line] > len(board[line]):
                for case_line in range(len(board[line + 1])):
                    board[line][case_line] = 0
                # remplissage_plateau(board)
                # mise_a_jour()
                total_ligne = total_line(board,line)
                return False                           # Renvoie False si on atteint le bout de la ligne sans trouver de solution
            while total_ligne != lignes[line]:
                board[line][case_ref] = 1
                case_ref += 1
                # remplissage_plateau(board)
                # mise_a_jour()
                total_ligne = total_line(board,line)
            for j in range(len(board[line])):
                if total_column(board,j) > colonnes[j]:
                    for case_line in range(len(board[line])):
                        board[line][case_line] = 0
                    # remplissage_plateau(board)
                    # mise_a_jour()
                    total_ligne = total_line(board,line)
            if total_ligne == lignes[line]:
                if solver(board, colonne, ligne, grille, line + 1, case) == False:   # Si aucune solution ne marche pour la ligne suivante
                    for case_line in range(len(board[line])):
                        board[line][case_line] = 0
                    # remplissage_plateau(board)
                    # mise_a_jour()
                    total_ligne = total_line(board,line)
            if check_board(board, grille) == True:
                remplissage_plateau(board)
                mise_a_jour()
                exit()
        else:                                               # Si l'indice est un tuple
            tuple1, tuple2 = lignes[line]
            if case_ref + tuple1 + tuple2 > len(board[line]):
                for case_line in range(case_ref,len(board[line])):
                    board[line][case_line] = 0
                # remplissage_plateau(board)
                # mise_a_jour()
                total_ligne = total_line(board,line)
                return False                           # Renvoie False si on atteint le bout de la ligne sans trouver de solution
            while total_ligne != tuple1:
                board[line][case_ref] = 1
                case_ref += 1
                # remplissage_plateau(board)
                # mise_a_jour()
                total_ligne = total_line(board,line)
            for case_ref2 in range(case_ref + 1, len(board[line])):
                case_flag = case_ref2
                if case_flag + tuple2 > len(board[line]):
                    for case_line in range(len(board[line])):
                        board[line][case_line] = 0
                    # remplissage_plateau(board)
                    # mise_a_jour()
                    total_ligne = total_line(board,line)
                    break
                while total_ligne != tuple1 + tuple2:
                    board[line][case_flag] = 1
                    case_flag += 1
                    # remplissage_plateau(board)
                    # mise_a_jour()
                    total_ligne = total_line(board,line)
                for x in range(len(board[line])):
                    if total_column(board,x) > colonnes[x]:
                        for case_line in range(case_ref,len(board[line])):
                            board[line][case_line] = 0
                        # remplissage_plateau(board)
                        # mise_a_jour()
                        total_ligne = total_line(board,line)
                if total_ligne == tuple1 + tuple2:
                    if solver(board, colonne, ligne, grille, line + 1, case) == False:   # Si aucune solution ne marche pour la ligne suivante
                        for case_line in range(case_ref,len(board[line])):
                            board[line][case_line] = 0
                        # remplissage_plateau(board)
                        # mise_a_jour()
                        total_ligne = total_line(board,line)
                if check_board(board, grille) == True:
                    remplissage_plateau(board)
                    mise_a_jour()
                    exit()


def total_line(board,line):
    '''Fonction qui calcule le nombre de cases
    sélectionnés sur une ligne de la grille entrée en paramètre.
    param board: list
    param line: int
    '''
    total = 0
    for case in range(len(board[line])):
        total += board[line][case]
    return total


def total_column(board, case):
    '''Fonction qui calcule le nombre de cases
    sélectionnés sur une colonne de la grille entrée en paramètre.
    param board: list
    param case: int
    '''
    total = 0
    for line in range(len(board)):
        total += board[line][case]
    return total



#-------------------------Programme-------------------------------------------------------------------------------------------------------------------------------


espace_haut=200 #pour centrer le tableau
espace_cote=100
cree_fenetre(75*largeur_plateau+espace_cote, 75*hauteur_plateau+espace_haut)


game = True
menu = True
option = False
play_canard = False
play_chat= False
play_note= False
solveur = False
exit = False
retour = False
end = False
lineSolv = 0
case = 0
Rejouer_chat= False
Rejouer_canard=False
Rejouer_Note=False


while game == True:
    while menu == True:
        history = []
        efface_tout()
        image(337,430,'image.jpg', ancrage='center')   #Source: https://www.vectorstock.com/royalty-free-vector/luxury-black-background-dark-geometric-squares-vector-21580913
        texte(225,120,'Logimage', couleur='dodgerblue', police='Times', taille=60)
        rectangle(100,300,675,380,couleur='silver', epaisseur=5, remplissage = 'white')
        texte(330,317,'Jouer', couleur='lightgrey', police='Times', taille=38)
        texte(325,310,'Jouer', couleur='black', police='Times', taille=38)
        rectangle(100,450,675,530,couleur='silver', epaisseur=5, remplissage = 'white')
        texte(220,467,'Choix de la grille', couleur='lightgrey', police='Times', taille=38)
        texte(215,460,'Choix de la grille', couleur='black', police='Times', taille=38)
        rectangle(100,600,675,680,couleur='silver', epaisseur=5, remplissage = 'white')
        texte(320,617,'Quitter', couleur='lightgrey', police='Times', taille=38)
        texte(315,610,'Quitter', couleur='black', police='Times', taille=38)

        ev = attend_ev()
        tev = type_ev(ev)
        mise_a_jour()

        if tev == 'ClicGauche':

            if abscisse(ev) < 675 and abscisse(ev) > 100 and ordonnee(ev) < 380 and ordonnee(ev) > 300:  # Pour lancer le jeu
                menu = False
                play_canard = True
                efface_tout()
                mise_a_jour()

            if abscisse(ev) < 675 and abscisse(ev) > 100 and ordonnee(ev) < 530 and ordonnee(ev) > 450:  # Pour accéder au choix des grilles
                menu = False
                option = True
                efface_tout()
                mise_a_jour()

            if abscisse(ev) < 675 and abscisse(ev) > 100 and ordonnee(ev) < 680 and ordonnee(ev) > 600:  # Pour quitter le jeu
                menu = False
                game = False


    board = []                   # Liste de liste qui donne l'état du plateau, 0: la case est blanche, 1: la case est coloré
    for colonne in range(9):     # Ici la grille est fixé à la taille 9 x 8, il faudra probablement changer ça pour pouvoir utiliser d'autres grilles
        line = []
        for ligne in range(8):
            line.append(0)
        board.append(line)

    while option==True:
        efface_tout()
        image(337,430,'image.jpg', ancrage='center')  #Source: https://www.vectorstock.com/royalty-free-vector/luxury-black-background-dark-geometric-squares-vector-21580913
        rectangle(100,300,675,380,couleur='silver', epaisseur=5, remplissage = 'white')
        texte(310,317,'Canard', couleur='lightgrey', police='Times', taille=38)
        texte(305,310,'Canard', couleur='black', police='Times', taille=38)
        rectangle(100,450,675,530,couleur='silver', epaisseur=5, remplissage = 'white')
        texte(335,467,'Chat', couleur='lightgrey', police='Times', taille=38)
        texte(330,460,'Chat', couleur='black', police='Times', taille=38)
        rectangle(100,600,675,680,couleur='silver', epaisseur=5, remplissage = 'white')
        texte(220,617,'Note de musique', couleur='lightgrey', police='Times', taille=38)
        texte(215,610,'Note de musique', couleur='black', police='Times', taille=38)
        image(150,75,'back2.png', ancrage='center')  # Source: https://cdn.pixabay.com/photo/2013/07/13/11/42/back-158491_640.png
        ev = attend_ev()
        tev = type_ev(ev)
        mise_a_jour() #il me semble que se mise a jour ne sert a rien (°0°)
        if tev == 'ClicGauche':

            if abscisse(ev) < 675 and abscisse(ev) > 100 and ordonnee(ev) < 380 and ordonnee(ev) > 300:  # Pour rejouer
                efface_tout()
                play_canard=True
                option=False
                efface_tout()
                mise_a_jour()

            if abscisse(ev) < 675 and abscisse(ev) > 100 and ordonnee(ev) < 530 and ordonnee(ev) > 450:  # Pour choisir/changer de grille
                end=False
                option=False
                play_chat=True
                efface_tout()
                mise_a_jour()

            if abscisse(ev) < 675 and abscisse(ev) > 100 and ordonnee(ev) < 680 and ordonnee(ev) > 600:  # Pour quitter
                end=False
                option=False
                play_note=True
                efface_tout()
                mise_a_jour()

            if abscisse(ev) > 106 and abscisse(ev) < 194 and ordonnee(ev) > 32 and ordonnee(ev) < 118:   # Pour revenir au menu
                option = False
                menu = True
                mise_a_jour()

    while play_canard == True:  # Début de la partie
        efface_tout()
        image(337,430,'image.jpg', ancrage='center')  #Source: https://www.vectorstock.com/royalty-free-vector/luxury-black-background-dark-geometric-squares-vector-21580913
        image(150,75,'back.png', ancrage='center')  # Source: https://www.interupgrade.com/images/pfeil-backbutton.png
        image(550,75,'menu.png', ancrage='center')  # Source: https://www.0ptim1ze.com/wp-content/uploads/white-37292_960_720.png
        image(320,75,'solveur.png', ancrage='center')  # Source: https://lutinbazar.fr/wp-content/uploads/2015/04/%C3%A9lec1-300x300.png
        affiche_num_colonne(colonnes_canard,x=0,y=-1)
        affiche_num_ligne(lignes_canard,x=-1,y=0)
        plateau(board)
        remplissage_plateau(board)
        icone_solveur(abscisse(ev),ordonnee(ev),solveur)
        solveur = icone_solveur(abscisse(ev),ordonnee(ev),solveur)
        ev = attend_ev()
        tev = type_ev(ev)
        mise_a_jour()
        if solveur == False:
            while tev != 'ClicGauche':
                ev = attend_ev()
                tev = type_ev(ev)
                mise_a_jour()
            case_select(board,history,abscisse(ev),ordonnee(ev))
        if solveur == True:
            solver(board, colonnes_canard, lignes_canard, canard, lineSolv, case)
        if abscisse(ev) > 450 and abscisse(ev) < 650 and ordonnee(ev) > 25 and ordonnee(ev) < 125:
            play_canard = False
            menu = True


        if check_board(board,canard) == True:
            remplissage_plateau(board)# j'ai replacer le fonction remplissage ici parceque ça affichais pas la derniere case que tu selectionnais quand tu gagnais (°w°)
            play_canard = False
            end = True
            Rejouer_canard=True


    while play_chat == True:  # Début de la partie
        efface_tout()
        image(337,430,'image.jpg', ancrage='center')  #Source: https://www.vectorstock.com/royalty-free-vector/luxury-black-background-dark-geometric-squares-vector-21580913
        image(150,75,'back.png', ancrage='center')  # Source: https://www.interupgrade.com/images/pfeil-backbutton.png
        image(550,75,'menu.png', ancrage='center')  # Source: https://www.0ptim1ze.com/wp-content/uploads/white-37292_960_720.png
        image(320,75,'solveur.png', ancrage='center')  # Source: https://lutinbazar.fr/wp-content/uploads/2015/04/%C3%A9lec1-300x300.png
        affiche_num_colonne(colonnes_chat,x=0,y=-1)
        affiche_num_ligne(lignes_chat,x=-1,y=0)
        plateau(board)
        remplissage_plateau(board)
        icone_solveur(abscisse(ev),ordonnee(ev),solveur)
        solveur = icone_solveur(abscisse(ev),ordonnee(ev),solveur)
        ev = attend_ev()
        tev = type_ev(ev)
        mise_a_jour()
        if solveur == False:
            while tev != 'ClicGauche':
                ev = attend_ev()
                tev = type_ev(ev)
                mise_a_jour()
            case_select(board,history,abscisse(ev),ordonnee(ev))
        if solveur == True:
            solver(board, colonnes_chat, lignes_chat, chat, lineSolv, case)
        if abscisse(ev) > 450 and abscisse(ev) < 650 and ordonnee(ev) > 25 and ordonnee(ev) < 125:
            play_chat = False
            menu = True

        if check_board(board,chat) == True:
            remplissage_plateau(board)# j'ai replacer le fonction remplissage ici parceque ça affichais pas la derniere case que tu selectionnais quand tu gagnais (°w°)
            play_chat = False
            end = True
            Rejouer_chat= True


    while play_note == True:  # Début de la partie
        efface_tout()
        image(337,430,'image.jpg', ancrage='center')  #Source: https://www.vectorstock.com/royalty-free-vector/luxury-black-background-dark-geometric-squares-vector-21580913
        image(150,75,'back.png', ancrage='center')  # Source: https://www.interupgrade.com/images/pfeil-backbutton.png
        image(550,75,'menu.png', ancrage='center')  # Source: https://www.0ptim1ze.com/wp-content/uploads/white-37292_960_720.png
        image(320,75,'solveur.png', ancrage='center')  # Source: https://lutinbazar.fr/wp-content/uploads/2015/04/%C3%A9lec1-300x300.png
        affiche_num_colonne(colonnes_note,x=0,y=-1)
        affiche_num_ligne(lignes_note,x=-1,y=0)
        plateau(board)
        remplissage_plateau(board)
        icone_solveur(abscisse(ev),ordonnee(ev),solveur)
        solveur = icone_solveur(abscisse(ev),ordonnee(ev),solveur)
        ev = attend_ev()
        tev = type_ev(ev)
        mise_a_jour()
        if solveur == False:
            while tev != 'ClicGauche':
                ev = attend_ev()
                tev = type_ev(ev)
                mise_a_jour()
            case_select(board,history,abscisse(ev),ordonnee(ev))
        if solveur == True:
            solver(board, colonnes_note, lignes_note, note_musique, lineSolv, case)
        if abscisse(ev) > 450 and abscisse(ev) < 650 and ordonnee(ev) > 25 and ordonnee(ev) < 125:
            play_note = False
            menu = True

        if check_board(board,note_musique) == True:
            remplissage_plateau(board)# j'ai replacer le fonction remplissage ici parceque ça affichais pas la derniere case que tu selectionnais quand tu gagnais (°w°)
            play_note= False
            end = True
            Rejouer_Note=True


    while end == True:       # Fin de partie
        rectangle(100,300,675,380,couleur='silver', epaisseur=5, remplissage = 'white')
        texte(325,317,'Rejouer', couleur='lightgrey', police='Times', taille=38)
        texte(320,310,'Rejouer', couleur='black', police='Times', taille=38)
        rectangle(100,450,675,530,couleur='silver', epaisseur=5, remplissage = 'white')
        texte(220,467,'Choix de la grille', couleur='lightgrey', police='Times', taille=38)
        texte(215,460,'Choix de la grille', couleur='black', police='Times', taille=38)
        rectangle(100,600,675,680,couleur='silver', epaisseur=5, remplissage = 'white')
        texte(320,617,'Quitter', couleur='lightgrey', police='Times', taille=38)
        texte(315,610,'Quitter', couleur='black', police='Times', taille=38)
        history = []

        rectangle(40,100,735,190, couleur='gold',remplissage='white', epaisseur=3)
        texte(54,110,"Félicitation vous avez gagner", couleur ="white", taille= 38)
        texte(56,112,"Félicitation vous avez gagner", couleur ="brown", taille= 38)
        texte(58,114,"Félicitation vous avez gagner", couleur ="red", taille= 38)
        texte(60,116,"Félicitation vous avez gagner", couleur ="yellow", taille= 38)
        texte(62,118,"Félicitation vous avez gagner", couleur ="lime", taille= 38)
        texte(64,120,"Félicitation vous avez gagner", couleur ="deepskyblue", taille= 38)
        texte(66,122,"Félicitation vous avez gagner", couleur ="violet", taille= 38)
        texte(68,124,"Félicitation vous avez gagner", couleur ="black", taille= 38)

        ev = attend_ev()
        tev = type_ev(ev)
        if tev == 'ClicGauche':

            if abscisse(ev) < 675 and abscisse(ev) > 100 and ordonnee(ev) < 380 and ordonnee(ev) > 300:  # Pour rejouer
                if Rejouer_chat==True:
                    efface_tout()
                    end= False
                    play_chat=True
                    Rejouer_chat=False
                elif Rejouer_canard==True :
                    efface_tout()
                    end= False
                    play_canard=True
                    Rejouer_canard=False
                elif Rejouer_Note==True:
                    efface_tout()
                    end= False
                    play_note=True
                    Rejouer_Note=False


            if abscisse(ev) < 675 and abscisse(ev) > 100 and ordonnee(ev) < 530 and ordonnee(ev) > 450:  # Pour choisir/changer de grille
                efface_tout()
                end= False
                option= True
                efface_tout()
                mise_a_jour()
                if Rejouer_chat==True:
                    Rejouer_chat= False
                elif Rejouer_canard==True :
                    Rejouer_canard=False
                elif Rejouer_Note==True:
                    Rejouer_Note= False


            if abscisse(ev) < 675 and abscisse(ev) > 100 and ordonnee(ev) < 680 and ordonnee(ev) > 600:  # Pour quitter
                end = False
                game = False
                if Rejouer_chat==True: # je suis pas sûr de le mettre ici aussi, jsp si game= false , si sa reset tout ou si faut quand meme tout remettre a false
                    Rejouer_chat= False
                elif Rejouer_canard==True :
                    Rejouer_canard=False
                elif Rejouer_Note==True:
                    Rejouer_Note= False



ferme_fenetre()