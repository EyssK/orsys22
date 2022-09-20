def exe_1():
    name = "Kevin"
    print(name)


def exe_2():
    guest = input("Renseignez votre nom : ")
    guest = guest.title()
    print(f"Bonjour {guest}")


def exe_3():
    table = ["NiCOlas", "ThoMas", "ReNé", "N'guyen"]
    guest = input("Renseignez votre nom : ").title()
    if guest.casefold() in [e.casefold() for e in table]:
        print(f"Bonjour {guest}")
    else:
        print(f"Vous n'êtes pas dans la liste")


def exe_4():
    name_list = []
    while True:
        name = input("Entrez un nom : ")
        if not name:
            print([n for n in name_list])
            break
        else:
            name_list.append(name)


def exe_5():
    name_list = ["zoo", "maman", "bonbon", "titi", "vélo", "toto", "tutu"]
    letter = input("Entrez une lettre : ")
    print([name for name in name_list if letter.casefold() == name[0].casefold()])
    print(list(filter(lambda x: letter.casefold() == x[0].casefold(), name_list)))


def exe_6():
    name_list = {}
    while True:
        name = input("Entrez un nom : ").casefold()
        if not name:
            while True:
                letter = input("Entrez une lettre : ").casefold()
                if not letter:
                    break
                else:
                    if letter in name_list:
                        print(name_list[letter])
                    else:
                        print(f"Pas de nom commencant par {letter}")
            break
        else:
            if name[0] in name_list:
                name_list[name[0]].append(name)
            else:
                name_list[name[0]] = [name]


class Repertoire:
    def __init__(self):
        self.liste_nom = list()
        self.cmd_list = {
            'a': self.ajouter,
            's': self.chercher,
            'd': self.supprimer,
            'l': self.afficher_lettre,
            'q': exit
        }

    @staticmethod
    def get_name():
        # return a name from input
        nom = input("Nom : ")
        return nom

    @staticmethod
    def get_letter():
        nom = input("Lettre : ")
        return nom

    def ajouter(self):
        nom = self.get_name()
        if nom not in self.liste_nom:
            self.liste_nom.append(nom)

    def chercher(self):
        nom = self.get_name()
        if nom in self.liste_nom:
            print(nom)
        else:
            print("Nom inconnue")

    def supprimer(self):
        nom = self.get_name()
        try:
            self.liste_nom.remove(nom)
        except KeyError:
            print("Nom inconnue")

    def afficher_lettre(self):
        lettre = self.get_letter()
        found = []
        for nom in self.liste_nom:
            if lettre.casefold() == nom[0].casefold():
                found.append(nom)
        print(found)

    def start(self):
        while True:
            cmd = input("Commande : ")
            try:
                self.cmd_list[cmd]()
            except KeyError:
                print("Commande inconnue")


def exe_7():
    a = Repertoire()
    a.start()


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._age = -1

    def __str__(self):
        return f"Nom: {self.last_name}\nPrénom: {self.first_name}"

    def set_age(self, age):
        if age in range(0, 110):
            self._age = age

    def get_age(self):
        return self._age

    def __eq__(self, other):
        if self.first_name == other.first_name and self.last_name == other.last_name:
            return True
        else:
            return False

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


def exe_8():
    a = Person("Jean", "Dupont")
    b = Person("Jean", "Dupont")
    a.set_age(10)
    print(a.get_age())
    print(a)
    print(hex(id(a)))
    print(hex(id(b)))
    print(a == b)
    print(a.full_name())


class Child(Person):
    def set_age(self, age):
        if age in range(0, 18):
            self._age = age


def exe_9():
    a = Child("leo", "titi")
    b = Child("leo", "titi")
    a.set_age(4)
    a.set_age(21)
    print(a.get_age())
    print(a == b)


class RepertoirePerson(Repertoire):
    # Cette classe permet de gérer des Répertoires de personnes. Elle hérite de la classe Répertoire
    def __init__(self):
        print("Init RepertoirePerson")
        super().__init__()

    def afficher_lettre(self):
        lettre = self.get_letter()
        found = []
        for (person, name) in [(person, person.last_name) for person in self.liste_nom]:
            if lettre.casefold() == name[0].casefold():
                found.append(person)
        [print(e.full_name()) for e in found]

    @staticmethod
    def get_name():
        # return a Person from input
        nom = str(input("Nom : "))
        prenom = str(input("Prénom : "))
        p = Person(prenom, nom)
        return p


def exe_10():
    a = RepertoirePerson()
    a.start()


if __name__ == "__main__":
    exe_10()
