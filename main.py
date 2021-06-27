from machine import I2C, Pin
import time
from machine_i2c_lcd import I2cLcd
import bauteile as bt

i2c_1 = I2C(1,sda=Pin(6), scl=Pin(7),freq = 400000)
i2c_2 = I2C(0,sda=Pin(0), scl=Pin(1),freq = 400000)

lcd_1 = I2cLcd(i2c_1, 39, 2, 16)
lcd_2 = I2cLcd(i2c_2, 39, 2, 16)

lichtschranke_1 = bt.Lichtschranke(0, 30000)
lichtschranke_2 = bt.Lichtschranke(1, 35000)
    
Spieler_Eingabe_1 = bt.Spieler_Eingabe(12,13,14,15,11)
Spieler_Eingabe_2 = bt.Spieler_Eingabe(4,3,2,8,5)

Minus_Button_1 = bt.Minus_Button(16)
Minus_Button_2 = bt.Minus_Button(17)

spieler_liste = {"0000":"Gast_1", "0001":"Frank", "0010":"Till", "0011":"Franz", "0100":"Seidel", "0101":"Jacob", "0110":"John", "0111":"Marius", "1000":"Marie", "1001":"Pauli", "1010":"Leo", "1011":"Celine", "1100":"Paul", "1101":"Frei_2", "1110":"Frei_3", "1111":"Gast_2" }

def auf_spiel_warten(Spieler_Eingabe_1, Spieler_Eingabe_2, spieler_liste, lcd_1, lcd_2):
    
    keine_eingaben = True
    zähler = 0
    
    while keine_eingaben:
        
        if Spieler_Eingabe_1.gib_spieler() != None and Spieler_Eingabe_2.gib_spieler() != None:
            
            lcd_1.clear()
            lcd_2.clear()
            
            keine_eingaben = False
            
            return True #um spiel zu starten
            
        else:
            lcd_1.clear()
            lcd_2.clear()
            
            lcd_1.move_to(0,0)
            lcd_1.putstr("%s: %s"%(list(spieler_liste.values())[zähler], list(spieler_liste.keys())[zähler]))
            
            lcd_1.move_to(0,1)
            lcd_1.putstr("%s: %s"%(list(spieler_liste.values())[zähler+1], list(spieler_liste.keys())[zähler+1]))
            
            lcd_2.move_to(0,0)
            lcd_2.putstr("%s: %s"%(list(spieler_liste.values())[zähler+2], list(spieler_liste.keys())[zähler+2]))
          
            lcd_2.move_to(0,1)
            lcd_2.putstr("%s: %s"%(list(spieler_liste.values())[zähler+3], list(spieler_liste.keys())[zähler+3]))
            
            zähler += 4
            
            if zähler == 16:
                zähler = 0
                
            time.sleep(2)
            
