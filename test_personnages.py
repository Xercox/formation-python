class Personnage:
    def __init__(self, nom, classe, niveau=1):
        self.nom = nom
        self.classe = classe
        self.niveau = niveau
        self.points_de_vie_max = 100 #Valeur de vie de base
        self.points_de_vie = self.points_de_vie_max
        self.points_de_mana_max = 100 #Valeur de mana de base
        self.points_de_mana = self.points_de_mana_max
        self.experience = 0
        self.inventaire = []

    def afficher_infos(self):
        print(f"{self.nom} - Niveau {self.niveau}")
        print(f"Classe : {self.classe}")
        print(f"Points de vie : {self.points_de_vie}/{self.points_de_vie_max}")
        print(f"Points de mana : {self.points_de_mana}/{self.points_de_mana_max}")


guerrier = Personnage("Maverick", "Combattant")
mage = Personnage("Gandalf", "Magicien")

mage.afficher_infos()
guerrier.afficher_infos()