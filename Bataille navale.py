y = ("1","2","3","4")
x = ("a","b","c","d")
equipes = ("équipe 1","équipe 2")
tour = 0
jeu = 0
débug = False
cases_attaques = {}
def paramètres():
    bat = input("Nombre de bateaux ? (De base 4) : ")
    while bat.isdigit() == False or  int(bat) > 16 or int(bat) < 1:
        print("L'entrée n'est pas un nombre  ou n'est pas valide veuiller recommencer")
        bat = input("Nombre de bateaux ? : ")
    bat = int(bat)
    print("Le nombre de bateaux sera:",bat)
    
    if input("Mode Débug (OUI ou NON): ") == "OUI":
        débug = True
    else :
        débug = False
    lst_para = [bat,débug]
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

def erreur_len(case_bats):
    print ("Coordonnées invalides veuiller recommencer ",)
    print (" ")
    case_bats = input("Coordonnées du bateau, Sous la forme x (lettre), y(nombre) Ex: a3 : ")
    return case_bats

def erreur_cord(case_bats):
    if len(case_bats)>=3 or len(case_bats) <= 1:
        case_bats = erreur_len(case_bats)
        
    while case_bats[0] not in x or case_bats[1] not in y:
        print ("Coordonnées invalides veuiller recommencer ",)
        print (" ")
        case_bats = input("Coordonnées du bateau, Sous la forme x (lettre), y(nombre) Ex: a3 : ")
        
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
            case_bat = input("Coordonnées du bateau, Sous la forme x (lettre), y(nombre) Ex: a3 : ")
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
    print (f"Affichages carte de l' {equipe}" )
    print ("/ = Rien 0 = Raté X = Coulé")
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
    tir = input("Coordonnées du tir, Sous la forme x (lettre), y(nombre): ")
    tir = erreur_cord(tir)
    print (" Tir aux coordonées : ",tir)
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
        
def bataille():
    bat1 = 0
    bat2 = 0
    tour = 0
    
    while tour == 0 and bat1 < bat and bat2 < bat :
        print ("Tour équipe 1")
        print(" ")
        if tirs("équipe 2") == 1:
            bat2+=1
        else :
            tour = 1
        print("Nombre de bateau restant de l'équipe 2 :",bat-bat2)
        
        while tour == 1 and bat1 < bat and bat2 < bat :
            print( "Tour équipe 2")
            print(" ")
            if tirs("équipe 1") == 1 :
                bat1+=1
            else :
                tour = 0
        print("Nombre de bateau restant de l'équipe 1 :",bat-bat1)

    if bat2 == bat :
        input("Le joueur 1 a gagné")
    else :
        input("Le joueur 2 a gagné")
    print(affichage_départ(0))
    if input("Voulez vous faire une nouvelle partie (OUI ou NON) : ") == "OUI":
        return 0
    
def bases() :
    if input("Voulez-vous changer les paramètres ? (OUI ou NON): ") == "OUI":
        bat = paramètres()
    else :
        bat = 4
        débug = False
        
while jeu == 0 :
    if input("Voulez-vous changer les paramètres ? (OUI ou NON): ") == "OUI":
        para = paramètres()
        bat = para[0]
        débug = para[1]
    else :
        bat = 4
        débug = False
        
    if débug == False :
        protec_général = 200
    else :
        protec_général = 0
    cases = _init_game()
    cases = bateaux()
    affichage_départ(protec_général)
    jeu = bataille()

input("Merci d'avoir Joué")

