"""
    # TD 17
Créez un script qui prend des arguments en ligne de commande :
- Path pour un fichier d'entrée
- Path pour un fichier de sortie
- Méthode : ajout ou remplace
Le script copie le contenu du fichier d'entrée dans celui de sortie.
"""
import getopt
import sys

short_options = "o:i:"
long_options = ["out=", "in="]

args, val = getopt.getopt(sys.argv[1:], short_options, long_options)

for arg, val in args:
    if arg in ("-o", "--out"):
        out_file = val
    elif arg in ("-i", "--in"):
        in_file = val

print(f"copying {in_file} into {out_file}")

with open(in_file, 'r', encoding="Latin1") as inf:
    with open(out_file, 'w', encoding="Latin1") as of:
        for line in inf.readlines():
            of.write(line)



