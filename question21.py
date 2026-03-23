import getpass
from datetime import datetime

mot_de_passe_correct = "Secret123!"  # je remplace par une valeur sécurisée
max_tentatives = 3

for tentative in range(1, max_tentatives + 1):
    entre = getpass.getpass("Entrez le mot de passe : ")
    resultat = "Réussi" if entre == mot_de_passe_correct else "Échec"
    # journalisation
    with open("access.log", "a", encoding="utf-8") as logf:
        logf.write(f"{datetime.now().isoformat()} - Tentative {tentative} : {resultat}\n")
    if entre == mot_de_passe_correct:
        print("Accès autorisé")
        break
    else:
        print("Accès refusé")
else:
    print("Nombre de tentatives épuisé")
