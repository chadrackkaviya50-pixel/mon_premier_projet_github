import ipaddress

ip_list = []
# je demande les adresses IP à l’utilisateur
for i in range(5):
    ip = input(f"Adresse IP #{i+1} : ")
    ip_list.append(ip)

valides = []
for ip in ip_list:
    try:
        ipaddress.ip_address(ip)
        print(f"{ip} est valide")
        valides.append(ip)
    except ValueError:
        print(f"{ip} est invalide")

# enregistrer les IP valides
with open("ip_valides.txt", "w", encoding="utf-8") as f:
    for ip in valides:
        f.write(ip + "\n")
print(f"IP valides enregistrées dans ip_valides.txt")
