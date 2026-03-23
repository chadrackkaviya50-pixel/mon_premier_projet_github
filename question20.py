import os

dossier = input("Chemin du dossier : ")
if not os.path.isdir(dossier):
    print("Le dossier n'existe pas.")
    exit()

fichiers = [f for f in os.listdir(dossier) 
if os.path.isfile(os.path.join(dossier, f))]
taille_totale = 0
plus_gros = ("", 0)

for f in fichiers:
    path = os.path.join(dossier, f)
    taille = os.path.getsize(path)
    taille_totale += taille
    print(f"{f} : {taille} octets")
    if taille > plus_gros[1]:
        plus_gros = (f, taille)

print(f"Le plus gros fichier :
{plus_gros[0]} ({plus_gros[1]} octets)")
print(f"Taille totale du dossier : 
{taille_totale} octets")
