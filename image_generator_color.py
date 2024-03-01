from PIL import Image
import random

# Dimensions de l'image
largeur = 2048
nom_fichier="./global.ini.tar.gz"

with open(nom_fichier, 'rb') as fichier:
    # Lecture du contenu ou d'autres opérations sur le fichier si nécessaire
    contenu = fichier.read()
    taille_fichier = fichier.tell()
    print(taille_fichier)
    print(len(contenu))

image = Image.new("RGB", (largeur,8152), "white")
y=0
x=0
for i in range(len(contenu)):
    x=x+3

    if x+3>=largeur:
        y=y+1
        x=0

    couleur=(contenu[x-3],contenu[x-2],contenu[x-1])
    #print(x,y,couleur)
    image.putpixel((x, y), couleur)
    #print(couleur)
    


# Enregistrement de l'image
image.save("image_random.png")

# Affichage de l'image (optionnel)

