#import cc.arduino.*
#import org.firmata.*
#Firmata firmata
from funciones import Arduino, guardarArchivo
#inicializar una instancia de Arduino para comunicarse
arduino=Arduino

#Variables para trazar el gráfico
x1,x2,y1,y2 = 0,0,0,0 #coordenadas para trazar lineas en el gráfico
ax,ay,divisionesx,divisionesy = 0,0,10,10 #diviones del gráfico
nombreArchivo,ensayofiles = "","" #variables para almacenar los datos en un archivo
pin1=4
pin2=5
pin3=6
Pmax,Rmax = 0,0
#coordenadas del gráfico
Xmin=450
Ymin=200
Xmax=Xmin+500
Ymax=Ymin+500 

#Variables  de Control de la Maquina
area=0.0 #area= area de la probeta en mm2
LI=0.0 #LI=Longitud inicial de la probeta
LP=0.0 #LP=longitud de la probeta al final de la precarga


#variables para almacenar el valor de los sensores medidos en arduino
sensor1=0   #sensor1=alargamiento 
sensor2=0   #sensor2=fuerza
VV=45       #VV= valor de PWM para la valvula proporcional
VIR=3470    #VIR=Valor Inicial de Recorrido
VIF=2200    #VIF=Valor Inicial de Fuerza

bomba=False
valvula=False
ritmo=False
ensayo=False

#datos de salida medidos y válvula  proporcional
recorrido=0.0
deformacion=0.0
fuerza=0.0
esfuerzo=0.0
proporcional=0.0
VF=0 

millisa=0.0 #millisa=tiempo anterior
fuerzaant=0.0 #fuerzaant=fuerza anterior
dt=0.0 #dt=delta de tiempo entre una medicion y otra
df=0.0 #df=variación de fuerza


relevo=0
relevo1=0
comparacion=10
debug1=0
valores=0

#variables para los loops de control de fase
CP=False #CP=Comienzo de Precarga
FP=False #FP=Fin de Precarga
FA=False #FA=Fuerza Alargamiento
CE=False #CE=comienzo de Ensayo
FE=False #FE=Fin de Ensayo
NS=False #NS=nuevo valor sensado
PV=False #PV=Parada Virtual, detiene la valvula proporcional para que deje de aumentar
          #la presion, y por lo tanto es necesario volver a empezar


#Variables para almacenar los datos de recorrido y presión
valuesa=[]
valuesf=[]
valuesd=[]
valuese=[]

#bytes recibidos por el puerto serial
serialData=0

def setup():
  
  size(1024,768,JAVA2D) #dibuja la ventana
  background(230) #colorea el fondo 
  createGUI() # crea la interfaz con los botonos y campos de texto
  customGUI() #crea el gráfico y otras partes de la interfaz
  FA=False
  cambiarGrafico(FA)#defmax.setText("")
  #esfmax.("")
  #println(Arduino.list())
  #arduino = new Arduino(this, Arduino.list()[1], 57600)
  #printArray(Serial.list())
  
  
  delay(2000)
   
  
  #myport.bufferUntil(START_SYSEX)
  arduino.adsConfig(arduino.DIFERENCIALMODE,arduino.GAIN_1)
  #recorrido=float(sensor1)
  #valuesr.append(map(recorrido, 0, 1024, 0, 300))
  #recorridot.setText(str(recorrido))
  #presion=float(sensor2)
  #valuesp.append(map(presion, 0, 1024, 0, 300))#Revisar map function and float lenght
  #presiont.setText(str(presion))



