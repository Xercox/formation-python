## Exemple d'un dictionnaire de course.
# achats = {
#     "carottes": 5.4,
#     "lait": 2.5,
#     "oeuf": 3.4,
#     "oranges": 4.5
# }

# print(achats)

# personne = {"nom": "Dupont", "prenom": "Benois", "age": 30, "marie": False}
# departements = {1: "Ain", 62:"Pas-de-Calais", 45:"Loiret"}
# personne["age"] = 31      # Modifier des valeurs du dictionnaire
# 
# print(personne)
# print(personne["prenom"]) # Affiche la valeur de prenom

# print(departements)
# print(departements[62])   # Affiche la valeur de 62
##---------------------------------------------------------------------------

## Ajouter/supprimer des éléments de dictionnaire

achats = {
    "carottes": 5.4,
    "lait": 2.5,
    "oeuf": 3.4,
    "oranges": 4.5
}
print("oranges" in achats)     # Vérifie si oui ou non orange est dans le dictionnaire
print(achats)
del achats["oeuf"]             # Supprime une donnée du dictionnaire 
achats["bananes"] = 2.3       # Ajouter une donée à un dictionnaire
achats["fromage"] = 4.5
print(achats)