import re
import pickle

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
        self.restore()
        self.cmd_list = {
            'a': self.cmd_ajouter,
            's': self.cmd_chercher,
            'd': self.cmd_supprimer,
            'l': self.afficher_lettre,
            'h': lambda : [print(keys, values) for keys, values in self.cmd_list.items()],
            'q': self.quit,
        }

    def get_name(self):
        # return a name from input
        nom = input("Nom : ")
        return nom

    def get_letter(self):
        nom = input("Lettre : ")
        return nom

    def __ajouter(self, personne):
        if personne not in self.liste_nom:
            self.liste_nom.append(personne)

    def cmd_ajouter(self):
        nom = self.get_name()
        self.__ajouter(nom)

    def cmd_chercher(self):
        nom = self.get_name()
        if nom in self.liste_nom:
            print(nom)
        else:
            print("Nom inconnue")

    def cmd_supprimer(self):
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

    def quit(self):
        self.save()
        exit()

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
    def __init__(self, first_name, last_name, email="a@a.fr", phone="0123456789"):
        self.first_name = first_name
        self.last_name = last_name
        self._age = -1
        if re.findall(r"^[-\w\.]+@([\w-]+\.)+[\w-]{2,4}$",email):
            self.email = email
        else:
            print(f"Mauvais email {email}")
            self.email = "a@a.fr"
        if re.findall(r"^(?:(?:\+|00)33[\s.-]{0,3}(?:\(0\)[\s.-]{0,3})?|0)[1-9](?:(?:[\s.-]?\d{2}){4}|\d{2}(?:[\s.-]?\d{3}){2})$", phone):
            self.phone = phone
        else:
            print(f"Mauvais numéro de téléphone {phone}")
            self.phone = "0123456789"


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


class RepertoirePerson():
    PATH="repertoire.save"
    # Cette classe permet de gérer des Répertoires de personnes. Elle hérite de la classe Répertoire
    def __init__(self):
        print("Init RepertoirePerson")
        self.liste_nom = list()
        self.restore()
        self.cmd_list = {
            'a': self.cmd_ajouter,
            's': self.cmd_chercher,
            'd': self.cmd_supprimer,
            'l': self.cmd_afficher_lettre,
            'h': self.cmd_help,
            'q': self.cmd_quit,
        }

    def get_letter(self):
        nom = input("Lettre : ")
        return nom

    def get_name(self):
        """
        return a Person from input
        :return: a person
        """
        nom = str(input("Nom : "))
        prenom = str(input("Prénom : "))
        p = Person(prenom, nom)
        return p

    def __ajouter(self, personne):
        """
        ajoute une personne dans le répertoire
        :param personne: la personne à ajouter
        :return: None
        """
        if personne not in self.liste_nom:
            self.liste_nom.append(personne)



    def __regexp_chercher(self, regexp):
        """
        Chercher la regexp dans les noms et prénoms dans le répertoire
        :param regexp: regexp
        :return: liste des personnes correspondantes
        """
        found = []
        for person in [person for person in self.liste_nom]:
            if re.findall(regexp, person.last_name) or re.findall(regexp, person.first_name):
                found.append(person)
        return found

    def get_regexp(self):
        nom = str(input("Regexp : "))
        return nom

    def save(self):
        print(f"Saving to {self.PATH}")
        with open(self.PATH, 'wb') as f:
            pickle.dump(self.liste_nom, f)
            # for person in self.liste_nom:
            #     f.write(f"{person.first_name}; {person.last_name}; {person.get_age()}; {person.email}; {person.phone}\n")

    def restore(self):
        try:
            with open(self.PATH, 'rb') as f:
                print(f"Restoring from {self.PATH}")
                self.liste_nom = pickle.load(f)
        except FileNotFoundError:
            # no save file found
            pass
            # lines = f.readlines()
            # for p_list in [e.split(";") for e in lines]:
            #     p_list = [e.strip() for e in p_list]
            #     person = Person(p_list[0], p_list[1], p_list[3], p_list[4])
            #     person.set_age(p_list[2])
            #     self.__ajouter(person)

    def start(self):
        """
        Démarre l'invité de commandes
        :return:
        """
        while True:
            cmd = input("Commande : ").split(" ")
            cmd = [e.strip() for e in cmd]
            try:
                self.cmd_list[cmd[0]](cmd[1:])
            except KeyError:
                print("Commande inconnue")

    def cmd_ajouter(self, *args):
        """
        Ajouter - Cette commande permet d'ajouter une personne au répertoire
        """
        nom = self.get_name()
        self.__ajouter(nom)

    def cmd_supprimer(self, *args):
        """
        Supprimer
        """
        nom = self.get_name()
        try:
            self.liste_nom.remove(nom)
        except KeyError:
            print("Nom inconnue")

    def cmd_chercher(self, *args):
        """
        Chercher
        """
        reg = self.get_regexp()
        found = self.__regexp_chercher(reg)
        if found:
            [print(e.full_name()) for e in found]
        else:
            print("Rien trouvé")

    def cmd_afficher_lettre(self, *args):
        """
        Afficher lettre
        """
        lettre = self.get_letter()
        found = []
        for person in self.liste_nom:
            if person.last_name[0].casefold() == lettre.casefold():
                found.append(person)
        [print(e.full_name()) for e in found]

    def cmd_help(self, *args):
        """
        Help
        """
        [print(keys, values.__doc__.strip()) for keys, values in self.cmd_list.items()]

    def cmd_quit(self, *args):
        """
        Quit
        """
        self.save()
        exit()

def exe_10():
    a = RepertoirePerson()
    a.start()


def exe_11():
    p = Person("John", "Wayne", "abc@te.com", "0123.456789")
    print(p)
    p = Person("Toto", "Titi", "c@-.--m", "+33265.89.09.12")
    print(p)

if __name__ == "__main__":
    exe_11()
