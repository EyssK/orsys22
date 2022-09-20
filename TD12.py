# TD 12

# Créez une `list` de mots. Utilisez `filter` pour ne garder que les mots contenant au moins un `r`

word_list = ["velo", "voiture", "maison", "radeau"]

filtered = filter(lambda x: 'r' in x, word_list)
e = list(filtered)
print(e)
