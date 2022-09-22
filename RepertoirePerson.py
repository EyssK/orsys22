from Person import Person
import re
import pickle


class RepertoirePerson:
    PATH = "repertoire.save"

    # Cette classe permet de gérer des Répertoires de personnes
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

    @staticmethod
    def get_letter():
        nom = input("Lettre : ")
        return nom

    @staticmethod
    def get_name():
        """
        return a Person from input
        :return: a person
        """
        nom = str(input("Nom : "))
        prenom = str(input("Prénom : "))
        p = Person(prenom, nom)
        return p

    @staticmethod
    def get_regexp():
        """
        return a regexp from input
        :return: a regexp
        """
        nom = str(input("Regexp : "))
        return nom

    def ajouter(self, personne):
        """
        ajoute une Person dans le répertoire
        :param personne: la personne à ajouter
        :return: None
        """
        if not personne.last_name:
            print("Ajout refusé: Nom vide")
            return
        if not personne.first_name:
            print("Ajout refusé: Prénom vide")
            return
        if personne not in self.liste_nom:
            self.liste_nom.append(personne)

    def regexp_chercher(self, regexp):
        """
        Chercher la regexp dans les noms et prénoms dans le répertoire
        :param regexp: regexp
        :return: liste des personnes correspondantes
        """
        found = []
        for person in [person for person in self.liste_nom]:
            if re.findall(regexp, person.last_name, re.IGNORECASE) or re.findall(regexp, person.first_name,
                                                                                 re.IGNORECASE):
                found.append(person)
        return found

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
        self.ajouter(nom)

    def cmd_supprimer(self, *args):
        """
        Supprimer
        """
        nom = self.get_name()
        self.supprimer(nom)

    def supprimer(self, person):
        try:
            self.liste_nom.remove(person)
        except ValueError:
            print(f"{person} est inconnue")

    def cmd_chercher(self, *args):
        """
        Chercher
        """
        reg = self.get_regexp()
        found = self.regexp_chercher(reg)
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
