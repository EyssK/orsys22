"""
RepertoireGUI gère la partie graphique de RepertoirePerson grace à TKinter
"""
import tkinter as tk
from typing import Dict
from RepertoirePerson import RepertoirePerson
from Person import Person


class RepertoireGUI:
    """
    Gère l'affichage via TKinter
    """

    def __init__(self):
        self.repertoire = RepertoirePerson()
        self.window = tk.Tk()
        self.window.title("Répertoire")
        self.window.geometry("500x100")

        tk.Button(self.window,
                  text="Ajouter une personne",
                  command=self.cmd_ajouter).grid(row=0, column=0)
        tk.Button(self.window,
                  text="Chercher une personne",
                  command=self.cmd_chercher).grid(row=0, column=1)
        tk.Button(self.window,
                  text="Supprimer une personne",
                  command=self.cmd_supprimer).grid(row=0, column=2)
        tk.Button(self.window,
                  text="Quitter",
                  command=self.cmd_quit).grid(row=0, column=3)

    @staticmethod
    def quit_window(window):
        window.destroy()

    @staticmethod
    def clean_frame(frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def cmd_chercher(self):
        def search(repertoire: RepertoirePerson,
                   svres: tk.StringVar,
                   svregexp: tk.StringVar):
            svres.set("\n".
                      join([str(e)
                            for e in repertoire.regexp_chercher(svregexp.get())]))

        win = tk.Tk()
        sv_chercher_regexp = tk.StringVar(win)
        sv_chercher_res = tk.StringVar(win)
        tk.Message(win, textvariable=sv_chercher_res).grid(row=2, columnspan=2)
        tk.Label(win, text="Regexp").grid(row=0, column=0)
        tk.Entry(win, textvariable=sv_chercher_regexp).grid(row=0, column=1)
        tk.Button(
            win, text="Ok", command=lambda: search(
                self.repertoire, sv_chercher_res, sv_chercher_regexp)).grid(row=1, column=0)
        tk.Button(win, text="Quitter", command=lambda: self.quit_window(win)).grid(row=1, column=1)

    def cmd_ajouter(self):
        def update(
                repertoire: RepertoirePerson,
                _sv: Dict[str, tk.StringVar],
                window: tk.Tk):
            args = {"first_name": _sv["Prénom"].get(),
                    "last_name": _sv["Nom"].get()}
            mail = _sv["mail"].get()
            phone = _sv["tel"].get()
            if mail:
                args["email"] = mail
            if phone:
                args["phone"] = phone
            repertoire.ajouter(Person(**args))
            RepertoireGUI.quit_window(window)

        win = tk.Tk()
        sv_dict: Dict[str, tk.StringVar] = {"Prénom": tk.StringVar(win),
                                            "Nom": tk.StringVar(win),
                                            "mail": tk.StringVar(win),
                                            "tel": tk.StringVar(win)}
        tk.Label(win, text="Prénom").grid(row=1, column=0)
        tk.Entry(win, textvariable=sv_dict["Prénom"]).grid(row=1, column=1)
        tk.Label(win, text="Nom").grid(row=2, column=0)
        tk.Entry(win, textvariable=sv_dict["Nom"]).grid(row=2, column=1)
        tk.Label(win, text="mail").grid(row=3, column=0)
        tk.Entry(win, textvariable=sv_dict["mail"]).grid(row=3, column=1)
        tk.Label(win, text="tel").grid(row=4, column=0)
        tk.Entry(win, textvariable=sv_dict["tel"]).grid(row=4, column=1)
        tk.Button(
            win, text="Ok",
            command=lambda: update(self.repertoire, sv_dict, win)).grid(row=5, column=0)
        tk.Button(
            win, text="Annuler",
            command=lambda: self.quit_window(win)).grid(row=5, column=1)

    def cmd_supprimer(self):
        def remove(repertoire: RepertoirePerson, window: tk.Tk):
            person = Person(
                first_name=sv_supprimer_prenom.get(),
                last_name=sv_supprimer_nom.get())
            repertoire.supprimer(person)
            RepertoireGUI.quit_window(window)

        win = tk.Tk()
        sv_supprimer_prenom = tk.StringVar(win)
        sv_supprimer_nom = tk.StringVar(win)
        tk.Label(win, text="Prénom").grid(row=1, column=0)
        tk.Entry(win, textvariable=sv_supprimer_prenom).grid(row=1, column=1)
        tk.Label(win, text="Nom").grid(row=2, column=0)
        tk.Entry(win, textvariable=sv_supprimer_nom).grid(row=2, column=1)
        tk.Button(
            win, text="Ok", command=lambda: remove(self.repertoire, win)).grid(row=3, column=0)
        tk.Button(
            win, text="Annuler", command=lambda: self.quit_window(win)).grid(row=3, column=1)

    def cmd_quit(self):
        self.window.quit()
        self.repertoire.cmd_quit()

    def start(self):
        self.window.mainloop()


if __name__ == "__main__":
    r = RepertoireGUI()
    r.start()
