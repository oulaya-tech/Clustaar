class BlackList:
    """
    Instruction:
        Il est autorisé de modifier le comportement de cette classe, sauf le nom des attributs
    """

    def __init__(self) -> None:
        """
        Initialise un set de mots à exclure.
        """
        self.bl = set()
        self.words = ""  # TODO load words.txt
        self._make_bl()

    # Charger le contenu du fichier words.txt dans self.words
        with open('words.txt', 'r', encoding= 'utf8') as f:
            self.words = f.read()

    def _make_bl(self) -> None:
        """
        Strip les mots et les ajoute dans l'attribut bl
        """
        words = self.words.split("\n")

        for w in words:
            w = w.strip()

            self.bl.add(w)