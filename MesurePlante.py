import machine, ssd1306, time
from machine import Pin, SoftI2C, ADC
import esp32
from time import sleep
from Plantes import Environement, Plante
import temp_humi
import WLAN
import Screen
import ujson as json
import utime

def load_plants():
    file = open("config.cfg", "r")
    o = json.loads(file.read())
    file.close()
    plants = []
    for name,config in o["plantes"].items():
        plants.append(Plante(config["pin"], name, config["calibrationAIR"], config["calibrationWater"]))
    return plants



#reset = machine.Pin(17)
oledi2c = SoftI2C(scl=Pin(14), sda=Pin(12), freq=100000)
screen = Screen.Screen(oledi2c)

screen.Show_Text("Starting Water")

#------------AutoConnect-------------------

WLAN.disable_network()

Enviro = Environement(12,14,load_plants())

cooldown = utime.ticks_ms()
cooldown_time = 600*1000

while True:
    if utime.ticks_ms() > cooldown:
        screen.Show_Text("Prise de mesure")
        WLAN.disable_network()#Désactive le réseau pour utiliser les sorties ADC2
        mesureJSON = Enviro.Get_Data()
        #print(mesureJSON, end="\r")
        connection =  WLAN.enable_network()
        
        if connection != "":#Re-active le reseau pour envoyer les donnée
            #print(mesureJSON)
            screen.Show_Text("Connect: {}".format(connection), title="internet")
            time.sleep(3)
            screen.Show_Text(WLAN.send_Data(mesureJSON),title="Gauthier Server:")
            time.sleep(1)
            cooldown = utime.ticks_ms() + cooldown_time
        else:
            screen.Show_Text("Aucune Connexion Trouvé")
            time.sleep(2)
    
    else:
        dt = int((cooldown - utime.ticks_ms())/1000)
        screen.Show_Text("{}s remaining".format(dt), title="temps avant mesure")
        time.sleep(1)
    
    
        
        
