import ssd1306

class Screen:
    
    def __init__(self, screenI2C):
        self.screenI2C = screenI2C
        
    def Show_Text(self,text,title=""):
        oled = ssd1306.SSD1306_I2C(128, 64, self.screenI2C	, 0x3c)
        oled.fill(0)
        oled.text(title, 0, 0)
        line_num = len(text)//16 + 1
        for i in range(line_num):
            oled.text("{}".format(text[0+i*16:16+i*16]),0,24+i*16)
        

        oled.show()
        