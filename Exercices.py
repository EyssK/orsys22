from datetime import timedelta
from turtle import forward, left, pencolor, exitonclick
from math import pi
import random

testname = "Alphabet"


def exe1():
    print(testname)


def exe2():
    print("La valeur est", testname, "et il a", len(testname), "caractères")


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
    """
    Affiche la table de conversion euro/dollar
    :param change_rate: Taux de change
    :return: None
    """
    euro = 1
    while euro <= 16384:
        print(euro, "euro(s) =", euro * change_rate, "dollar(s)")
        euro = euro * 2


def exe7():
    """
    Cette fonction affiche le mot et compte le nombre de voyelles et consonnes
    :return: None
    """
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
    """
    Additionne les élèments d'une liste d'entiers
    :param liste_entiers:
    :return:
    """
    return sum(liste_entiers)


def exe9():
    """
    Retourne une liste d'entiers entrée par l'utilisateur
    :return: liste d'entier
    """
    return [int(e) for e in input("Entrez une liste de nombres ").split()]


def exe10():
    """
    Additionne les élèments d'une liste entrée par l'utilisateur
    :return: None
    """
    print(exe8(exe9()))


def exe11(sec):
    """
    Affiche la date en fonction du nombre de secondes
    :param sec: nombre de seconde
    :return: None
    """
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
    """
    Affiche le nombre de 'e' dans la string s
    :param s: string à vérifier
    :return: None
    """
    nb_e = 0
    for c in s:
        if c == 'e':
            nb_e += 1
    if nb_e:
        print("Il y a", nb_e, "'e' dans cette chaîne")
    else:
        print("Il n'y a pas de 'e' dans cette chaîne")


def exe13(liste):
    """
    Affiche l'élèment maximal de la liste
    :param liste: Liste d'élèment à comparer
    :return:
    """
    maxi = liste[0]
    for elem in liste:
        if elem > maxi:
            maxi = elem
    print(maxi, max(liste))


def exe14(liste):
    """
    Sépare la liste d'entier l en deux liste l_p et l_i contenant respectivement les éléments paires et impaires de l
    :param liste: Liste d'entier
    :return: None
    """
    l_p, l_i = list(), list()
    for e in liste:
        if est_pair(e):
            l_p.append(e)
        if not est_pair(e):
            l_i.append(e)
    print(liste, l_p, l_i)


def exe15():
    """
    FizzBuzz: somme les multiples de 3 et 5
    :return: None
    """
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
    """
    Dessine un carré de taille et couleur variable
    :param size_square: longeur du coté du carré
    :param color_square: couleur du carré
    :return:
    """
    pencolor(color_square)
    for i in range(4):
        forward(size_square)
        left(90)


def exe17(size_triangle, color_triangle):
    """
    # Dessine un triangle équilatéral de taille et couleur variable
    :param size_triangle: longeur du coté du triangle
    :param color_triangle: couleur du triangle
    :return:
    """
    pencolor(color_triangle)
    for i in range(3):
        forward(size_triangle)
        left(120)


def exe18():
    """
    invité de commande pour dessiner des carrés et des triangles
    :return: None
    """
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
    """
    affiche une pyramide de la hauteur spécifié par n
    :param n: profondeur de la pyramide
    :return: None
    """
    space = n - 1
    for i in range(n):
        print(' ' * space + "*" * (i * 2 + 1))
        space -= 1


def exe20(s):
    """
    check palindrome
    :param s: mot à vérifier
    :return: True si palindrome, False sinon
    """
    idx = 0
    while idx < len(s):
        if s[idx] != s[-idx - 1]:
            print("pas palindrome")
            return False
        idx += 1
    print("palindrome")
    return True


def exe21(r):
    """
    Calcule l'aire d'un cercle de rayon r
    :param r: rayon du cercle
    :return: aire du cercle
    """

    def aire_cercle(radius):
        return pi * radius ** 2

    aire = aire_cercle(r)
    print(f"{aire:.2f}")
    return aire