def draw(): 
  
  if((valvula)and(not FP)and(NS)and(not PV)):#fuerza menor a 100kg --
    if(not CP): 
      LI=float(longitud.getText())
      area=float(areatext.getText())
      CP=True
      millisa=millis()
      FA=False
      cambiarGrafico(FA)
    

    if(fuerza>200):
      FP=True
      VV+=1
      Mensaje("PRECARGA FINALIZADA","Puede continuar con el ensayo")
    
      """if(((millis()-millisa)/1000)>5){
       VV--
       mill#isa=millis()
       analogWrite(pin3,VV)
       proporcionalb.setValue(VV)
       println(VV,"unidades")
       
    }"""
    NS=False
  
    if(relevo>10):
      if(FP):
        print(sensor1,"  ",recorrido,"mm",VV)
        print(sensor2,"  ",fuerza,"kg")
        print()
      
      else:
        print(sensor1,"  ",sensor1*0.1875,"mV  ",recorrido,"mm")
        print(sensor2,"  ",sensor2*0.1875,"mV  ",fuerza,"kg")
        print()
      
      if(not CE): relevo=0
    
    
  if( (ensayo) and (FP) and (NS) and (not PV)):
    if(not CE):
      Rmax=int(defmax.getText())
      Pmax=int(esfmax.getText())
      area=float(areatext.getText())
      LI=float(longitud.getText())
      VF=20#proporcionalb.getValueF()
      CE=True
      relevo=0
      customGUI()
    
    
  #Reconocimiento de rotura y de la velocidad de aplicacion de la fuerza
  dt=(millis()-millisa)/1000
  
  deformacion=recorrido/LI
  esfuerzo=(fuerza/area)/100
   
  
  valuesa.append(recorrido)
  valuesf.append(fuerza)
  valuesd.append(deformacion)
  valuese.append(esfuerzo)

  if((CE)and(relevo>5)):
    if dt>0 and relevo1 > comparacion:
        df=(fuerza-fuerzaant)/dt
        if(fuerza<150):
          arduino.analogWrite(pin3,255)
          guardarArchivo(valuesf,valuesa,valuese,valuesd)
          ensayo=~ensayo
        
        if(df<VF and VV>0 and ensayo==True):
          VV-=1
          arduino.analogWrite(pin3,VV) 
          comparacion+=1
        
        #if(ndf>VF and VV<50){
        #  VV++
        #  analogWrite(pin3,VV)
        #}
        millisa=millis()
        fuerzaant=fuerza
        proporcionalb.setValue(VV)
        relevo1=0
        valores=valuesf.size()
    if(FA):
        x1=map(valuesa.get(valores-2),0,Rmax,Xmin,Xmax)
        y1=map(valuesf.get(valores-2),0,Pmax,Ymax,Ymin)
        x2=map(valuesa.get(valores-1),0,Rmax,Xmin,Xmax)
        y2=map(valuesf.get(valores-1),0,Pmax,Ymax,Ymin)
        line(x1, y1, x2, y2)
        recorridot.setText(str(recorrido))
        esfuerzot.setText(str(fuerza))
      
    
    else:
        x1=map(valuesd.get(valores-2),0,Rmax,Xmin,Xmax)
        y1=map(valuese.get(valores-2),0,Pmax,Ymax,Ymin)
        x2=map(valuesd.get(valores-1),0,Rmax,Xmin,Xmax)
        y2=map(valuese.get(valores-1),0,Pmax,Ymax,Ymin)
        line(x1, y1, x2, y2)
        recorridot.setText(str(deformacion))
        esfuerzot.setText(str(esfuerzo))
      
    relevo=0
    relevo1+=1
  

  if(PV):
    proporcionalb.setValue(50)
    arduino.analogWrite(pin3,255)
  

  NS=False
  relevo+=1

  delay(100) #demorar 100 ms entre mediciones



