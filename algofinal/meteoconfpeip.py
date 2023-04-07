import requests
import json

class Meteo:
    token="0b58cbcceae275f9c7e0de90576bbc8ba969a11db8c8692b47d7b1027fa2f82d"
    nantesInseeCode=44109

    def getDayForecasts():
        '''
        dayDelta=0: prévisions pour tout de suite, 1: demain, 2: après demain...
        '''
        req=requests.get("https://api.meteo-concept.com/api/forecast/daily?token="+Meteo.token+"&insee="+str(Meteo.nantesInseeCode))
        if(req.status_code!=200):
            raise Exception(req.text)
        else:
            return json.loads(req.text)["forecast"]

    def getDayPrecipitationAndProb(dayDelta):
        fc=Meteo.getDayForecasts()

        return (fc[dayDelta]["rr10"], fc[dayDelta]["probarain"])

    def getDayEtp(dayDelta):
        fc=Meteo.getDayForecasts()

        return fc[dayDelta]["etp"]