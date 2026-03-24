#!/bin/bash
read -p "Chemin du dossier à sauvegarder : " dossier
# vérifier si le dossier existe
if [ ! -d "$dossier" ]; then
    echo "Le dossier $dossier n'existe pas."
    exit 1
fi

# créer le dossier sauvegardes s'il n'existe pas
mkdir -p sauvegardes

# nom de l'archive avec date
date_str=$(date +%F)
archive="backup_${date_str}.tar.gz"

# création de l'archive compressée
tar -czf "sauvegardes/$archive" -C "$dossier" .

echo "Sauvegarde créée : sauvegardes/$archive"
