"""
La suite de syracuse
~~~~~~~~~~~~~~~~~~~

* Programme qui calcule la suite de Syracuse et donne des informations complémentaires.
* Ici, nous considérons que la suite est celle des altitudes d'une feuille.
"""

__title__ = "Syracuse"
__author__ = "Robin & Habib"

#! Importation des modules

# On importe pyplot de matplotlib pour la fontion affichageGraphique()
from matplotlib import pyplot


#! Définitions des fonctions

def saisiEntier() -> int:  # By Habib
    """Fonction qui demande à l'utilisateur de saisir un entier avec les contraintes suivantes:
        * Un message clair indique à l'utilisateur ce qui est attendu ;
        * La saisie au clavier du nombre doit être compris entre 2 et 200 ;
        * Si la valeur saisie n'est pas dans l'interval [2, 200], on demande à l'utilisateur de saisir à nouveau une valeur.

    Returns :
        int : Retourne l'entier entré par l'utilisateur (compris entre 2 et 200).

    Examples : 
        >>> saisiEntier()
        Saisissez un nombre qui doit être compris entre 2 et 200 : 200
        200
    """
    int_number = int(
        input("Saisissez un nombre qui doit être compris entre 2 et 200 : "))
    while int_number > 200 or int_number < 2:
        int_number = int(
            input("Saisissez un nombre qui doit être compris entre 2 et 200 : "))
    return int_number


def etapeSuivante(int_number: int) -> int:  # By Robin
    """Fonction qui calcule l'entier suivant dans la suite de Syracuse et le retourne.

    Args : 
        int_number (int): Un nombre entier strictement positif

    Returns :
        int : Retourne la valeur de l'entier suivant calculé

    Examples : 
        >>> etapeSuivante(5)
        16
        >>> etapeSuivante(16)
        8
    """
    # Si le nombre est paire :
    if (int_number % 2) == 0:
        int_number = int_number/2
    # Si le nombre est impaire :
    else:
        int_number = int_number*3+1.
    return int(int_number)


def vol(int_number: int) -> list:  # By Robin
    """Fonction qui crée une liste contenant la première valeur de la suite et en utilisant la fonction etapeSuivante(),
       calcule et stocke dans la liste créée les termes de la suite de syracuse de l'entier initial jusqu'à 1 inclus.

    Args : 
        int_number (int): Un nombre entier strictement positif

    Returns :
        list : Retourne la liste avec les termes de la suite de syracuse de l'entier initial jusqu'à 1 inclus

    Examples : 
        >>> vol(11)
        [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    flight_list = [int_number]
    while int_number != 1:
        int_number = etapeSuivante(int_number)
        flight_list.append(int_number)
    return flight_list


def tempsVol(int_list: list) -> int:  # By Habib
    """Fonction qui calcule la valeur du temps de vol.

    Args : 
        int_list (list): Une liste contenant uniquement des entiers strictement positif

    Returns :
        int : Retourne la valeur du temps de vol sous forme d'un entier

    Examples : 
        >>> var = [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> vol(var)
        14
    """
    return len(int_list)


def altMaxi(int_list: list) -> int:  # By Habib
    """Fonction qui détermine l'altitude maximale de la suite qui peut être la valeur initiale.

    Args : 
        int_list (list): Une liste contenant uniquement des entiers strictement positif

    Returns :
        int : Retourne la valeur de l'altitude maximale de la suite

    Examples : 
        >>> var = [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> altMaxi(var)
        52
    """
    int_max = int_list[0]
    for i in int_list:
        if int_max < i:
            int_max = i
    return int_max


def tempsVolAltitude(int_list: list) -> int:  # By Habib
    """Fonction qui détermine le temps de vol en altitude, le nombre d'étapes nécessaires pour redescendre en dessous de l'altitude initiale.

    Args : 
        int_list (list): Une liste contenant uniquement des entiers strictement positif

    Returns :
        int : Retourne la valeur du temps de vol en altitude

    Examples : 
        >>> var = [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> tempsVolAltitude(var)
        8
    """
    time_flight_altitude = 0
    int_value = int_list[0]
    for i in int_list:
        time_flight_altitude = time_flight_altitude + 1
        if int_value > i:
            return time_flight_altitude


def affichageGraphique(x_list: list) -> None:  # By Robin
    """Fonction qui crée et affiche la courbe de la liste entrée en argument.

    Args : 
        x_list (list): Une liste contenant uniquement des entiers strictement positif

    Returns :
        None : Retourne rien

    Examples : 
        >>> var = [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> affichageGraphique(var)

        [Résultat](https://cdn.discordapp.com/attachments/896804633555648515/911937836327002122/unknown.png)
    """
    pyplot.axis([0, len(x_list)-1, min(x_list), max(x_list)+1])
    pyplot.plot(range(len(x_list)), x_list, "b*--")
    pyplot.xlabel("Temps")
    pyplot.ylabel("Hauteur")
    pyplot.title("Graphique de la suite de Syracuse")
    pyplot.show()
    return None


#! Programme Principal
while True:
    # On demande le premier entier de la suite de syracuse qu'on veut calculer
    int_number = saisiEntier()
    # On calcule la suite de syracuse selon l'entier entré précédement
    flight = vol(int_number)
    # On calcule la valeur du temps de vol
    flight_time = tempsVol(flight)
    # On détermine l'altitude maximale de la suite
    max_flight_altitude = altMaxi(flight)
    # On détermine le temps de vol en altitude
    time_flight_altitude = tempsVolAltitude(flight)
    # On transforme la liste en chaine de caractères avec chaques éléments de la liste séparé par une virgule
    flight_str = str(flight)
    # On affiche le résultat du programme avec les informations complémentaires
    print("La suite de Syracuse :", flight_str, "\n" +
          "Le temps de vol :", flight_time, "\n" +
          "L'altitude maximal :", max_flight_altitude, "\n" +
          "Le temps avant avant de redescendre :", time_flight_altitude, "\n")
    # On affiche le graphique de la suite
    affichageGraphique(flight)
