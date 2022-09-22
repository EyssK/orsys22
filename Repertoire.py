class Repertoire:
    def __init__(self):
        self.liste_nom = list()
        self.cmd_list = {
            'a': self.cmd_ajouter,
            's': self.cmd_chercher,
            'd': self.cmd_supprimer,
            'l': self.afficher_lettre,
            'h': lambda: [print(keys, values) for keys, values in self.cmd_list.items()],
            'q': self.quit,
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

    @staticmethod
    def quit():
        exit()

    def start(self):
        while True:
            cmd = input("Commande : ")
            try:
                self.cmd_list[cmd]()
            except KeyError:
                print("Commande inconnue")
