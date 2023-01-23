# confpeip

## Des détails sur les champs des fichiers JSON dans "daily_retrieved_data" sont contenus dans "analyse_des_json.md"

## Choses propres au code de Gogo

* j'utilise "meteofranceapi" en tant que librairie, pas en tant que fichier principal
* le code "ALANCERTOUSLESJOURS", je le lance tous les jours pour récupérer des données (puisque c'est dûr de trouver des bases de données toutes prêtes) et je ferais des jolis tableaux et courbes dans une semaine

# Serveur HTTP pour modifier le sheets
Le serveur est hébergé à `golgot.fr`, sur le port `42069`.
Il faut envoyer, à n'importe quel lien si le port est le bon, une requête POST contenant un JSON correspondant à ceci:
* `sansEngrais`: un objet JSON contenant:
    * `temperature`: température en degrés, un `float`
    * `humiditeAir`: assez clair je pense, en pourcents, un `float`
    * `humiditeSol`: *idem*
    * `etatPlante`: l'état de santé de la plante, `-1` si tu ne veux rien préciser et laisser la case vide, `1` si quasi morte, `2` si bof, `3` si parfait (tout ça en `float`)
    * `commText`: commentaire textuel, en string. Mettre `"null"` **EN STRING** si tu veux laisser la case vide
    * `arrosage`: string, qui peut valoir (**ATTENTION À LA CASSE !**) `Oui` si Noah a dû arroser, `Non` sinon, et `Pas encore fait` si tu laisses la case vide
* `avecEngrais`: idem mais pour la plante avec engrais
* `date`: date au format "01/01/1970-15" en `string` pour le 1er janvier 1970 à 15h, mettre "now" en `string` si tu veux mettre dans la ligne du jour et de l'heure actuelle

**Ne rien mettre de plus car je passe tout l'objet à une fonction conçue TRÈS PRÉCISEMENT pour ce formatage d'objet**

# Comment lancer/Librairies à utiliser

Les packages pip3 à installer sont (pour les gars qui voient pas ce que c'est envoyez moi un dm):
* `sympy`
* `matplotlib`
* `meteofrance-api`

pour les installer:

`pip3 install nomdupaquet` *dans un terminal*