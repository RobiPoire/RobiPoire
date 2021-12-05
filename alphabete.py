"""
Alphabete
~~~~~~~~~~~~~~~~~~~
De son voyage sur Terre, le Professeur Zorglub a ramené sur sa planète une découverte extraordinaire : 
l'ordre alphabétique. Finies les fastidieuses recherches séquentielles dans le dictionnaire ! 
Il ne reste plus qu'un problème :classer effectivement le dictionnaire dans l'ordre lexicographique ... 
et c'est votre mission, si vous l'acceptez !

Example :
>>> 4
>>> 10
>>> 3
>>> t%('
>>> %(%(
>>> '''ttt
>>> ttt
ttt
%(%(
ttt

"""

__title__ = "Alphabete"
__author__ = "Robin"


def alphabet_creation(number_letter_alphabet, maximum_word_length, number_words_dictionary, alphabet):
    while len(alphabet) != number_letter_alphabet:
        print(f"L'alaphabet doit comporter {number_letter_alphabet} lettres !")
        alphabet = input("L'alphabet (dans l'ordre): ")
    alphabet = list(alphabet.strip())
    words = []
    for i in range(number_words_dictionary):
        conf1, conf2 = False, False
        while conf1 == False or conf2 == False:
            conf1, conf2 = True, True
            word = input(f"Mot N°{i+1}: ")
            for j in list(word.strip()):
                if j not in alphabet and conf1 == True:
                    print(
                        f"La lettre \"{j}\" n'est pas dans l'alphabet, veuilliez re-essayer.")
                    conf1 = False
            if len(word) > maximum_word_length:
                print(
                    f"Mot trop grand ! La longueur maximal est de \"{maximum_word_length}\" lettres.")
                conf2 = False
        words.append(word)
    return words


if __name__ == "__main__":
    number_letter_alphabet = int(input("Le nombre de lettres de l'alphabet: "))
    maximum_word_length = int(
        input("La longueur maximale des mots du dictionnaire: "))
    number_words_dictionary = int(input("Le nombre de mots du dictionnaire: "))
    alphabet = input("L'alphabet (dans l'ordre): ")
    words = alphabet_creation(
        number_letter_alphabet, maximum_word_length, number_words_dictionary, alphabet)
    words = sorted(words, key=lambda word: [alphabet.index(i) for i in word])
    for i in words:
        print(i)
