# import requests : # 
import requests
response = requests.get("https://quotes.toscrape.com/")
 # Affiche le code de statut HTTP (200, 404, 500…)
print(response.status_code)
 # Affiche le contenu HTML de la page
print(response.content)
