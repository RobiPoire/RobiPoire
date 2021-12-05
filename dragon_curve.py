"""
La courbe du Dragon
~~~~~~~~~~~~~~~~~~~

Fonction qui calcule la courbe du dragon selon l'entier entré.
"""

__title__ = "Dragon Curve"
__author__ = "RobiPoire"


#! Définition des erreurs

class TooSmall(Exception):
    def __str__(self):
        return f"Vous devez rentrez un nombre supérieur à {Exception.__str__(self)} !"


#! Définitions des fonctions

def dragon_curve(int_number: int):
    """Calcule la courbe du dragon selon le nombre entier entré.

    Args:
        int_number (int): Nombre entier supérieur ou égale à 1.

    Raises:
        TooSmall: Si le nombre est inférieur ou égal à 1.

    Returns:
        [list]: Retourne une liste avec des nombres entiers supérieur ou égal à 1.

    Examples : 
        >>> dragon_curve(5)
        0010011000110110001001110011011
    """
    if int_number <= 1:
        raise TooSmall(0)
    results_str = "0"
    for i in range(2, int_number + 1):
        a = "0"
        b = "0"
        for j in range(len(results_str)):
            a += results_str[j]
            if b == "1":
                a += "0"
                b = "0"
            else:
                a += "1"
                b = "1"
        results_str = a
    return results_str


print(dragon_curve(5))
