"""
La bataille navoul coloré
~~~~~~~~~~~~~~~~~~~

Un jeux incroyable avec une intéligence artificiel incroyable
"""

__title__ = "La bataille navoul coloré"
__author__ = "Zazizou & RobiPoire"


#! Importation des modules

from random import randint
from colorama import Fore


#! Définitions des fonctions

def newTab():
    t = []
    for i in range(10):
        t.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    return t


def displayTab(tab, playertab):
    print(f"{Fore.YELLOW} | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |{Fore.RESET}")
    print(f"{Fore.YELLOW}-----------------------------------------{Fore.RESET}")
    for i in range(10):
        stri = ""
        if i == 0:
            stri = f"{Fore.YELLOW}A|{Fore.RESET}"
        if i == 1:
            stri = f"{Fore.YELLOW}B|{Fore.RESET}"
        if i == 2:
            stri = f"{Fore.YELLOW}C|{Fore.RESET}"
        if i == 3:
            stri = f"{Fore.YELLOW}D|{Fore.RESET}"
        if i == 4:
            stri = f"{Fore.YELLOW}E|{Fore.RESET}"
        if i == 5:
            stri = f"{Fore.YELLOW}F|{Fore.RESET}"
        if i == 6:
            stri = f"{Fore.YELLOW}G|{Fore.RESET}"
        if i == 7:
            stri = f"{Fore.YELLOW}H|{Fore.RESET}"
        if i == 8:
            stri = f"{Fore.YELLOW}I|{Fore.RESET}"
        if i == 9:
            stri = f"{Fore.YELLOW}J|{Fore.RESET}"

        for j in range(10):
            char = ''
            if tab[i][j] == 0:
                char = "   "
            if playertab:
                if tab[i][j] == 1:
                    char = "   "
                if tab[i][j] == 2:
                    char = f"{Fore.GREEN} O {Fore.RESET}"
                if tab[i][j] == 3:
                    char = f"{Fore.RED} X {Fore.RESET}"
            else:
                if tab[i][j] == 1:
                    char = f" {Fore.CYAN}• {Fore.RESET}"
                if tab[i][j] == 2:
                    char = "   "
                if tab[i][j] == 3:
                    char = f"{Fore.RED} X {Fore.RESET}"

            stri += char
            stri += f"{Fore.YELLOW}|{Fore.RESET}"
        print(stri)
        print(f"{Fore.YELLOW}-----------------------------------------{Fore.RESET}")


def newBoat(tab, boat, horizontal, x, y):
    if horizontal:
        if x+boat > 10:
            return 1

        for i in range(boat):
            if not tab[y][x+i] == 0:
                return 1
        for i in range(boat):
            tab[y][x+i] = 2
    else:
        if y+boat > 10:
            return 1
        for i in range(boat):
            if not tab[y+i][x] == 0:
                return 1
        for i in range(boat):
            tab[y+i][x] = 2
    return tab


def touche(tab, x, y):
    if tab[y][x] == 2 or tab[y][x] == 3:
        tab[y][x] = 3
        print(
            f"{Fore.BLUE}|================[Touché!]================|{Fore.RESET}")
        return True
    else:
        tab[y][x] = 1
        print(
            f"{Fore.BLUE}|================[Manqué!]================|{Fore.RESET}")
        return False


def couler(tab, boats):
    for i in boats:
        x = i[2]
        y = i[3]
        if not i[4]:
            if i[1]:
                for j in range(i[0]):
                    if tab[y][x+j] == 3:
                        if j == i[0]-1:
                            i[4] = True
                            print(
                                f"{Fore.BLUE}|================[Coulé! ]================|{Fore.RESET}")
                            return True
                    else:
                        break
            else:
                for k in range(i[0]):
                    if tab[y+k][x] == 3:
                        if k == i[0]-1:
                            print(
                                f"{Fore.BLUE}|================[Coulé! ]================|{Fore.RESET}")
                            i[4] = True
                            return True
                    else:
                        break
    return False


def victoire(liste):
    for i in liste:
        if not i[4]:
            return False
    return True


def convert(case):
    try:
        y = int(case[1])-1
        if len(case) > 2:
            if int(case[1]) == 1 and int(case[2]) == 0:
                y = 9
            else:
                return 1
        x = case[0]
        if x == 'A':
            x = 0
        elif x == 'B':
            x = 1
        elif x == 'C':
            x = 2
        elif x == 'D':
            x = 3
        elif x == 'E':
            x = 4
        elif x == 'F':
            x = 5
        elif x == 'G':
            x = 6
        elif x == 'H':
            x = 7
        elif x == 'I':
            x = 8
        elif x == 'J':
            x = 9
        else:
            return 1
        if x > 9 or y > 9:
            return 1
        return [y, x]
    except Exception as e:
        return 1


