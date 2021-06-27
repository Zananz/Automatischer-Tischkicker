#Klassen für physische bauteile

from machine import ADC #für lichtschranke (photoresitor)

from machine import Pin #für Schalter und Taster

class Lichtschranke(): #ball unterbricht diese wenn: tor
    
    def __init__(self, pin, grenzwert):
        
        self.pin = ADC(pin)
        self.grenzwert = grenzwert #Spannungen der Lichtschranken variert leicht (unterschiede in ele. Bauteilen) 
        
    def treffer(self): # gibt true für treffer zurück
        
        wert = self.pin.read_u16()
    
        if wert > self.grenzwert: 
            return False
        else:
            return True
        
class Spieler_Eingabe(): # 4 Schalter zur eingabe, 1 Schalter zum bestätigen
    
    def __init__(self, pin_1, pin_2, pin_3, pin_4, pin_5):
        
        self.pin_1 = Pin(pin_1, Pin.IN, Pin.PULL_DOWN)
        self.pin_2 = Pin(pin_2, Pin.IN, Pin.PULL_DOWN)
        self.pin_3 = Pin(pin_3, Pin.IN, Pin.PULL_DOWN)
        self.pin_4 = Pin(pin_4, Pin.IN, Pin.PULL_DOWN)
        
        self.pin_5 = Pin(pin_5, Pin.IN, Pin.PULL_DOWN)
        
    def gib_spieler(self): #gibt str mit 4 stelliger binärzahl oder None zurück
        
        if self.pin_5.value() == 1:
            return "%i%i%i%i"%(self.pin_1.value(), self.pin_2.value(), self.pin_3.value(), self.pin_4.value())
        else:
            return None
        
class Minus_Button(): #Taster um ein tor der jewaligen seite zu löschen
    
    def __init__(self, pin):
        
        self.pin = Pin(pin, Pin.IN, Pin.PULL_DOWN)
        
    def ist_gedrückt(self): #gibt True oder False zurück
        
        return bool(self.pin.value())
        