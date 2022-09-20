""" Créez un script qui demande à l'utilisateur son nom et qui lui affiche le nombre de caractères dont il est composé,
le carré de ce nombre et la racine carrée."""

from math import sqrt

user_name = input("Quel est votre nom ? ")
L = len(user_name)
print(L, L**2, sqrt(L))