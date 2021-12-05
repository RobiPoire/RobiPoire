"""
Outil Trînome
~~~~~~~~~~~~~~~~~~~

Fonction pour calculer des trinômes.
"""

__title__ = "Trinomial"
__author__ = "RobiPoire"

#! Importation des modules

from math import sqrt


#! Définitions des fonctions

def trinomial(a: float, b: float, c: float):
    """Calcule Alpha, Beta, Delta et les racines d'un trinôme.

    Args:
        a (float): Nombre flottant non égale à 0.
        b (float): Nombre flottant
        c (float): Nombre flottant

    Raises:
        NotTrinomial: Si a est égale à 0.

    Returns:
        [dict]: Dictionaire avec toutes les informations sur le trinome.
    """
    result = dict()
    result["alpha"] = (-b)/(2*a)
    result["beta"] = a*(result["alpha"]**2)+b*result["alpha"]+c
    result["delta"] = b**2-(4*a*c)
    if result["delta"] > 0:
        x1 = (-b-sqrt(result["delta"]))/2*a
        x2 = (-b+sqrt(result["delta"]))/2*a
        result["racines"] = [x1, x2]
    elif result["delta"] == 0:
        result["racines"] = result["alpha"]
    else:
        result["racines"] = None
    return result
