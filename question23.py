import re
from collections import Counter

fichier = input("Chemin du fichier server.log : ")
try:
    with open(fichier, encoding="utf-8") as f:
        lignes = f.readlines()
except FileNotFoundError:
    print("Fichier introuvable.")
    exit()

failed = [line for line in lignes if "failed login" in line.lower()]
# extraction des adresses IP (IPv4 simples)
ips = []
for line in lignes:
    ips += re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", line)

count_failed = len(failed)
ip_counter = Counter(ips)
ip_plus_freq = ip_counter.most_common(1)[0] if ip_counter else ("Aucune IP", 0)

print(f"Nombre de lignes contenant 'failed login' : {count_failed}")
print(f"IP la plus fréquente : {ip_plus_freq[0]} ({ip_plus_freq[1]} occurrences)")
print("Résumé :")
print(f"- Total de lignes : {len(lignes)}")
print(f"- Lignes 'failed login' : {count_failed}")
print(f"- Nombre d'IP différentes : {len(ip_counter)}")
