import random 
x,y = ("a","b","c","d"),("1","2","3","4")
equipes = ("équipe 1","équipe 2")
jeu = 0
cases_attaques = {}

def paramètres():
    
    bat = input("Nombre de bateaux ?  (De base 4) : ")
    while bat.isdigit() == False or  int(bat) > 16 or int(bat) < 1:
        print("L'entrée n'est pas un nombre ou n'est pas valide veuiller recommencer")
        bat = input("Nombre de bateaux ? : ")
    bat = int(bat)
    print("Le nombre de bateaux sera:",bat)
    
    if input("Mode Débug (OUI(O) ou NON(N)): ") == "O":
        débug = True
    else :
        débug = False
    print("")
    
    print ("Type de Parties :\n"
           "Joueurs - Joueur = 2\n"
           "Joueur - Ordinateur = 1\n"
           "Ordinateur - Ordinateur = 0")
    nbr_joueurs = "10"
    while nbr_joueurs.isdigit() == False or int(nbr_joueurs) > 2 or  int(nbr_joueurs) < 0:
        nbr_joueurs = input("Nombre de joueurs humains: ")
    nbr_joueurs = int(nbr_joueurs)
    lst_para = [bat,débug,nbr_joueurs]
    return lst_para

def _init_game():
    cases = {}
    for i in equipes:
        for e in x:
            for g in y:
                cases[i,e,g] = "Rien"
                cases_attaques[i,e,g] = "Rien"
    print("Reset terminé")
    return cases


def coord_gén(case_bat,eq):
    xia = x[random.randint(0,4)]
    yia = y[random.randint(0,4)]
    gén = xia + yia 
    return gén
#while case_bat[eq,xia,yia] != "Rien" :  
    
def erreur_len(case_bats):
    print ("Coordonnées invalides veuiller recommencer ",)
    print (" ")
    case_bats = input("Coordonnées du bateau, Sous la forme: x (lettre), y(nombre) Ex: a3 : ")
    return case_bats

def erreur_cord(case_bats):
    if len(case_bats)>=3 or len(case_bats) <= 1:
        case_bats = erreur_len(case_bats)
        
    while case_bats[0] not in x or case_bats[1] not in y:
        case_bats = erreur_len(case_bats)
        
        if len(case_bats)>=3 :
            case_bats = erreur_len(case_bats)
    return case_bats
        
def bateaux():
    for e in equipes :
        print(" ")
        print("Tour de l'",e)
        
        for h in range(1,1+bat):
            print(" ")
            print("Bateau numéro :",h)
            case_bat = input("Coordonnées du bateau, Sous la forme: x (lettre), y(nombre) Ex: a3 : ")
            case_bat = erreur_cord(case_bat)
            
            er = 0
            while er == 0:
                i  = case_bat[0]
                g = case_bat[1]
                if cases[e,i,g] == "Rien":
                    cases[e,i,g] = "Bateau"
                    er = 1
                else :
                    print("Vous avez choisit les mêmes coordonnées qu'un autre bateau")
                    case_bat = erreur_len(case_bat)
        protection = 0
        while protection <= protec_général : 
            print(" ")
            protection += 1
    return cases

def affichage_départ(protec):
    for i in equipes:
        print ("Affichages bateaux :", i )
        if protec > 0 :
            input("Êtes vous prêt ? (Pas besoin de répondre) Protection contre la triche")
        
        for h in range (9):
            print("-", end = "")
        print("-")
        
        for g in y:
            print("|", end = "")
            
            for e in x:
                if cases[i,e,g] == "Rien":
                    print("/",end = " ")
                else :
                    print("O", end = " ")
            print( "|")
        
        for h in range (9):
            print("-", end = "")
        print("-")
        protection = 0
        if protec > 0 :
            input("Attente")
        while protection <= protec : 
            print(" ")
            protection += 1

def affichage_attaque(equipe):
    print ("Affichages carte de l",equipe )
    print ("/ = Rien|0 = Raté|X = Coulé")
    for h in range (9):
        print("-", end = "")
    print("-")
    
    for g in y:
        print("|", end = "")
        for e in x:
            
            if cases_attaques[equipe,e,g] == "Rien":
                print("/",end = " ")
            if cases_attaques[equipe,e,g] == "Raté":
                print("O", end = " ")
            if cases_attaques[equipe,e,g] == "Coulé":
                print("X", end = " ")
                
        print( "|")
    for h in range (9):
        print("-", end = "")
    print("-")
    
def tirs(equipe):
    affichage_attaque(equipe)
    tir = input("Coordonnées du tir, Sous la forme: x (lettre), y(nombre): ")
    tir = erreur_cord(tir)
    print (" Tir aux coordonées: ",tir)
    tirx = tir[0]
    tiry = tir[1]
    
    if cases[equipe,tirx,tiry] == "Bateau":
        print(" ")
        print("Coulé")
        print(" ")
        cases_attaques[equipe,tirx,tiry] = "Coulé"
        return 1

    else :
        print (" ")
        print("Raté")
        print(" ")
        cases_attaques[equipe,tirx,tiry] = "Raté"
        return 0
        
def bataille(equipes):
    bateq1 = 0
    bateq2 = 0
    tour = 0
    
    while tour == 0 and bateq1 < bat and bateq2 < bat :
        print ("Tour",equipes[0])
        print(" ")
        if tirs(equipes[1]) == 1:
            bateq2+=1
        else :
            tour = 1
        print("Nombre de bateaux restants de l'",equipes[1],bat-bateq2)
        
        while tour == 1 and bateq1 < bat and bateq2 < bat :
            print( "Tour",equipes[1])
            print(" ")
            if tirs(equipes[0]) == 1 :
                bateq1+=1
            else :
                tour = 0
        print("Nombre de bateaux restants de l'",equipes[0],bat-bateq1)

    if bateq2 == bat :
        input("L'",equipes[0],"a gagné")
    else :
        input("L'",equipes[1],"a gagné")
    print(affichage_départ(0))
    if input("Voulez vous faire une nouvelle partie ? (OUI(O) ou NON(N)) : ") == "O":
        return 0
    
def bases() :
    if input("Voulez-vous changer les paramètres ? (OUI(O) ou NON(N)): ") == "O":
        bat = paramètres()
    else :
        bat = 4
        débug = False
        
while jeu == 0 :
    i = input("Voulez-vous changer les paramètres ? (OUI(O) ou NON(N)): ")
    if i == "O":
        para = paramètres()
        bat = para[0]
        débug = para[1]
        nbr_joueurs = para[2]
    if i != "O" :
        bat = 4
        débug = False
        nbr_joueurs = 2
    
    if nbr_joueurs == 2:
        print("Partie Joueur contre Joueur")
    if nbr_joueurs == 1:
        print("Partie Joueur contre Ordinateur")
        equipes = ("équipe 1","Ordinateur")
    if nbr_joueurs == 0:
        print("Partie Ordinateur contre Ordinateur")
        equipes = ("Ordinateur 1","Ordinateur 2")
    if débug == False :
        protec_général = 80
    if débug == True :
        protec_général = 0
    cases = _init_game()
    cases = bateaux()
    affichage_départ(protec_général)
    jeu = bataille(equipes)

input("Merci d'avoir Joué")