def customGUI():
  Rmax=int(defmax.getText())
  Pmax=int(esfmax.getText())
  divisionesx=int(unidades.getText())
  divisionesy=divisionesx  
  rectMode(CORNERS)
  fill(230)
  rect(Xmin-40, Ymin-20, Xmax+20, Ymax+40)

  """ Esto va directamente en los botones
  if(bomba) bombab.setLocalColorScheme(GCScheme.GREEN_SCHEME)
  else bombab.setLocalColorScheme(GCScheme.RED_SCHEME) 
  
  if(valvula) valvulab.setLocalColorScheme(GCScheme.GREEN_SCHEME)  
  else valvulab.setLocalColorScheme(GCScheme.RED_SCHEME)
  
  if(ensayo) ensayob.setLocalColorScheme(GCScheme.GREEN_SCHEME)  
  else ensayob.setLocalColorScheme(GCScheme.RED_SCHEME)
  """
  
  for i in range(divisionesx):
    #print("tamaño: ",valuesr.size())
    ax=int(map(i,0,divisionesx,Xmin,Xmax))
    stroke(150)
    line(ax, Ymax, ax, Ymin)
    textSize(12)
    fill(0, 102, 153)
    textAlign(CENTER,TOP)
    text(i*Rmax/divisionesx, ax, Ymax+5) 
  
  for i in range(divisionesy):
    #print("tamaño: ",valuesr.size())
    ay=int(map(i,0,divisionesy,Ymax,Ymin))
    stroke(150)
    line(Xmin, ay, Xmax, ay)
    textSize(12)
    fill(0, 102, 153)
    textAlign(RIGHT,CENTER)
    text(i*Pmax/divisionesy, Xmin-5, ay)
  

    
  if(CE):
    if(FA):
      for i in range(len(valuesa)):
        #print("tamaño: ",valuesf.size())
        x1=map(valuesa[i],0,Rmax,Xmin,Xmax)
        y1=map(valuesf[i],0,Pmax,Ymax,Ymin)
        x2=map(valuesa[i+1],0,Rmax,Xmin,Xmax)
        y2=map(valuesf[i+1],0,Pmax,Ymax,Ymin)
        line(x1, y1, x2, y2)      
    fill(0, 102, 153)
    textAlign(CENTER,TOP)
    text("Alargamiento (mm)", (Xmin+Xmax)/2, Ymax+30)
    textAlign(CENTER,CENTER)
    pushMatrix()
    translate(Xmin-45,(Ymin+Ymax)/2)
    rotate(-HALF_PI)
    text("Fuerza (kg)", 0, 0)
    popMatrix()
    
  else:
    for i in range(len(valuesd)):
        #print("tamaño: ",valuesd.size())
        x1=map(valuesd[i],0,Rmax,Xmin,Xmax)
        y1=map(valuese[i],0,Pmax,Ymax,Ymin)
        x2=map(valuesd[i+1],0,Rmax,Xmin,Xmax)
        y2=map(valuese[i+1],0,Pmax,Ymax,Ymin)
        line(x1, y1, x2, y2) 
      
    textSize(18)
    fill(0, 102, 153)
    textAlign(CENTER,TOP)
    text("Deformación Específica (mm/mm)", (Xmin+Xmax)/2, Ymax+30)
    textAlign(CENTER,CENTER)
    pushMatrix()
    translate(Xmin-45,(Ymin+Ymax)/2)
    rotate(-HALF_PI)
    text("Esfuerzo (kg/cm2)", 0, 0)
    popMatrix()
  

def serialEvent(serial):

  serialData=serial.read()
  arduino.processInput(serialData)
  if((serialData==arduino.END_SYSEX)and(arduino.storedInputData[0]==arduino.DIFERENCIALMODE)and not NS):
    NS=True
  


def cambiarGrafico(FAR:bool):
  if(not FAR):
    
    label5.setText("ALARGAMIENTO (mm)")
    label6.setText("FUERZA (Kg)")
    label4.setText("FUERZA MAX. \n(kg)")
    label3.setText("ALARGAMIENTO MAX. (mm)")
    esfmax.setText(str(int(esfmax.getText())*float(areatext.getText())))
    defmax.setText(str(int(defmax.getText())*float(longitud.getText())))
    FAB.setText("FUERZA / ALARGAMIENTO")
    FA=True
    
  else:
    label5.setText("DEF. ESP.\n(mm / mm)")
    label6.setText("ESFUERZO\n(Kg / cm2)")
    label4.setText("ESFUERZO MAX.\n(kg / cm2)")
    label3.setText("DEF. ESP. MAX.\n(mm / mm)")
    esfmax.setText(str(int(esfmax.getText())/float(areatext.getText())))
    defmax.setText(str(int(defmax.getText())/float(longitud.getText())))
    FAB.setText("ESFUERZO / DEF. ESP.")
    FA=False
    
    customGUI()
