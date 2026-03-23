def lambda_handler(event, context):
    """
    Fonction d'entrée pour AWS Lambda.
    event : dictionnaire contenant les données de l'appel
    context : informations d'exécution fournies par AWS
    """
    nom = event.get("nom", "inconnu")
    message = f"Bonjour {nom}, bienvenue dans AWS Lambda"
    return {
        "statusCode": 200,
        "body": message
    }
