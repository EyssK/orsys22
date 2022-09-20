'''
TD 10

_La fontion `count()` du type `str` permet de compter le nombre d'occurrences d'une lettre_

Créez une variable et assignez-lui une suite aléatoire de lettre.
Créez une fonction qui prend en paramètre une chaîne de caractère et qui retourne un dictionnaire
dont les clefs sont les différentes lettres présentes et en valeur le nombre d'occurrences.
Affichez le résultat.
'''

var ="azlmehazmfhvuâfgvé!"

def count_dict(s):
    d = dict()
    for l in s:
        # print(l, s.count(l))
        if l not in d:
            d[l] = s.count(l)
    return d

print(count_dict(var))
print({char: var.count(char) for char in var})