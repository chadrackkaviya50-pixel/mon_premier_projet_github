#!/bin/bash
read -p "Entrez le nom du fichier : " fichier
if [ -e "$fichier" ]; then
    echo "Le fichier '$fichier' existe."
    taille=$(stat -c%s "$fichier")
    perms=$(stat -c%A "$fichier")
    echo "Taille : $taille octets"
    echo "Permissions : $perms"
else
    echo "Le fichier '$fichier' n'existe pas."
fi
