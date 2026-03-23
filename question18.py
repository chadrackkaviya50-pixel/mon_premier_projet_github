import csv

chemin = input("Chemin du fichier CSV : ")
etudiants = []
with open(chemin, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if not row:
            continue
        nom, note_str = row[0], row[1]
        try:
            note = float(note_str)
        except ValueError:
            print(f"Note invalide pour {nom}.")
            continue
        etudiants.append((nom, note))

# j'affiche les étudiants
print("Liste des étudiants et notes :")
for nom, note in etudiants:
    print(f"{nom} : {note}")

# je calcul  la moyenne
moyenne = sum(n for _, n in etudiants) / len(etudiants) if etudiants else 0
print(f"Moyenne générale : {moyenne:.2f}")

# je choisis le meilleur étudiant
if etudiants:
    meilleur = max(etudiants, key=lambda x: x[1])
    print(f"Meilleure note : {meilleur[0]} avec {meilleur[1]}")
# étudiants sous la moyenne de 10
moins_de_10 = [nom for nom, note in etudiants if note < 10]
if moins_de_10:
    print("Étudiants ayant une note < 10 :")
    for nom in moins_de_10:
        print(f" - {nom}")
