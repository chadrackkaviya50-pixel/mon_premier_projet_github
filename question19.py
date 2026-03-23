import re

password = input("Entrez un mot de passe : ")

violations = []
if len(password) < 10:
    violations.append("doit contenir au moins 10 caractères")
if not re.search(r"[A-Z]", password):
    violations.append("doit contenir au moins une majuscule")
if not re.search(r"[a-z]", password):
    violations.append("doit contenir au moins une minuscule")
if not re.search(r"\d", password):
    violations.append("doit contenir au moins un chiffre")
if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    violations.append("doit contenir au moins un caractère spécial")

if violations:
    print("Mot de passe invalide :")
    for v in violations:
        print(f" - {v}")
else:
    print("Mot de passe valide.")