def exe22():
    """
    Trie la liste de tuple (CP, Ville) avec l'ordre alphabétique des villes
    """
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
    """
    jouer au pendu
    """
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
    # d = Domino(1, 6)
    # d.display_points()
    # print(d.value())
    #
    # d = Domino(0, 2)
    # try:
    #     d.display_points()
    #     print(d.value())
    # except AttributeError:
    #     pass
    #
    # d = Domino('titi', 'toto')
    # try:
    #     d.display_points()
    #     print(d.value())
    # except AttributeError:
    #     pass

    d1 = Domino(4, 3)
    d2 = Domino(6, 1)
    d1.display_points()
    d2.display_points()
    print("Total points :", d1.value() + d2.value())

    domino_list = []
    for i in range(7):
        domino_list.append(Domino(6, i))
    vt = 0
    for domino in domino_list:
        domino.display_points()
    vt = vt + domino.value()
    print('Total value : ', vt)


class Domino:
    def __new__(cls, a, b):
        print(f"NEW DOMINO: {a} {b}")
        try:
            int(a)
            int(b)
            if a > 6 or a < 0:
                raise ValueError
            if b > 6 or b < 0:
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


class CompteBancaire:
    def __init__(self, name, amount):
        self.name = str(name)
        self.amount = int(amount)

    def add(self, amount):
        # ajoute une somme au compte
        self.amount += amount

    def withdraw(self, amount):
        # retire une somme du compte
        if self.amount >= amount:
            self.amount -= amount

    def display(self):
        # affiche le solde du compte
        s = "s" * (self.amount > 0)
        print(f"Le compte {self.name} contient {self.amount} euro{s}")


def exe27():
    compte = CompteBancaire('Nicolas', 1000)
    compte.add(500)
    compte.display()
    compte.withdraw(100)
    compte.display()
    compte = CompteBancaire('Nicolas', 0)
    compte.display()


class Cercle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Cercle area")
        return pi * self.radius ** 2


class Cylindre(Cercle):
    def __init__(self, radius, height):
        self.height = height
        super().__init__(radius)

    def volume(self):
        print("Cylindre volume")
        return self.area() * self.height


class Cone(Cylindre):
    def volume(self):
        print("Cone volume")
        return 1 / 3 * super().volume()


def exe28():
    cone = Cone(1, 5)
    print(cone.volume())


class Carte:
    VALEURS = ("_", "_", "2", "3", "4", "5", "6", "7", "8", "9", "10", "valet", "dame", "roi", "as")
    COULEURS = ("pique", "trèfle", "carreau", "coeur")

    def __new__(cls, value: int, color: int):
        try:
            if value not in range(2, 15) or color not in range(0, 4):
                raise ValueError
        except ValueError:
            print("Exception at Carte __new__: bad value or color")
            raise ValueError
        else:
            return super().__new__(cls)

    def __init__(self, value, color):
        self.value = value
        self.color = color

    def __repr__(self):
        return f"{self.VALEURS[self.value]} de {self.COULEURS[self.color]}"


class JeuDeCartes:
    def __init__(self):
        jeu = list()
        for value in range(2, 15):
            for color in range(0, 4):
                jeu.append(Carte(value, color))
        self.jeu = jeu

    @staticmethod
    def nom_carte(carte: Carte):
        return carte.__repr__()

    def battre(self):
        random.shuffle(self.jeu)

    def tirer(self):
        if len(self.jeu) > 0:
            return self.jeu.pop()
        else:
            return None


def exe29():
    jeu = JeuDeCartes()
    jeu.battre()
    for n in range(53):
        c = jeu.tirer()
        print(JeuDeCartes.nom_carte(c))
    if c == None:
        print("Plus de carte !")
    else:
        print(jeu.nom_carte(c))


def exe31():
    joueur1 = JeuDeCartes()
    joueur2 = JeuDeCartes()
    joueur1.battre()
    joueur2.battre()
    score1, score2 = 0, 0

    print("Jouons à la bataille !")
    while True:
        c1 = joueur1.tirer()
        c2 = joueur2.tirer()
        if c1 is not None:
            if c1.value > c2.value:
                score1 += 1
                print(f"{c1} gagne contre {c2}")
            elif c1.value < c2.value:
                score2 += 1
                print(f"{c1} perd contre {c2}")
        else:
            break
    print(f"Joueur1: {score1}, Joueur2: {score2}")
    if score1 > score2:
        print("Joueur1 a gagné")
    elif score1 < score2:
        print("Joueur2 a gagné")
    else:
        print("Egalité")


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
    # exe26()
    # exe27()
    # exe29()
    exe31()
    pass


if __name__ == '__main__':
    main()
