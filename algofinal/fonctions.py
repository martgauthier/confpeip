def decisionArrosage(hPrevu, seuilLimite, precipitations, proba, etp, volumePot, surfacePot, fc):
    '''
    Liste des paramètres:
        -hPrevu: humidité prévue à J+1 (en pourcents)
        -seuilLimite: "wilting point" (en pourcents)
        -precipitations: precipitations annoncées jusqu'à J+1 (mm)
        -proba: proba de pluie (entier entre 0 et 1)
        -etp: total d'evapotranspiration aujourd'hui (mm)
        -volumePot (mL)
        -surfacePot (cm²)
        -fc: "field capacity" (%), l'objectif d'humidité à viser
    Retourne:
        la quantité qu'il faut arroser tout de suite, pour éviter qu'à J+1 on finisse en dessous du wilting point
    '''
    if(hPrevu <= seuilLimite):
        quantiteAArroserSansPluie=(fc-hPrevu)*volumePot + etp*surfacePot
        quantiteApporteeParPluie=precipitations*surfacePot

        return quantiteAArroserParPluie - proba*quantiteApporteeParPluie #si proba=1, on économisera au max, si proba=0 on arrosera au max
    else:
        return 0


def calculTauInitial(listeDerniersTau):
    '''
    Liste des paramètres:
        -listeDerniersTau: liste de 5 élements contenant les derniers tau des exponentielles précédentes, en commencant par la plus vieille et en finissant par la plus récente
    Retourne:
        -la moyenne pondérée (nouveau tau), qui accorde un poids plus important aux tau récents qu'aux tau vieux.
    '''
    sommeTotale=listeDerniersTau[0]+2*listeDerniersTau[1]+3*listeDerniersTau[2]+4*listeDerniersTau[3]+5*listeDerniersTau[4]
    return sommeTotale/(1+2+3+4+5)