def verif(n):
    if n == 9:
        return 8
    elif n == 0:
        return 1
    else:
        return n

#[False, x, y, direction, xorigine, yorigine]
# ( 5 = aucune, 0 = Nord, 1 = Sud, 2 = ouest, 3 = Est)


def tirerComputer(tab, memoire, boats):
    if memoire[0]:
        erreur = True
        while(erreur):
            ty = randint(0, 9)
            if ty % 2 == 1:
                tx = randint(0, 4)*2
            else:
                tx = randint(0, 4)*2+1
            if tab[ty][tx] == 0 or tab[ty][tx] == 2:
                if touche(tab, tx, ty):
                    memoire[0] = False
                    memoire[1] = tx
                    memoire[2] = ty
                    memoire[3] = 5
                    memoire[4] = tx
                    memoire[5] = ty
                    if couler(tab, boats):
                        memoire[0] = True
                erreur = False
    else:
        if memoire[3] == 5:
            x = memoire[1]
            y = memoire[2]
            if tab[verif(y)+1][x] == 0 or tab[verif(y)+1][x] == 2:
                if touche(tab, x, y+1):
                    memoire[3] = 0
                    memoire[2] = y+1
                    if couler(tab, boats):
                        memoire[0] = True

            elif tab[verif(y)-1][x] == 0 or tab[verif(y)-1][x] == 2:
                if touche(tab, x, y-1):
                    memoire[3] = 1
                    memoire[2] = y-1
                    if couler(tab, boats):
                        memoire[0] = True

            elif tab[y][verif(x)-1] == 0 or tab[y][verif(x)-1] == 2:
                if touche(tab, memoire[1]-1, y):
                    memoire[3] = 2
                    memoire[1] = x-1
                    if couler(tab, boats):
                        memoire[0] = True

            elif tab[y][verif(x)+1] == 0 or tab[y][verif(x)+1] == 2:
                if touche(tab, x+1, y):
                    memoire[3] = 3
                    memoire[1] = x+1
                    if couler(tab, boats):
                        memoire[0] = True

            else:
                memoire[0] = True

        else:
            if memoire[3] == 0:
                x = memoire[1]
                y = verif(memoire[2])+1
                memoire[1] = x
                memoire[2] = y
                if tab[y][x] == 0 or tab[y][x] == 2:
                    if not touche(tab, x, y):
                        memoire[3] = 5
                        memoire[1] = memoire[4]
                        memoire[2] = memoire[5]
                    if couler(tab, boats):
                        memoire[0] = True
                else:
                    memoire[3] = 5
                    memoire[1] = memoire[4]
                    memoire[2] = memoire[5]

            if memoire[3] == 1:
                x = memoire[1]
                y = verif(memoire[2])-1
                memoire[1] = x
                memoire[2] = y
                if tab[y][x] == 0 or tab[y][x] == 2:
                    if not touche(tab, x, y):
                        memoire[3] = 5
                        memoire[1] = memoire[4]
                        memoire[2] = memoire[5]
                    if couler(tab, boats):
                        memoire[0] = True
                else:
                    memoire[3] = 5
                    memoire[1] = memoire[4]
                    memoire[2] = memoire[5]

            if memoire[3] == 2:
                x = verif(memoire[1])-1
                y = memoire[2]
                memoire[1] = x
                memoire[2] = y
                if tab[y][x] == 0 or tab[y][x] == 2:
                    if not touche(tab, x, y):
                        memoire[3] = 5
                        memoire[1] = memoire[4]
                        memoire[2] = memoire[5]
                    if couler(tab, boats):
                        memoire[0] = True
                else:
                    memoire[3] = 5
                    memoire[1] = memoire[4]
                    memoire[2] = memoire[5]

            if memoire[3] == 3:
                x = verif(memoire[1])+1
                y = memoire[2]
                memoire[1] = x
                memoire[2] = y
                if tab[y][x] == 0 or tab[y][x] == 2:
                    if not touche(tab, x, y):
                        memoire[3] = 5
                        memoire[1] = memoire[4]
                        memoire[2] = memoire[5]
                    if couler(tab, boats):
                        memoire[0] = True
                else:
                    memoire[3] = 5
                    memoire[1] = memoire[4]
                    memoire[2] = memoire[5]


#! Programme Principal

#=====================================[placement des bateaux]=====================================#
horizontal = True
bateauComputer = []
bateauPlayer = []
player = newTab()
computer = newTab()
size = 0

# mise en place des bateaux de l'ordinateur

