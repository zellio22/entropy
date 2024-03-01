from PIL import Image
import random

# Dimensions de l'image
largeur = 2048
nom_fichier="./global.ini"

with open(nom_fichier, 'rb') as fichier:
    # Lecture du contenu ou d'autres opérations sur le fichier si nécessaire
    contenu = fichier.read()
    taille_fichier = fichier.tell()
    print(taille_fichier)
    print(len(contenu))

image = Image.new("RGB", (largeur,int(taille_fichier/3/largeur)+1), "white")
y=0
x=0
for i in range(0,len(contenu),3):
    x=x+1

    if x%largeur==0:
        y=y+1
        x=0

    couleur=(contenu[i-3],contenu[i-2],contenu[i-1])
    #print(x,y,couleur)
    image.putpixel((x, y), couleur)
    #print(couleur)
    


# Enregistrement de l'image
image.save("image_random.png")

# Affichage de l'image (optionnel)

