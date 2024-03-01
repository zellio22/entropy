# Remplacez 'chemin/vers/le/fichier' par le chemin réel de votre fichier binaire
chemin_fichier = './test.txt'

# Ouverture du fichier en mode binaire
with open(chemin_fichier, 'rb') as fichier:
    # Lecture de l'octet initial
    print(fichier.tell())
    fichier.seek(0,2)
    octet = fichier.read(1)
    
    while octet:
        # Affichage de la valeur de l'octet
        print(f"Valeur de l'octet : {ord(octet)}")
        # Lecture de l'octet suivant
        octet = fichier.read(1)