for i in range(5):
    size = 0
    if i == 0:
        size = 5
    if i == 1:
        size = 4
    if i == 2 or i == 3:
        size = 3
    if i == 4:
        size = 2
    erreur = True
    while(erreur):
        x = randint(0, 7)
        y = randint(0, 7)
        tirage = randint(0, 1)
        orientation = False
        if tirage == 1:
            orientation = True

        if newBoat(computer, size, orientation, x, y) == 1:
            None
        else:
            bateauComputer.append([size, orientation, x, y, False])
            erreur = False

# print(bateauComputer)
# displayTab(computer,True)
print(f"{Fore.MAGENTA}Programme par Elouan et Robin, bon jeu ;){Fore.RESET} \n")

for i in range(5):
    if i == 0:
        print(
            f"{Fore.BLUE}|=============[Porte avion (5 cases)]=============|{Fore.RESET}")
        size = 5
    if i == 1:
        print(
            f"{Fore.BLUE}|==============[Croiseur (4 cases)]==============|{Fore.RESET}")
        size = 4
    if i == 2 or i == 3:
        print(
            f"{Fore.BLUE}|==============[Sous-marin (3 cases)]==============|{Fore.RESET}")
        size = 3
    if i == 4:
        print(
            f"{Fore.BLUE}|==============[Torpilleur (2 cases)]==============|{Fore.RESET}")
        size = 2

    t = True
    while t:
        inp = input(
            f"{Fore.BLUE}Voulez vous le placer de manière horizontal ou vertical (v ou h)? -> {Fore.RESET}")

        if inp == "h":
            horizontal = True
            t = False
        elif inp == "v":
            horizontal = False
            t = False
        else:
            print(f'{Fore.BLUE}Entrée invalide, veuillez reesayer{Fore.RESET}')

    displayTab(player, True)
    t = True
    while t:
        inp = input(
            f"{Fore.BLUE}Quelle case? (lettre en majuscule ex: B5) -> {Fore.RESET}")
        if not convert(inp) == 1:
            inp = convert(inp)
            if newBoat(player, size, horizontal, inp[0], inp[1]) == 1:
                t = True
                print(
                    f"{Fore.BLUE}Le bateau ne rentre pas ou est obstrué par un autre bateau, veuillez réessayer:{Fore.RESET}")
            else:
                bateauPlayer.append([size, horizontal, inp[0], inp[1], False])
                t = False
                displayTab(player, True)
        else:
            print(f"{Fore.BLUE}Entrée invalide veuillez réessayer{Fore.RESET}")


#=====================================[Main loop]=====================================#

memoire = [True, 0, 0, 5, 0, 0]

print("\n \n")
input(f"{Fore.BLUE}[Appuyez sur entrée pour continuer]{Fore.RESET}")
print("\n \n")

print(f"{Fore.BLUE}Début de la partie, bonne chance:{Fore.RESET}")
while not victoire(bateauComputer) and not victoire(bateauPlayer):
    print(f"{Fore.BLUE}================Sa grille:================{Fore.RESET}")
    displayTab(computer, False)
    t = True
    while t:
        inp = input(f"{Fore.BLUE}Où tirez-vous? -> {Fore.RESET}")
        if not convert(inp) == 1:
            inp = convert(inp)
            t = False
            touche(computer, inp[0], inp[1])
            couler(computer, bateauComputer)
            displayTab(computer, False)
        else:
            print(f"{Fore.BLUE}Entrée invalide veuillez réessayer:{Fore.RESET}")

    print("\n \n")
    input(f"{Fore.BLUE}[Appuyez sur entrée pour continuer]{Fore.RESET}")
    print("\n \n")
    print(f"{Fore.BLUE}Au tour de l'ordinateur:{Fore.RESET}")
    tirerComputer(player, memoire, bateauPlayer)
    print(f"{Fore.BLUE}===============Votre grille:==============={Fore.RESET}")
    displayTab(player, True)
    print("\n \n")
    input(f"{Fore.BLUE}[Appuyez sur entrée pour continuer]{Fore.RESET}")
    print("\n \n")

if victoire(bateauPlayer):
    print(
        f"{Fore.BLUE}|=============[Vous avez perdu!]=============|{Fore.RESET}")
if victoire(bateauComputer):
    print(
        f"{Fore.BLUE}|=============[Vous avez gagné!]=============|{Fore.RESET}")

print("\n \n")
input(f"{Fore.BLUE}[Appuyez sur entrée pour continuer]{Fore.RESET}")
print("\n \n")

print(f"{Fore.BLUE}|=========[Grille de l'adversaire:]=========|{Fore.RESET}")
displayTab(computer, True)
print(f"{Fore.BLUE}|==============[Votre gille:]==============|{Fore.RESET}")
displayTab(player, True)
