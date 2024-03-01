
taille_fichier=1025
largeur=512
y=0
x=0
for i in range(taille_fichier):

    x=x+1

    if i%largeur == 0:
        y=y+1
        x=0

    print(x,y)