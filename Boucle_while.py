# La boucle while fonctionne de la manière suivante :

# On crée une variable nommée 'tour' qui servira de compteur.
tour = 0

# On utilise une boucle while avec la condition : tant que 'tour' est inférieur ou égal à 7, le code à l'intérieur de la boucle s'exécutera.
while tour <= 7:
    # À chaque itération de la boucle, on affiche un message avec la valeur actuelle de 'tour'.
    print("Dans la boucle", tour)
    
    # On incrémente la variable 'tour' pour éviter une boucle infinie.
    tour += 1
