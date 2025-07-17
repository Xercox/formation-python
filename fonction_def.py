# def ma_fonction():
#     print("Bonjours Georges")

# ma_fonction()

# def message(prenom):
#     print(f"Bonjour {prenom}")

# message("Leonardo")
# message("Tom")
# message("Angelina")

# def aire_cercle(rayon):
#     print("L'aire du cercles est:", 3.14 * rayon ** 2)

# aire_cercle(0.5)
# aire_cercle(10)

# def message(prenom, temperature):
#     print(f"Bonjour {prenom}")
#     print(f"La température est de {temperature}°C")
# message("Xercox", 35)                               # Bien respecter l'ordre 
# message(temperature = 23, prenom = "Miss-dixie")    # ou spécifier directement quand on se souvien pas de l'ordre 

# def salutation(prenom = "Tom"): # Assigne directement une valeur pour ne pas la redemander tous le temps
#     print("bonjours", prenom)

# def message(temperature, prenom = "tom"):
#     print(f"Bonjour {prenom}")
#     print(f"La température est de {temperature}°C")

# message(24, "Xercox") # ici Xercox a la priorité sur le prenom par default
# message(24)           # donnera le prenom par default et la température stipuler 

# def carre(nombre):
#     # print(f"Le carré de {nombre} est {nombre*nombre}")
#     return nombre*nombre
# resultat = carre(4)
# print(resultat)

def age_personne(age):
    if age >= 18:
        return f"{age} = Vous êtes majeure"
    else:
        return f"{age} = Vous êtes mineure"
resultat = age_personne(19)
print(resultat)