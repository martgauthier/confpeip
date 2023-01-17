from meteofranceapi import weather_data
import matplotlib as mpl
import sympy as sp
import json
import os
from datetime import datetime

wd=weather_data("44000")

print("À Nantes:")
print(wd.cast.daily_forecast)
print(wd.cast.forecast)

hourly_forecast=wd.cast.forecast
daily_forecast=wd.cast.daily_forecast
probability_forecast=wd.cast.probability_forecast

# S/o chatgpt qui a fait ce code
# Récupération de la date d'aujourd'hui
date_today = datetime.now().strftime("%d_%m")

# Création du chemin vers le dossier parent "dailydata"
parent_folder = "daily_retrieved_data"

# Création du chemin vers le dossier de la date d'aujourd'hui
date_folder = os.path.join(parent_folder, date_today)

# Création du dossier de la date d'aujourd'hui s'il n'existe pas
if not os.path.exists(date_folder):
    os.makedirs(date_folder)

# Écriture du fichier "hourly_forecast"
hourly_forecast_file = os.path.join(date_folder, "hourly_forecast.json")
with open(hourly_forecast_file, "w") as outfile:
    json.dump(hourly_forecast, outfile)

# Écriture du fichier "daily_forecast"
daily_forecast_file = os.path.join(date_folder, "daily_forecast.json")
with open(daily_forecast_file, "w") as outfile:
    json.dump(daily_forecast, outfile)

probability_forecast_file = os.path.join(date_folder, "probability_forecast.json")
with open(probability_forecast_file, "w") as outfile:
    json.dump(probability_forecast, outfile)

