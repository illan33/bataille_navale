bat = 4
y = ("1","2","3","4")
x = ("a","b","c","d")
equipes = ("eq1","eq2")

def paramètres():
    bat = input("Nombre de bateaux ? : ")
    
    while bat.isdigit() == False or  int(bat) > 16 or int(bat) < 1:
        print("L'entrée n'est pas un nombre  ou n'est pas valide veuiller recommencer")
        bat = input("Nombre de bateaux ? : ")
        
    bat = int(bat)
    print("Le nombre de bateaux sera:",bat)
    return bat

def reset():
    cases = {}
    for i in equipes:
        for e in x:
            for g in y:
                cases[i,e,g] = "Rien"
    print("Reset terminé")
    return cases

def erreur_len(case_bats):
    print ("Coordonnées invalides veuiller recommencer ",)
    print (" ")
    case_bats = input("Coordonnées du bateau, Sous la forme x (lettre), y(nombre): ")
    return case_bats

def erreur_cord(case_bats):
    if len(case_bats)>=3 :
       case_bats = erreur_len(case_bats)
    while case_bats[0] not in x or case_bats[1] not in y:
        print ("Coordonnées invalides veuiller recommencer ",)
        print (" ")
        case_bats = input("Coordonnées du bateau, Sous la forme x (lettre), y(nombre): ")
        if len(case_bats)>=3 :
            case_bats = erreur_len(case_bats)
    return case_bats
        
def bateaux():
    for e in equipes :
        print("Tour de",e)
        
        for h in range(1,1+bat):
            print(" ")
            print("Bateau numéro :",h)
            case_bat = input("Coordonnées du bateau, Sous la forme x (lettre), y(nombre): ")
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
                    case_bat = erreur_cord(case_bat)
        protection = 0
        while protection <= 20 : 
            print(" ")
            protection += 1
    return cases

if input("Voulez-vous changer les paramètres ? (OUI ou NON): ") == "OUI":
    bat = paramètres()
cases = reset()
cases = bateaux()
        
        

