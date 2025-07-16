# Les listes python
# Une liste est comme un conteneur ou on peut y stocket ce qu'on veut.

villes = ["Paris", "New York", "Londre"] 

# Affiche l'index 0 (Paris)
print(villes[0])

# Assigner l'index d'un ligne à une variable
ville_1 = villes[1] 
print(ville_1) # Affiche (New York)

# Remplacer un index
villes[1] = "Bordeaux" # remplace (New York) par (Bordeaux)
print(villes)

# Tranchage (Récuperer plusieurs index) 
print(villes[0:2]) # Affichera (Paris)(New York) lis a partir de l'index 0 jusque l'index 2 sans le compter dedans

# Ajouter un élément a une liste
villes.append("Lyon") # ajoute +1 a l'index et ajoute la ville dans la liste

# Ajouter une liste dans une liste
villes = villes + ["Marseille", "Lyon"] # ou le nom d'une autre liste

# Pour supprimer une valeur d'une liste 
villes.remove("New York") # enlève (New York) de la liste
#  Ou 
del villes[1] # ferra la même chose
#-------------------------------------------------------------------------------------------------------------------
# L'opérateur d'appartenance: in 

villes = ["Paris", "New York", "Londres"]

ville = "Bordeaux"
if ville in villes: # Si ville est dans villes
    print(f"{ville} fait déjà partie de notre liste")
else: # Sinon ajoute ville à villes
    villes.append(ville)
    print(f"{ville} fait désormais partie de notre liste")
print(villes)
#-------------------------------------------------------------------------------------------------------------------
# Boucle for & listes
for i in [0,1,2,3,4,5,6]:
    print("Dans la boucle", i)

for v in ["Lisbonne", "Londre", "Paris", "Rome"]:
    print(v.upper())