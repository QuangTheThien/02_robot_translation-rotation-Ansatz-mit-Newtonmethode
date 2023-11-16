from app import App, Point
from newton import *

SSP = Point(200,400)# Schienen START Punkt
SEP = Point(600,400)# Schien END Punkt
AL = 200 #Armlänge

#--- application loop ---#
def loop(t:float):
    app.clearCanvas()#Canvas resetten
    app.drawText(app.mousePos,Point(100,150)) #Anzeige Position der Maus
    
    #statische Sachen
    app.drawLine(SSP,SEP,5,"green") #grüne Mittellinie
    app.drawLine(Point(SSP.x,SSP.y-AL),Point(SEP.x,SEP.y-AL)) # obere Randlinie
    app.drawLine(Point(SSP.x,SSP.y+AL),Point(SEP.x,SEP.y+AL)) # untere Randlinie
    app.drawArc(Point(0,200),400,400,90,180)#linker Bogen app.drawArc(Point((SSP.x-AL,SSP.y-AL)),2*AL,2*AL,90,180,)
    app.drawArc(Point(400,200),400,400,-90,180)#rechter Bogen app.drawArc(Point((SEP.x-AL,SEP.y-AL)),2*AL,2*AL,-90,180,)
    
    #dynamische Sachen in robotFunc:
    robotFunc(app.mousePos)
    
def robotFunc(targetPos:Point):
    MausPos = targetPos#Maus Position als Point übergeben
    def f (v:np.array):
        Funktion = np.array([f1(v) - MausPos.y, f2(v) - MausPos.x])#f1 und f2 in einem Array zusammenfügen
        return Funktion
    
    def f1(v:np.array):#Funktion für Y Wert
        YPunkt = AL*np.sin(v[1]) + 400 #v[1] = Winkel
        return YPunkt
    
    def f2(v:np.array): #Funktion für X Wert
        XPunkt = AL*np.cos(v[1]) + v[0] + 200 #v[0] = Sliderposition, v[1] = Winkel
        return XPunkt
    
    StartVektor = np.array([10, 10])# 10 stabiler als 1
    Wert = newton(StartVektor,f)#Array mit den Werten aus newton;
        #(Wert[0],Wert[1],Wert[2])#Wert 0 = Slider, Wert 1 = Winkel
    
    
    if Wert[2]==999: # falls newton divergiert
        Wert = np.array([0,0])#random standard Wert für Slider und Winkel
    
    #Übergabe der Werte, falls die Werte konvergieren
    Slider = Point(200+Wert[0],400) #Koordinaten Slider
    Kreis = Point(Wert[0]+AL*np.cos(Wert[1])+200,AL*np.sin(Wert[1])+400) #Koordinaten Schwarzer Punkt
        
    #dynamische Sachen
    app.drawRect(Slider-Point(10,10),20,20,"gray")#Slider
    app.drawLine(Slider,Kreis)#Arm
    app.drawCircle(Kreis,10,"black","black")#Schwarzer Punkt
    
#--- main ---#
app = App("My App", 800, 800)
app.start(loop)