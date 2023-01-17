# Explications des champs pour chaque JSON

## daily_forecast
* `dt`: timestamp de l'heure/date de mesure
* `T`: 
    * `min`: valeur min en degrès C°
    * `max`: valeur max en degrès C°
* `humidity`: *(mêmes champs que `T`, mais en pourcents)*
* `weather12H`: 
    * `icon`: ca doit être un identifiant de logo jpense
    * `desc`: exemple: "ensolleillé", "nuageux"...
* `sun`:
    * `rise`: timestamp de la levée du soleil
    * `set`: timestamp du coucher du soleil
* `precipitation`:
    * `24h` *(unique champ)*: <span style="color: red;">PAS COMPRIS !!! À ANALYSER </span>

## hourly_forecast
* `dt`: timestamp de l'heure/date de mesure
* `T`: 
    * `value`: température réelle (degrés C°)
    * `windchill`: température ressentie
* `humidity`: humidité de l'air en %
* `rain`:
    * `1h` (*unique champ*): <span style="color: red;">**J'AI PAS COMPRIS, À ANALYSER!!!!!**</span>
*  `weather`:
    * `icon`: renvoye un espèce d'identifiant, peut-être le nom d'un logo ?
    * `desc`: comme son nom l'indique. Des exemples: "ensoleillé", "Nuageux"...

## probability_forecast
* `dt`: timestamp de l'heure/date de mesure des infos
* `rain`:
    * `3h`: probabilité en % qu'il pleuve dans les 3 prochaines heures (0 ou `null` si impossible)
    * `6h`: idem
* `snow`: *fonctionne de la même manière que **rain** mais pour la neige*
* `freezing`: probabilité en % qu'il gèle