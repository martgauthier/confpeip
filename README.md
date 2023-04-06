# confpeip

# Serveur HTTP pour modifier le sheets
Le serveur est hébergé à `golgot.fr`, sur le port `42069`.
Le chemin de la requête ne compte pas, ça peut être n'importe quoi (ou être vide).
Objet à envoyer:

* `nomDeLaFeuille`: (*remplacer `nomDeLaFeuille` par le nom de la feuille que vous voulez créer ou modifier*) un objet JSON contenant:
    * `temperature`: température en degrés, un `float`
    * `humiditeAir`: assez clair je pense, en pourcents, un `float`
    * `humiditeSol`: *idem*
    * `etatPlante`: l'état de santé de la plante, `-1` si tu ne veux rien préciser et laisser la case vide, `1` si quasi morte, `2` si bof, `3` si parfait (tout ça en `float`)
    * `commText`: commentaire textuel, en string. Mettre `"null"` **EN STRING** si tu veux laisser la case vide
    * `arrosage`: string, qui peut valoir (**ATTENTION À LA CASSE !**) `Oui` si Noah a dû arroser, `Non` sinon, et `Pas encore fait` si tu laisses la case vide
* (*remettre autant d'objets comme le précédent que voulus*)
* `date`: date au format "01/01/1970-15:05" en `string` pour le 1er janvier 1970 à 15h05, mettre "now" en `string` si tu veux mettre dans la ligne du jour et de l'heure actuelle

**Ne rien mettre de plus car je passe tout l'objet à une fonction conçue TRÈS PRÉCISEMENT pour ce formatage d'objet**