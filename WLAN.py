import network
import urequests as requests
import utime
import ujson as json
station = network.WLAN(network.STA_IF)

def load_wifi():
    file = open("config.cfg", "r")
    o = json.loads(file.read())
    file.close()
    plants = []
    return o["wifi"]

password_from_SSID = load_wifi()

def disable_network():
    station.active(False)

def enable_network(screen=""):
    ssid_on_net = show_network()
    #print(ssid_on_net)
    for i in ssid_on_net:
        if i in password_from_SSID.keys():
            disconnect()
            connect(i, password_from_SSID[i])
            
            if screen != "":
                screen.Show_Text(i,title="Conncected To :")
            else:
                print("connected to {}".format(i))
            print("c'est fini")
            return i
            
    return ""
    

def show_network(debug=False):
    ssid_list=  []
    station.active(True)
    for (ssid, bssid, channel, RSSI, authmode, hidden) in station.scan():
        if debug:
            print("* {:s}".format(ssid))
            print(" - Channel: {}".format(channel))
            print(" - RSSI: {}".format(RSSI))
            print(" - BSSID: {:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}".format(*bssid))
            print()
        ssid_list.append("{:s}".format(ssid))
    return ssid_list
        

def connect(ssid, password):
    import network
    ip = '192.168.1.110'
    subnet = '255.255.255.0'
    gateway = '192.168.1.1'
    dns = '8.8.8.8'
    station = network.WLAN(network.STA_IF)
    if station.isconnected() == True:
        print("Already connected")
        print(station.ifconfig())
        return
    
    station.active(True)
    #station.ifconfig((ip,subnet,gateway,dns))
    station.connect(ssid,password)
    timeout = utime.ticks_ms() + 2000
    while station.isconnected() == False:
        if utime.ticks_ms() > timeout:
            break
            print("timeout")
        pass
    print("Connection successful")
    print(station.ifconfig())

def disconnect():
    import network
    station = network.WLAN(network.STA_IF)
    station.disconnect()
    station.active(False)

def send_Data(json_data,url = 'http://golgot.fr:42069',):
    response = requests.post(url, json=json_data)
    return response.text
