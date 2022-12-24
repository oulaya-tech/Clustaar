import re
class Extraction :
    def extract_article_info(html_file):
        # Lecture du contenu du fichier HTML
        with open(html_file, 'r', encoding = 'utf8') as f:
            html_content = f.read()

        # Initialiseation des variables pour stocker les informations de l'article
        title = ""
        content = ""
        links = []

        # Extraction du titre de l'article
        title_match = re.search(r'<title>(.*)</title>', html_content)
        if title_match:
            title = title_match.group(1)

        # Extraction du contenu de l'article
        content_match = re.search(r'<div class="content">(.+?)</div>', html_content, re.DOTALL)
        if content_match:
            content = content_match.group(1)

        # Extraction des liens de l'article
        links_matches = re.finditer(r'(http:.+?)>', html_content)
        for match in links_matches:
            links.append(match.group(1))

        # Renvoie des informations de l'article sous forme de dictionnaire
        return {
            'title': title,
            'content': content,
            'links': links
        }

    # Obtenir les informations de tous les fichiers HTML
    html_files = ['1.html', '2.html', '3.html', '4.html', '5.html']
    articles_info = []
    for html_file in html_files:
        articles_info.append(extract_article_info(html_file))

    # Affichage des informations de chaque article
    for article_info in articles_info:
        print(f'Titre: {article_info["title"]}')
        print(f'Contenu: {article_info["content"]}')
        print(f'Liens: {article_info["links"]}')
        print()

    # get title 
    def get_title(self):    
        return self.title
    # get content 
    def get_content(self):
        return self.content
    # get content
    def get_links(self):
        return self.links
     