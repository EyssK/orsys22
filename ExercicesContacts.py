from Repertoire import Repertoire
from Person import Person
from RepertoirePerson import RepertoirePerson
from RepertoireGUI import RepertoireGUI


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


def exe_7():
    a = Repertoire()
    a.start()


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


def exe_10():
    a = RepertoirePerson()
    a.start()


def exe_11():
    p = Person("John", "Wayne", "abc@te.com", "0123.456789")
    print(p)
    p = Person("Toto", "Titi", "c@-.--m", "+33265.89.09.12")
    print(p)


def exe_12():
    r = RepertoireGUI()
    r.start()


if __name__ == "__main__":
    exe_12()
