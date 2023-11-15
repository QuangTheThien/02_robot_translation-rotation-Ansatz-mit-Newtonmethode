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
    
    #dynamische Sachen
    app.drawRect(Point(190,390),20,20,"gray")#Quadrat
    app.drawLine(Point(200,400),Point(200,200))#Arm
    app.drawCircle(Point(200,200),10,"black","black")#Punkt
    
    robotFunc(app.mousePos)
    
def robotFunc(targetPos:Point):
    MTuple = Point.toTuple(targetPos)
    # print(MArray[0])
    def f1(v:np.ndarray):#Funktion, um den Wert des Winkels zu berechnen
        phi = np.array(np.arcsin([(v[1]-400)/AL])) #Winkel
        print("Phi: " , phi)
        return phi
    
    def f2(v:np.ndarray): #Funktion, um den Translationswert zu berechnen
        Tx = np.array(AL*np.cos(np.arcsin([(v[1]-400)/AL])))
        print("Tx: " , Tx)
        return Tx
    
    def func(v:np.ndarray):
        Funktion = np.array([f1(v), f2(v)])
        print("Funktion: " , Funktion)
        print("Funktion shape: ", Funktion.shape)
        return Funktion
    print("f1 außerhalb: ", f1)
    print("f2 außerhalb: ", f2)
    print("func: ", func)
    
    MArray = np.array([[MTuple[0]], [MTuple[1]]]) #MTuple zu einer Array gemacht
    #print(MArray)
    func(MArray)
    print("MArray shape: ", MArray.shape)
    
    #newton(MArray,func)

#aktuelles Problem: func ist immer eine Dimension weiter als MArray

#--- main ---#
app = App("My App", 800, 800)
app.start(loop)