def spiel(Spieler_Eingabe_1, Spieler_Eingabe_2, spieler_liste, lcd_1, lcd_2, lichtschranke_1, lichtschranke_2):
    
    spieler_kürzel_1 = Spieler_Eingabe_1.gib_spieler()#umgekehrt da denkfehler bei der instalation
    spieler_kürzel_2 = Spieler_Eingabe_2.gib_spieler() #umkehrung keinen effekt auf restlichhen code  
    
    if spieler_kürzel_1 != spieler_kürzel_2:
        
        lcd_1.move_to(0,0)
        lcd_1.putstr("%s vs %s"%(spieler_liste[spieler_kürzel_1], spieler_liste[spieler_kürzel_2]))
        
        lcd_1.move_to(0,1)
        lcd_1.putstr("0 : 0")
        
        lcd_2.move_to(0,0)
        lcd_2.putstr("%s vs %s"%(spieler_liste[spieler_kürzel_2], spieler_liste[spieler_kürzel_1]))
        
        lcd_2.move_to(0,1)
        lcd_2.putstr("0 : 0")
        
        spiel = True
        
        tor_zähler_1 = 0
        tor_zähler_2 = 0
        
        while spiel:
            
            if lichtschranke_1.treffer():
                
                tor_zähler_1 += 1
                
                if tor_zähler_1 >= 10:
                    
                    lcd_1.clear()
                    lcd_2.clear()
                    
                    lcd_1.move_to(0,0)
                    lcd_1.putstr("Gewonnen %s"%spieler_liste[spieler_kürzel_1])
                    
                    lcd_2.move_to(0,0)
                    lcd_2.putstr("Gewonnen %s"%spieler_liste[spieler_kürzel_1])
                    
                    sec_zähler = 15 #zeit um letzen punkt zurück zu nehmen
                    
                    while sec_zähler > 0:
                        
                        lcd_1.move_to(0,1)
                        lcd_1.putstr("%i "%sec_zähler)
                        
                        lcd_2.move_to(0,1)
                        lcd_2.putstr("%i "%sec_zähler)
                        
                        time.sleep(1)
                        
                        if Minus_Button_1.ist_gedrückt():
                            
                            sec_zähler = 0
                            
                            tor_zähler_1 = 9
                            
                            lcd_1.move_to(0,0)
                            lcd_1.putstr("%s vs %s"%(spieler_liste[spieler_kürzel_1], spieler_liste[spieler_kürzel_2]))
                            
                            lcd_2.move_to(0,0)
                            lcd_2.putstr("%s vs %s"%(spieler_liste[spieler_kürzel_2], spieler_liste[spieler_kürzel_1]))
                            
                            lcd_1.move_to(0,1)
                            lcd_1.putstr("%i : %i"%(tor_zähler_1, tor_zähler_2))
                            
                            lcd_2.move_to(0,1)
                            lcd_2.putstr("%i : %i"%(tor_zähler_2, tor_zähler_1))
                            
                            while Minus_Button_1.ist_gedrückt():
                                #um nur 1 tor abzuziehen
                                time.sleep_ms(50)
                                
                        sec_zähler -= 1
                                
                    if tor_zähler_1 == 10:
                        
                        spiel = False
                        
                        tor_zähler_1 = 0
                        tor_zähler_2 = 0
                        
                        #Abspeichern des gesammtspielstandes
                        #2 Dateien um später lesen zu erleichten (Speicher nicht problematisch)
                        text_dokument = open("Spielstände/%s-%s.txt"%(spieler_kürzel_1, spieler_kürzel_2), "r")
                        alter_stand = text_dokument.read()
                        text_dokument.close()
                        
                        text_dokument = open("Spielstände/%s-%s.txt"%(spieler_kürzel_1, spieler_kürzel_2), "w")#2. öffnen um alen inhalt zu löschen
                        text_dokument.write("%s:%s"%(str(int(alter_stand.split(":")[0])+1), str(alter_stand.split(":")[1])))
                        text_dokument.close()
                        
                        #2.Datei
                        text_dokument = open("Spielstände/%s-%s.txt"%(spieler_kürzel_2, spieler_kürzel_1), "r")
                        alter_stand = text_dokument.read()
                        text_dokument.close()
                        
                        text_dokument = open("Spielstände/%s-%s.txt"%(spieler_kürzel_2, spieler_kürzel_1), "w")#2. öffnen um alen inhalt zu löschen
                        text_dokument.write("%s:%s"%(str(alter_stand.split(":")[0]), str(int(alter_stand.split(":")[1])+1)))
                        text_dokument.close()
                        
                        lcd_1.clear()
                        lcd_2.clear()
                            
                        lcd_1.move_to(0,0)
                        lcd_1.putstr("Spielstand:")
                            
                        lcd_2.move_to(0,0)
                        lcd_2.putstr("Spielstand:")
                            
                        text_dokument = open("Spielstände/%s-%s.txt"%(spieler_kürzel_1, spieler_kürzel_2), "r")
                        stand_1 = text_dokument.read()
                        text_dokument.close()
                            
                        text_dokument = open("Spielstände/%s-%s.txt"%(spieler_kürzel_2, spieler_kürzel_1), "r")
                        stand_2 = text_dokument.read()
                        text_dokument.close()
                            
                        lcd_1.move_to(0,1)
                        lcd_1.putstr("%s:%s"%(stand_1.split(":")[0], stand_1.split(":")[1]))
                                         
                        lcd_2.move_to(0,1)
                        lcd_2.putstr("%s:%s"%(stand_2.split(":")[0], stand_2.split(":")[1]))
                        
                        
                        sec_zähler = 7 #zeit des anzeigen des spielstandes
                        
                        while sec_zähler > 0:
                                         
                            sec_zähler -= 1
                                         
                            time.sleep(1)
                            
                        lcd_1.clear()
                        lcd_2.clear()
                            
                        lcd_1.move_to(0,0)
                        lcd_1.putstr("Neustart in:")
                            
                        lcd_2.move_to(0,0)
                        lcd_2.putstr("Neustart in:")
                        
                        if Spieler_Eingabe_1.gib_spieler() != None or Spieler_Eingabe_2.gib_spieler() != None:
                        
                            sec_zähler = 15 #zeit um Neustart abzubrechen
                    
                            while sec_zähler > 0:
                                
                                lcd_1.move_to(0,1)
                                lcd_1.putstr("%i "%sec_zähler)
                                
                                lcd_2.move_to(0,1)
                                lcd_2.putstr("%i "%sec_zähler)
                                
                                sec_zähler -=1
                                
                                if Spieler_Eingabe_1.gib_spieler() == None or Spieler_Eingabe_2.gib_spieler() == None:
                                    
                                    sec_zähler = 0
                                
                                time.sleep(1)
                else:
                    
                    lcd_1.move_to(0,1)
                    lcd_1.putstr("%i : %i  "%(tor_zähler_1, tor_zähler_2))
                    
                    lcd_2.move_to(0,1)
                    lcd_2.putstr("%i : %i  "%(tor_zähler_2, tor_zähler_1))
                    
                    time.sleep(1)
            
                
            if lichtschranke_2.treffer():
                
                tor_zähler_2 += 1
                
                if tor_zähler_2 >= 10:
                    
                    lcd_1.clear()
                    lcd_2.clear()
                    
                    lcd_1.move_to(0,0)
                    lcd_1.putstr("Gewonnen %s"%spieler_liste[spieler_kürzel_2])
                    
                    lcd_2.move_to(0,0)
                    lcd_2.putstr("Gewonnen %s"%spieler_liste[spieler_kürzel_2])
                    
                    sec_zähler = 15 #zeit um letzen punkt zurück zu nehmen
                    
                    while sec_zähler > 0:
                        
                        lcd_1.move_to(0,1)
                        lcd_1.putstr("%i "%sec_zähler)
                        
                        lcd_2.move_to(0,1)
                        lcd_2.putstr("%i "%sec_zähler)
                        
                        time.sleep(1)
                        
                        if Minus_Button_2.ist_gedrückt():
                            
                            sec_zähler = 0
                            
                            tor_zähler_2 = 9
                            
                            lcd_1.move_to(0,0)
                            lcd_1.putstr("%s vs %s"%(spieler_liste[spieler_kürzel_1], spieler_liste[spieler_kürzel_2]))
                            
                            lcd_2.move_to(0,0)
                            lcd_2.putstr("%s vs %s"%(spieler_liste[spieler_kürzel_2], spieler_liste[spieler_kürzel_1]))
                            
                            lcd_1.move_to(0,1)
                            lcd_1.putstr("%i : %i"%(tor_zähler_1, tor_zähler_2))
                            
                            lcd_2.move_to(0,1)
                            lcd_2.putstr("%i : %i"%(tor_zähler_2, tor_zähler_1))
                            
                            while Minus_Button_2.ist_gedrückt():
                                #um nur 1 tor abzuziehen
                                time.sleep_ms(50)
                                
                        sec_zähler -= 1
                                
                    if tor_zähler_2 == 10:
                        
                        spiel = False
                        
                        tor_zähler_1 = 0
                        tor_zähler_2 = 0
                        
                        #Abspeichern des gesammtspielstandes
                        #2 Dateien um später lesen zu erleichten (Speicher nicht problematisch)
                        text_dokument = open("Spielstände/%s-%s.txt"%(spieler_kürzel_1, spieler_kürzel_2), "r")
                        alter_stand = text_dokument.read()
                        text_dokument.close()
                        
                        text_dokument = open("Spielstände/%s-%s.txt"%(spieler_kürzel_1, spieler_kürzel_2), "w")#2. öffnen um alen inhalt zu löschen
                        text_dokument.write("%s:%s"%(str(alter_stand.split(":")[0]), str(int(alter_stand.split(":")[1])+1)))
                        text_dokument.close()
                        
                        #2.Datei
                        text_dokument = open("Spielstände/%s-%s.txt"%(spieler_kürzel_2, spieler_kürzel_1), "r")
                        alter_stand = text_dokument.read()
                        text_dokument.close()
                        
                        text_dokument = open("Spielstände/%s-%s.txt"%(spieler_kürzel_2, spieler_kürzel_1), "w")#2. öffnen um alen inhalt zu löschen
                        text_dokument.write("%s:%s"%(str(int(alter_stand.split(":")[0])+1), str(alter_stand.split(":")[1])))
                        text_dokument.close()
                        
                        lcd_1.clear()
                        lcd_2.clear()
                            
                        lcd_1.move_to(0,0)
                        lcd_1.putstr("Spielstand:")
                            
                        lcd_2.move_to(0,0)
                        lcd_2.putstr("Spielstand:")
                            
                        text_dokument = open("Spielstände/%s-%s.txt"%(spieler_kürzel_1, spieler_kürzel_2), "r")
                        stand_1 = text_dokument.read()
                        text_dokument.close()
                            
                        text_dokument = open("Spielstände/%s-%s.txt"%(spieler_kürzel_2, spieler_kürzel_1), "r")
                        stand_2 = text_dokument.read()
                        text_dokument.close()
                            
                        lcd_1.move_to(0,1)
                        lcd_1.putstr("%s:%s"%(stand_1.split(":")[0], stand_1.split(":")[1]))
                                         
                        lcd_2.move_to(0,1)
                        lcd_2.putstr("%s:%s"%(stand_2.split(":")[0], stand_2.split(":")[1]))
                        
                        
                        sec_zähler = 7 #zeit des anzeigen des spielstandes
                        
                        while sec_zähler > 0:
                                         
                            sec_zähler -= 1
                                         
                            time.sleep(1)
                        
                        if Spieler_Eingabe_1.gib_spieler() != None or Spieler_Eingabe_2.gib_spieler() != None:
                            
                            lcd_1.clear()
                            lcd_2.clear()
                                
                            lcd_1.move_to(0,0)
                            lcd_1.putstr("Neustart in:")
                                
                            lcd_2.move_to(0,0)
                            lcd_2.putstr("Neustart in:")
                        
                            sec_zähler = 15 #zeit um Neustart abzubrechen
                        
                            while sec_zähler > 0:
                                
                                lcd_1.move_to(0,1)
                                lcd_1.putstr("%i "%sec_zähler)
                                
                                lcd_2.move_to(0,1)
                                lcd_2.putstr("%i "%sec_zähler)
                                
                                sec_zähler -=1
                                
                                if Spieler_Eingabe_1.gib_spieler() == None or Spieler_Eingabe_2.gib_spieler() == None:
                                    
                                    sec_zähler = 0
                                
                                time.sleep(1)
                else:
                
                    lcd_1.move_to(0,1)
                    lcd_1.putstr("%i : %i  "%(tor_zähler_1, tor_zähler_2))
                    
                    lcd_2.move_to(0,1)
                    lcd_2.putstr("%i : %i  "%(tor_zähler_2, tor_zähler_1))
                    
                    time.sleep(1)
                
                
            if Minus_Button_1.ist_gedrückt():
                
                if tor_zähler_1 > -99: #um zu großen Wert zu verhindern
                
                    tor_zähler_1 -= 1
                    
                    lcd_1.move_to(0,1)
                    lcd_1.putstr("%i : %i"%(tor_zähler_1, tor_zähler_2))
                    
                    lcd_2.move_to(0,1)
                    lcd_2.putstr("%i : %i"%(tor_zähler_2, tor_zähler_1))
                    
                while Minus_Button_1.ist_gedrückt():
                    #um nur 1 tor pro druck abzuziehen bzw. loop ohne pause zu verhindern
                    time.sleep_ms(50)
                    
                    if  Minus_Button_2.ist_gedrückt(): #um spiel abzubrechen
                        
                        if Spieler_Eingabe_1.gib_spieler() == None and Spieler_Eingabe_2.gib_spieler() == None:
                            spiel = False
            
            if Minus_Button_2.ist_gedrückt():
                
                if tor_zähler_2 > -99: #um zu großen Wert zu verhindern
                    
                    tor_zähler_2 -= 1
                    
                    lcd_1.move_to(0,1)
                    lcd_1.putstr("%i : %i"%(tor_zähler_1, tor_zähler_2))
                    
                    lcd_2.move_to(0,1)
                    lcd_2.putstr("%i : %i"%(tor_zähler_2, tor_zähler_1))
                
                while Minus_Button_2.ist_gedrückt():
                    #um nur 1 tor pro druck abzuziehen bzw. loop ohne pause zu verhindern
                    time.sleep_ms(50)
                    
                    if  Minus_Button_1.ist_gedrückt(): #um spiel abzubrechen
                        
                        if Spieler_Eingabe_1.gib_spieler() == None and Spieler_Eingabe_2.gib_spieler() == None:
                            spiel = False
        
        time.sleep_us(50)
        
    else:
        
        lcd_1.clear()
        lcd_2.clear()
                
        lcd_1.move_to(0,0)
        lcd_1.putstr("Fehler erkannt:")
                
        lcd_2.move_to(0,0)
        lcd_2.putstr("Fehler erkannt:")
                
        lcd_1.move_to(0,1)
        lcd_1.putstr("2x %s"%spieler_kürzel_1)
                
        lcd_2.move_to(0,1)
        lcd_2.putstr("2x %s"%spieler_kürzel_1)
        
        time.sleep(1)
        
while True:
    
    if auf_spiel_warten(Spieler_Eingabe_1, Spieler_Eingabe_2, spieler_liste, lcd_1, lcd_2):
        spiel(Spieler_Eingabe_1, Spieler_Eingabe_2, spieler_liste, lcd_1, lcd_2, lichtschranke_1, lichtschranke_2)
