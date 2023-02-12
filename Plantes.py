from machine import Pin, SoftI2C, ADC
import utime
import json
import urequests as requests

class Environement:
    
    def __init__(self, sda_pin, scl_pin, plantes):
        
        sda=Pin(sda_pin) # PYCOM-V
        scl=Pin(scl_pin) # PYCOM-V
        self.plantes = plantes
        self.i2c= SoftI2C(sda=sda, scl=scl, freq=400000) #I2C channel 0,pins,400kHz max
        self.address = 64
        self.STATUS_BITS_MASK = 0xFFFC
        
    def get_humi(self):
        # Read humidity
        self.i2c.writeto(self.address, b'\xF5') # Trigger humidity measurement
        utime.sleep_ms(29) # Wait for it to finish (29ms max)
        data = self.i2c.readfrom(self.address, 2) # Get the 2 byte result
        adjusted = (data[0] << 8) + data[1] # convert to 16 bit value
        adjusted &= self.STATUS_BITS_MASK # zero the status bits
        adjusted *= 125 # scale
        adjusted /= 1 << 16 # divide by 2^16
        adjusted -= 6 # subtract 6
        #print ("Humidity = %.1f" % adjusted)
        return adjusted

    def get_precise_humi(self):
        humilist = []
        for i in range(20):
            humilist.append(self.get_humi())
        return sum(humilist)/len(humilist)

    def get_temp(self):
        # Read temperature
        self.i2c.writeto(self.address, b'\xF3') # Trigger temperature measurement
        utime.sleep_ms(85) # Wait for it to finish (85ms max)
        data = self.i2c.readfrom(self.address, 2) # Get the 2 byte result
        ## Compute temperature
        adjusted = (data[0] << 8) + data[1] # convert to 16 bit value
        adjusted &= self.STATUS_BITS_MASK # zero the status bits
        adjusted *= 175.72 # scale
        adjusted /= 1 << 16 # divide by 2^16
        adjusted -= 46.85 # subtract offset
        #print ("Temperature = %.1f" % adjusted)
        return adjusted
    
    def get_precise_temp(self):
        templist = []
        for i in range(20):
            templist.append(self.get_temp())
        return sum(templist)/len(templist)
    
    def Get_Data(self):
        Plante_Data = {}
        for plante in self.plantes:
            Plante_Data[plante.name] = {
                "temperature": self.get_precise_temp(),
                "humiditeAir": self.get_precise_humi(),
                "humiditeSol": plante.get_mesure2(),
                "etatPlante": -1,
                "commText": "null",
                "arrosage": "Pas encore fait"
            }
        Plante_Data["date"] = "now"
        return json.dumps(Plante_Data)
        

class Plante:
    
    def __init__(self, hygrometrie_pin, name,calibrationAir=3000,calibrationWater = 1600):
        self.hygrometriePin = ADC(Pin(hygrometrie_pin))
        #self.atten =  ADC.ATTN_11DB #capt2
        #self.width = ADC.WIDTH_10BIT
        self.calibrationAir = calibrationAir
        self.calibationWater = calibrationWater
        self.name = name
        
        
    def get_mesure(self):
        humi_sol = []
        for i in range(100):
            humi_sol.append(self.hygrometriePin.read_u16()/65535*100)
        hum_sol_final = sum(humi_sol)/len(humi_sol)
        return hum_sol_final
    
    def get_mesure2(self):
        humi_sol = []
        for i in range(100):
            humi_sol.append(self.hygrometriePin.read())
        hum_sol_final = sum(humi_sol)/len(humi_sol)
        
        sm = (1- (hum_sol_final - self.calibationWater) / (self.calibrationAir - self.calibationWater)) * 100

        return sm
    
    
