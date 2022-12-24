import blacklist

# Création d'un objet BlackList
blacklist = blacklist.BlackList()

def get_most_common_words(text, num_words):
    # split pour avoir les mots séparés du texte
    words = text.split()

    # Création d'un dictionnaire pour compter les mots
    counter = {}
    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1

    # Tri du dictionnaire par valeur 
    sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)

    # Initialisation de la liste des mots les plus fréquents dans le texte
    most_common_words = []

    # boucle for pour itérer sur les mots les plus fréquents
    for word, count in sorted_counter[:num_words]:
        # Vérification de l'existence du mots dans le module blacklist
        if word not in blacklist.bl:
            # Ajout du mot et son nombre d'occurrences à la liste des mots les plus fréquents
            most_common_words.append((word, count))

    # Renvoie de la liste des mots les plus fréquents
    return most_common_words

# Lecture du contenu du fichier
with open('texte.txt', 'r', encoding='utf8') as f:
    text = f.read()

# Afficher les 10 mots les plus fréquents
print(get_most_common_words(text, 10))

