from datetime import timedelta
from turtle import forward, left, pencolor, exitonclick
from math import pi

name = "Alphabet"


def exe1():
    print(name)


def exe2():
    print("La valeur est", name, "et il a", len(name), "caractères")


def exe3():
    name1 = input("Insérez votre nom :")
    if name1:
        print("Bonjour", name1.title())
    else:
        print("Bonjour vous!")


def est_pair(a):
    if a % 2 == 0:
        return True
    else:
        return False


def exe4():
    # Indique si le nombre entré par l'utilisateur est paire ou impaire
    number = input("Entrez un nombre ")
    if est_pair(number):
        print(number, "est pair")
    else:
        print(number, "est impair")


def exe5():
    # Affiche la table de 9 et marque une flèche sur les valeurs paires
    for idx in range(20):
        res = idx * 9
        i = est_pair(res)
        print(res, '<-' * i)


def exe6(change_rate=1.14):
    # Affiche la table de conversion euro/dollar
    euro = 1
    while euro <= 16384:
        print(euro, "euro(s) =", euro * change_rate, "dollar(s)")
        euro = euro * 2


def exe7():
    # Cette fonction affiche le mot et compte le nombre de voyelles et consonnes
    mot = input("Entrez un mot ")
    voyelles = 'aeiouy'
    voy, con = 0, 0
    for c in mot:
        print(c)
        if c in voyelles:
            voy += 1
        else:
            con += 1
    print("Le mot contient", voy, "voyelles et", con, "consonnes")


def exe8(liste_entiers):
    # Additionne les élèments d'une liste d'entiers
    return sum(liste_entiers)


def exe9():
    # Additionne les élèments d'une liste entrée par l'utilisateur
    return [int(e) for e in input("Entrez une liste de nombres ").split()]


def exe10():
    print(exe8(exe9()))


def exe11(sec):
    y_in_sec = 365 * 24 * 60 * 60  # non bisextile
    # m_in_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # m_in_sec = [ e * 24 * 60 * 60 for e in m_in_day]
    # for m_idx in m_in_sec:
    #    m
    m_in_sec = 30 * 24 * 60 * 60  # month = 30 jours
    d_in_sec = 24 * 60 * 60
    h_in_sec = 60 * 60
    y = sec // y_in_sec
    sec = sec % y_in_sec
    m = sec // m_in_sec
    sec = sec % m_in_sec
    d = sec // d_in_sec
    sec = sec % d_in_sec
    h = sec // h_in_sec
    sec = sec % h_in_sec
    minute = sec // 60
    s = sec % 60
    print(timedelta(seconds=sec))
    print(y, "year", m, "month", d, "days", str(h) + ':' + str(minute) + ':' + str(s))


def exe12(s):
    # Affiche le nombre de 'e' dans la string s
    nb_e = 0
    for c in s:
        if c == 'e':
            nb_e += 1
    if nb_e:
        print("Il y a", nb_e, "'e' dans cette chaîne")
    else:
        print("Il n'y a pas de 'e' dans cette chaîne")


def exe13(liste):
    # Affiche l'élèment maximal de la liste
    maxi = liste[0]
    for elem in liste:
        if elem > maxi:
            maxi = elem
    print(maxi, max(liste))


def exe14(liste):
    # Sépare la liste d'entier l en deux liste l_p et l_i contenant respectivement les éléments paires et impaires de l
    l_p, l_i = list(), list()
    for e in liste:
        if est_pair(e):
            l_p.append(e)
        if not est_pair(e):
            l_i.append(e)
    print(liste, l_p, l_i)


def exe15():
    inf = int(input("Entrez la borne inférieur "))
    sup = int(input("Entrez la borne supérieur "))
    multiple_3et5 = 0
    multiple_3ou5 = 0
    for i in range(inf, sup):
        if not i % 3 and not i % 5:
            multiple_3et5 += i
        if not i % 3 or not i % 5:
            multiple_3ou5 += i
    print("Somme des multiples de 3 et 5", multiple_3et5)
    print("Somme des multiples de 3 ou 5", multiple_3ou5)


def exe16(size_square, color_square):
    # Dessine un carré de taille et couleur variable

    pencolor(color_square)
    for i in range(4):
        forward(size_square)
        left(90)


