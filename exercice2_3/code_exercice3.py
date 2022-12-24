import os
import json

from code_exercice2 import Extraction

class HTMLPage:
    # initialisatoon de HTMLPage 
    def __init__(self, title, content, links):
        self.title = Extraction.get_title(title)
        self.content = Extraction.get_content(content)
        self.links = Extraction.get_links(links)
    # Initialisation de la méthode to_json
    def to_json(self):
        return {
            'title': self.title,
            'content': self.content,
            'links': self.links
        }

# Création d'une instance de la classe HTMLPage
page = HTMLPage(self.title, self.content, self.links)

# Conversion des informations de la page en format JSON
page_json = page.to_json()
print(page_json)  

# Extraction des infos de tous les fichiers HTML de la liste
html_file = ['1.html', '2.html', '3.html', '4.html', '5.html']
pages = Extraction.extract_article_info(html_file)

# Création d'un fichier d'index inverted vide
inverted_index = {}

# Pour chaque page, enregistrer les informations dans un fichier JSON
# et ajouter les tokens de la page à l'index inversé
for i, page in enumerate(pages):
    # Convertioon des informations de la page en format JSON
    page_json = page.to_json()

    # Enregistrementt ses informations de la page dans un fichier JSON
    with open(f'page{i}.json', 'w') as f:
        f.write(json.dumps(page_json))

    # Pour chaque token de la page, ajouter la page à l'index inversé
    for token in page.tokens:
        if token in inverted_index:
            inverted_index[token].append(i)
        else:
            inverted_index[token] = [i]

# Enregistrer l'index inversé dans un fichier JSON
with open('inverted_index.json', 'w', encoding='utf8') as f:
    f.write(json.dumps(inverted_index))
