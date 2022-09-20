# Exception
# Créez un script qui demande à l'utilisateur de rentrer un nombre.
# Grâce à la gestion d'exception, affichez à l'utilisateur s'il a entré un nombre ou pas.

while True:
    n = input("Entrez un nombre ")
    try:
        number = float(n)
    except:
        print("Ce n'est pas un nombre !")
    else:
        print(f"Votre nombre est {number}")
        break