def exe17(size_triangle, color_triangle):
    # Dessine un triangle équilatéral de taille et couleur variable

    pencolor(color_triangle)
    for i in range(3):
        forward(size_triangle)
        left(120)


def exe18():
    # invité de commande pour dessiner des carrés et des triangles
    print("Carré : 1")
    print("Triangle : 2")
    while True:
        draw = input("Que voulez vous dessinez ? forme taille couleur ").split()
        if not draw:
            return
        if draw[0] == '1':
            exe16(int(draw[1]), draw[2])
        elif draw[0] == '2':
            exe17(int(draw[1]), draw[2])
        else:
            print("Forme inconnue")
            break


def exe19(n):
    # affiche une pyramide de la hauteur spécifié par n
    space = n - 1
    for i in range(n):
        print(' ' * space + "*" * (i * 2 + 1))
        space -= 1


def exe20(s):
    # check palyndrome
    idx = 0
    while idx < len(s):
        if s[idx] != s[-idx - 1]:
            print("pas palyndrome")
            return False
        idx += 1
    print("palyndrome")
    return True


def exe21(r):
    # Calcule l'aire d'un cercle de rayon r
    def aire_cercle(radius):
        return pi * radius ** 2

    aire = aire_cercle(r)
    print(f"{aire:.2f}")
    return aire


def exe22():
    # Trie la liste de tuple (CP, Ville) avec l'ordre alphabétique des villes
    liste = [("83000", "Toulon"), ("06000", "Nice"), ("29200", "Brest"), ("59000", "Lille")]
    print(sorted(liste, key=lambda a: a[1]))


def exe23():
    liste = ["23", "12", "89", "21"]
    print(liste)
    print([e for e in map(lambda a: int(a), liste)])
    print([int(e) for e in liste])


def exe24():
    def fibonacci_generator():
        a, b = 1, 1
        while True:
            yield a
            a, b = b, a + b

    my_iterator = fibonacci_generator()
    for i in range(10):
        print(next(my_iterator))


def exe25():
    # jouer au pendu
    mot_a_deviner = list("baba")
    reste_a_trouve = list(mot_a_deviner)
    mot_trouve = ["_"] * len(mot_a_deviner)
    vie = 3
    while True:
        lettre = input(f"{mot_trouve} {vie} vies\nProposez une lettre : ")
        if lettre not in reste_a_trouve:
            vie -= 1
        while lettre in reste_a_trouve:
            idx = reste_a_trouve.index(lettre)
            mot_trouve[idx] = lettre
            reste_a_trouve[idx] = '*'
        if mot_a_deviner == mot_trouve:
            print("Gagné !")
            break
        if vie == 0:
            print("Perdu !")
            break


def exe26():
    d = Domino(1, 6)
    d.display_points()
    print(d.value())

    d = Domino(0, 2)
    try:
        d.display_points()
        print(d.value())
    except AttributeError:
        pass

    d = Domino('titi', 'toto')
    try:
        d.display_points()
        print(d.value())
    except AttributeError:
        pass


class Domino:
    def __new__(cls, a, b):
        print(f"NEW DOMINO: {a} {b}")
        try:
            int(a)
            int(b)
            if a > 6 or a < 1:
                raise ValueError
            if b > 6 or b < 1:
                raise ValueError
        except ValueError:
            print("Exception at Domino init:  must be integers between 1 and 6")
        else:
            return super(Domino, cls).__new__(cls)

    def __init__(self, a, b):
        self.A = int(a)
        self.B = int(b)

    def display_points(self):
        print(f"A: {self.A}\tB:{self.B}")

    def value(self):
        return self.A + self.B


def exe27():
    pass


def main():
    # exe7()
    # print(exe8([1,2,3,4]))
    # print(exe9())
    # exe11(1234567899)
    # exe12("toto est très content")
    # exe13([1,2,3,4,1,2])
    # exe14([1, 2, 3, 4, 1, 2])
    #
    # exe15()
    #
    # exe16(100,'red')
    # exe17(100, 'blue')
    # exe18()
    # exitonclick()
    #
    # exe19(8)
    # exe20("abcecba")
    # exe21(5)
    # exe22()
    # exe23()
    #
    # exe24()
    # exe25()

    pass


if __name__ == '__main__':
    main()
