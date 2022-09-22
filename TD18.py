"""
    # TD 18
Récupérez le fichier `human-proteome.fasta` qui contient le protéome humain, c'est-à-dire les séquences de l'ensemble
des protéines chez l'Homme. Ce fichier est au format FASTA.
On souhaite lister toutes ces protéines et les indexer avec un numéro croissant.
Créez un script liste_proteome.py qui :
- lit le fichier human-proteome.fasta
- extrait, avec une regex, de toutes les lignes de commentaires des séquences, le numéro d'accession de la protéine
- affiche le mot protein, suivi d'un numéro qui s'incrémente, suivi du numéro d'accession
Voici un exemple de sortie attendue :
```
protein 00001 O95139
protein 00002 O75438
protein 00003 Q8N4C6
[...]
protein 20371 Q8IZJ1
protein 20372 Q9UKP6
protein 20373 Q96HZ7
```
Conseils :
La ligne de commentaire d'une séquence au format FASTA est de la forme
`>sp|O95139|NDUB6_HUMAN NADH dehydrogenase [...]`
Elle débute toujours pas le caractère `>`.
Le numéro d'accession `O95139` se situe entre le premier et le second symbole `|` (symbole pipe).
Le numéro qui s'incrémente débutera à 1 et sera affiché sur 5 caractères avec
des 0 à sa gauche si nécessaires (formatage `{:05d}`).
"""
import re
import timeit
import sys


def re_readline():
    with open("human-proteome.fasta", 'r') as f:
        regex = re.compile(r"^>sp\|(.+)\|")
        increm = 1
        while True:
            l = f.readline().strip()
            if not l:
                break
            m = regex.search(l)
            if m:
                # print(f"protein {increm:05} {m.group(1)}")
                increm += 1

def re_read():
    with open("human-proteome.fasta", 'r') as f:
        regex = re.compile(r"^>sp\|(.+)\|", re.MULTILINE)
        increm = 1
        lines = f.read()
        m = regex.findall(lines)
        for e in m:
            # print(f"protein {increm:05} {e}")
            increm += 1

print("re_read", timeit.Timer('re_read()', setup="from __main__ import re_read").timeit(number=20), "seconds")
print("re_readline", timeit.Timer('re_readline()', setup="from __main__ import re_readline").timeit(number=20), "seconds")
