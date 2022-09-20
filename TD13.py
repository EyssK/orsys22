# TD 13
# Iterateurs / générateurs
# Créez le générateur de nombres aléatoires entre 0 et 100.

from random import randrange


def rand_gen_1_100(n):
    for i in range(n):
        yield randrange(0, 100)


print([a for a in rand_gen_1_100(10)])
