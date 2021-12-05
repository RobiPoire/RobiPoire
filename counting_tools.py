"""
Outils de numération
~~~~~~~~~~~~~~~~~~~

Contient deux fonctions :
* Une qui permet de convertir un nombre d'une base x à une base y.
* Et une autre qui permet de calculer des nombres de même base.
"""

__title__ = "Counting Tools"
__author__ = "RobiPoire"


#! Importation des modules

from math import pow, log


#! Définition des erreurs

class BaseTooSmall(Exception):
    def __str__(self):
        return f"Vous devez rentrez une base plus grande que {Exception.__str__(self)} !"


class BaseTooLarge(Exception):
    def __str__(self):
        return f"Vous devez rentrez une base plus petite que {Exception.__str__(self)} !"


class IncorrectCalcul(Exception):
    def __str__(self):
        return 'Ceci est un calcul incorrect, veuilliez rentrer "+", "-", "*" ou "/" !'


#! Définitions des fonctions

def base_convert(str_number: str, old_base: int, new_base: int):
    """Convertit un nombre d'une ancienne base à une nouvelle base.

    Args:
        str_number (str): Nombre entier à convertir.
        old_base (int): Base du nombre entré.
        new_base (int): Nouvelle base du nombre.

    Raises:
        BaseTooSmall: Si une base est inférieur à 2.
        BaseTooLarge: Si une base est supérieur à 36.

    Returns:
        str : Nombre converti à la nouvelle base.

    Examples : 
        >>> base_convert("F", 16, 10)
        15
    """
    if old_base < 2 or new_base < 2:
        raise BaseTooSmall("1")
    if new_base > 36 or old_base > 36:
        raise BaseTooLarge("37")
    try:
        str_number = str_number.lower()
    except:
        pass
    characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
                  'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    nbr_dec = 0
    i = len(str_number) - 1
    for x in str_number:
        nbr_dec += characters.index(x) * int(pow(old_base, i))
        i -= 1
    nbr_chars = int(log(nbr_dec)/log(new_base) + 1)
    nbr_final = ""
    for i in range(0, nbr_chars):
        x = int(nbr_dec / pow(new_base, nbr_chars-1-i))
        nbr_dec -= int(x * pow(new_base, nbr_chars-1-i))
        nbr_final += characters[x]
    return nbr_final


def base_calculator(str_number_one: str, str_number_two: str, base: int, calcul: str = "+"):
    """Calcule un nombre de n'importe quel base.

    Args:
        str_number_one (str): 1er nombre entier à calculer.
        str_number_two (str): 2eme nombre entier à calculer.
        base (int): La base des deux nombres.
        calcul (str, optional): L'opération. Defaults to "+".

    Raises:
        BaseTooSmall: Si une base est inférieur à 2.
        BaseTooLarge: Si une base est supérieur à 36.
        IncorrectCalcul: Si le calcul n'est pas "+", "-", "*" ou "/".

    Returns:
        str: Retourne le resultat.

    Examples : 
        >>> base_calculator("F", "3", 16, "*")
        42
    """
    if base < 2:
        raise BaseTooSmall("1")
    if base > 36:
        raise BaseTooLarge("37")
    if calcul == "+":
        result = int(base_convert(str_number_one, base, 10)) + \
            int(base_convert(str_number_two, base, 10))
        result = base_convert(str(result), 10, base)
        return result
    elif calcul == "-":
        result = int(base_convert(str_number_one, base, 10)) - \
            int(base_convert(str_number_two, base, 10))
        result = base_convert(str(result), 10, base)
        return result
    elif calcul == "*":
        result = int(base_convert(str_number_one, base, 10)) * \
            int(base_convert(str_number_two, base, 10))
        result = base_convert(str(result), 10, base)
        return result
    elif calcul == "/":
        result = int(base_convert(str_number_one, base, 10)) / \
            int(base_convert(str_number_two, base, 10))
        result = base_convert(str(result), 10, base)
        return result
    else:
        raise IncorrectCalcul
