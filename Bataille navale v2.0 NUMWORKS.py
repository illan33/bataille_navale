import random
# Initailisation :
x,y = ("a","b","c","d"),("1","2","3","4")
equipes = ("équipe 1","équipe 2")
jeu = 0
cases_attaques = {}

def paramètres():
    
    bat = input("Nombre de bateaux ?\n(De base 4) : ")
    while bat.isdigit() == False or  int(bat) > 16 or int(bat) < 1:
        print("L'entrée n'est pas un nombre\nou n'est pas valide veuiller recommencer")
        bat = input("Nombre de bateaux ? : ")
    bat = int(bat)
    print("Le nombre de bateaux\nsera:",bat)
    
    if input("Mode Débug\n(OUI(O) ou NON(N)): ") == "O":
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
    print("Reset terminé\n")
    return cases
# Fonctions gérant les erreurs :
def erreurs_coord(case_bats):
    print ("Coordonnées invalides\nveuiller recommencer ",)
    print (" ")
    case_bats = input("Coordonnées,\nSous la forme:\nx (lettre), y(nombre)\nEx: a3 : ")
    return case_bats

def erreurs_(case_bats):
    while len(case_bats)>=3 or len(case_bats) <= 1:
        while case_bats[0] not in x or case_bats[1] not in y:
            case_bats = erreurs_coord(case_bats)
    return case_bats

# Fonctions gérant le placement des bateaux :
def chx_bateaux_h(eq):   
    print(" ")
    for h in range(1,1+bat):
        print(" ")
        print("Bateau numéro :",h)
        case_bat = input("Coordonnées du bateau,\nSous la forme:\nx (lettre), y(nombre)\nEx: a3 : ")
        case_bat = erreurs_(case_bat)
        
        er = 0
        while er == 0:
            i  = case_bat[0]
            g = case_bat[1]
            if cases[eq,i,g] == "Rien":
                cases[eq,i,g] = "Bateau"
                er = 1
            else :
                print("Vous avez choisit\nles mêmes coordonnées\nqu'un autre bateau")
                case_bat = erreurs_coord(case_bat)
    protection = 0
    while protection <= protec_général : 
        print(" ")
        protection += 1
    return cases

def chx_bateaux_bot(eq):
    h = bat
    while h != 0 :
        gén = coord_gén()
        xia = gén[0]
        yia = gén[1]
        if cases[eq,xia,yia] == "Rien" :
            cases[eq,xia,yia] = "Bateau"
            h -=1
    print("Placement des bateaux,\nde l'",eq,"réussie\n")
    return cases
# Fontion créatrice de coordonnées :
def coord_gén():
    xia = x[random.randint(0,3)]
    yia = y[random.randint(0,3)]
    gén = xia + yia 
    return gén
#  Fonctions d'affichages :
def affichage_départ(protec):
    for i in equipes:
        print ("Affichages bateaux de l':", i )
        if protec > 0 :
            input("Êtes vous prêt ?\n(Pas besoin de répondre)\nProtection contre la triche")
            print(" ")
        for h in range (9):
            print("-", end = "")
        print("-")
        
        for g in y:
            print("|", end = "")
            
            for e in x:
                if cases[i,e,g] == "Rien":
                    print("/",end = " ")
                else :
                    print("X", end = " ")
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
    print ("Affichages carte de l'",equipe )
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
# Fonction des Tirs :    
def tirs(eq,tipe):
    affichage_attaque(eq)
    if tipe == "N":
        tir = input("Coordonnées du tir,\nSous la forme:\nx (lettre), y(nombre): ")
        tir = erreurs_(tir)
    else :
        h = 0
        while h ==0 :
            tir = coord_gén()
            tir_xia = tir[0]
            tir_yia = tir[1]
            if cases_attaques[eq,tir_xia,tir_yia] == "Rien":
                h = 1
    print ("Tir aux coordonées: ",tir, end = ' ')
    if débug == True :
        print("")
    if débug == False :
        input ("")
    tirx = tir[0]
    tiry = tir[1]
    
    if cases[eq,tirx,tiry] == "Bateau":
        print(" ")
        print("Coulé")
        print(" ")
        cases_attaques[eq,tirx,tiry] = "Coulé"
        return 1

    else :
        print (" ")
        print("Raté")
        print(" ")
        cases_attaques[eq,tirx,tiry] = "Raté"
        return 0
# Fonction gérant les Tirs et les tours :
def bataille(eq):
    bateq1 = 0
    bateq2 = 0
    tour = 0
    tipes = ["N","N"]
    
    for equipe in eq :
        if equipe == "équipe 1" or equipe == "équipe 2":
            print("C'est à\nl'",equipe,"de répondre")
            if input ("Voulez vous générer\nvos tirs aléatoirements ?\n(OUI(O) ou NON(N): ") == "O" :
                tipes[eq.index(equipe)] = "O"
        else :
            tipes[eq.index(equipe)] = "O"
    while tour == 0 and bateq1 < bat and bateq2 < bat :
        print ("Tour",eq[0])
        if tirs(eq[1],tipes[0]) == 1:
            bateq2+=1
        else :
            tour = 1
        print("Nombre de bateaux restants\nde l'",eq[1],":",bat-bateq2)
        
        while tour == 1 and bateq1 < bat and bateq2 < bat :
            print( "Tour",eq[1])
            print(" ")
            if tirs(eq[0],tipes[1]) == 1 :
                bateq1+=1
            else :
                tour = 0
        print("Nombre de bateaux restants\nde l'",eq[0],":",bat-bateq1)
    input ("Affichages des tirs")
    for equipe in eq :
        affichage_attaque(equipe)
    input ("Affichages des bateaux")
    affichage_départ(0)
    if bateq2 == bat :
        print("L'",eq[0],"a gagné")
    else :
        print("L'",eq[1],"a gagné")
    if input("Voulez vous faire une nouvelle partie ?\n(OUI(O) ou NON(N)) : ") == "O":
        return 0

# Jeu en lui même utilisant les fonctions du dessus
while jeu == 0 :
    print("Bonne partie !")
    i = input("Voulez-vous changer\nles paramètres ?\n(OUI(O) ou NON(N)): ")
    if i == "O":
        para = paramètres()
        bat = para[0]
        débug = para[1]
        nbr_joueurs = para[2]
    if i != "O" :
        bat = 4
        débug = False
        nbr_joueurs = 2

    if débug == False :
        protec_général = 80
    if débug == True :
        protec_général = 0
    
    
    if nbr_joueurs == 2:
        print("Partie Joueur contre\nJoueur")
        
    if nbr_joueurs == 1:
        print("Partie Joueur contre\nOrdinateur")
        equipes = ("équipe 1","Ordinateur")
        protec_général = 0
        
    if nbr_joueurs == 0:
        print("Partie Ordinateur contre\nOrdinateur")
        equipes = ("Ordinateur 1","Ordinateur 2")
        protec_général = 0
        
    cases = _init_game()
    
    for g in equipes:
        if g == "équipe 1" or g == "équipe 2":
            print("Tour de l'",g)
            if input("Voulez vous générer\nvos bateaux aléatoirement ?\n(OUI(O) ou NON(N): ") == "O" :
                cases = chx_bateaux_bot(g)
            else :
                cases = chx_bateaux_h(g)
        else :
            cases = chx_bateaux_bot(g)
    
    affichage_départ(protec_général)
    jeu = bataille(equipes)

input("Merci d'avoir Joué")
