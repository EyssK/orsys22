# TD 9
# f-strings
# Créez une variable avec une `list` de nombre. Parcourez tous les nombres grâce à une boucle `for` et affichez leur racine carrée avec 1 seul chiffre après la virgule.

from math import sqrt

var = [1,180,5,19,2]

for e in var:
    print(f'sqrt avec 1 seul chiffre après la virgule sqrt({e}) = {sqrt(e):.1f}')
    print("😀", '\U0001f604', '\N{grinning face with smiling eyes}')
