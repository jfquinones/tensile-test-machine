""" =========================================================
 * ====                   WARNING                        ===
 * =========================================================
 * The code in this tab has been generated from the GUI form
 * designer and care should be taken when editing this file.
 * Only add/edit code inside the event handlers i.e. only
 * use lines between the matching comment tags. e.g.

 void myBtnEvents(GButton button) { #_CODE_:button1:12356:
     # It is safe to enter your event code here  
 } #_CODE_:button1:12356:
 
 * Do not rename this tab!
 * =========================================================
 """

# The above code is defining a function called "bombabutton" in Python. This function takes two
# arguments, a GButton object called "source" and a GEvent object called "event". The function
# contains a comment that explains that it is meant to be used directly on buttons.
def bombabutton(source,event): #_CODE_:bombab:945064:
    """ Esto va directamente en los botones
    if(bomba) bombab.setLocalColorScheme(GCScheme.GREEN_SCHEME)
    else bombab.setLocalColorScheme(GCScheme.RED_SCHEME) 
    
    if(valvula) valvulab.setLocalColorScheme(GCScheme.GREEN_SCHEME)  
    else valvulab.setLocalColorScheme(GCScheme.RED_SCHEME)
    
    if(ensayo) ensayob.setLocalColorScheme(GCScheme.GREEN_SCHEME)  
    else ensayob.setLocalColorScheme(GCScheme.RED_SCHEME)
    """
    if(not bomba):
      digitalWrite(pin1,HIGH)
      bombab.setLocalColorScheme(GCScheme.GREEN_SCHEME)
    
    else:
      digitalWrite(pin1,LOW)
      bombab.setLocalColorScheme(GCScheme.RED_SCHEME) 
    
    bomba=~bomba
    #println("BOMBA: ",bomba)
    #println("bombab - GButton >> GEvent." + event + " @ " + millis())
    #_CODE_:bombab:945064:

# The above code is defining a function called "proporcionalslider" that takes in two parameters: a
# GCustomSlider object called "source" and a GEvent object called "event". Within the function, there
# is an if-else statement that checks if the value of a variable called "proporcionalb" is equal to
# 50. If it is, then a text field called "esfuerzot" is cleared and a pin called "pin3" is set to a
# value of 255 using the "analogWrite" function. If the value of "prop
def proporcionalslider(source, event): #_CODE_:proporcionalb:825714:
  if(proporcionalb.getValueF()==50):
  #esfuerzot.setText("")
    analogWrite(pin3,255)  
  
  else:
    #proporcional=map(proporcionalb.getValueF(),0,50,50,0)
    proporcional=map(proporcionalb.getValueF(),50,0,50,0)
    #esfuerzot.setText(str(int(proporcional)))
    analogWrite(pin3,int(proporcional))
  
    #println(int(proporcional))
    #_CODE_:proporcionalb:825714:


# The above code is defining a function called "recorridotext" in Python. The function takes two
# arguments, a GTextField object called "source" and a GEvent object called "event". The function is
# currently empty, but it includes a commented-out line of code that prints a message to the console
# when the function is called.
def recorridotext(source,event): #_CODE_:recorridot:915628:
  pass
  #println("recorridot - GTextField >> GEvent." + event + " @ " + millis())
  #_CODE_:recorridot:915628:


# The above code is a function in Python that handles events for a button called "valvulab". When the
# button is pressed, it checks if a variable called "bomba" is true. If it is true, it toggles the
# state of a variable called "valvula" and sets the color scheme of the button to green if the valve
# is open or red if the valve is closed. If "bomba" is false, it sets the valve to closed and sets the
# color scheme of the button to red. The function also prints the state of the valve and the event
# that
def valvulabutton(source,event):  #_CODE_:valvulab:397701:
    if (bomba):
      if(not valvula):
        digitalWrite(pin2,HIGH)
        valvula=!valvula
        valvulab.setLocalColorScheme(GCScheme.GREEN_SCHEME)  
      else:
        digitalWrite(pin2,LOW)
        valvula=!valvula
        valvulab.setLocalColorScheme(GCScheme.RED_SCHEME)
    else:
      digitalWrite(pin2,LOW)
      valvula=false
      valvulab.setLocalColorScheme(GCScheme.RED_SCHEME)

    #println("PRESION: ",valvula)
    #println("valvulab - GButton >> GEvent." + event + " @ " + millis())
    #_CODE_:valvulab:397701:


# The above code is defining a function called "esfuerzotext" that takes two arguments: a GTextField
# object called "source" and a GEvent object called "event". The function is currently empty, except
# for a commented-out println statement.
def esfuerzotext(source, event): #_CODE_:esfuerzot:417210:
  pass
  #println("presiont - GTextField >> GEvent." + event + " @ " + millis())
 #_CODE_:esfuerzot:417210:




def areat(source, event)> #_CODE_:areatext:549350:
  pass
 #_CODE_:areatext:549350:

def ensayobutton(source, event): #_CODE_:ensayob:488936:
    if(bomba):
      if(valvula):  
        if(not ensayo):
          #digitalWrite(pin3,HIGH)
          #private final int GAIN_1  # ads.setGain(GAIN_TWOTHIRDS)  # 2/3x gain +/- 6.144V  1 bit = 3mV      0.1875mV (default)
          #private final int GAIN_2  # ads.setGain(GAIN_ONE)        # 1x gain   +/- 4.096V  1 bit = 2mV      0.125mV
          #private final int GAIN_3  # ads.setGain(GAIN_TWO)        # 2x gain   +/- 2.048V  1 bit = 1mV      0.0625mV
          #private final int GAIN_4  # ads.setGain(GAIN_FOUR)       # 4x gain   +/- 1.024V  1 bit = 0.5mV    0.03125mV
          #private final int GAIN_5  # ads.setGain(GAIN_EIGHT)      # 8x gain   +/- 0.512V  1 bit = 0.25mV   0.015625mV
          #private final int GAIN_6  # ads.setGain(GAIN_SIXTEEN)    # 16x gain  +/- 0.256V  1 bit = 0.125mV  0.0078125mV
          #adsConfig(DIFERENCIALMODE,GAIN_1)
          ensayob.setLocalColorScheme(GCScheme.GREEN_SCHEME) 
          ensayo=~ensayo
        else:
          print("ENSAYO: APAGADO")
          analogWrite(pin3,255)
          ensayob.setLocalColorScheme(GCScheme.RED_SCHEME)
          guardarArchivo(valuesf,valuesa,valuese,valuesd)
          ensayo=~ensayo
      else:
        ensayob.setLocalColorScheme(GCScheme.RED_SCHEME)
        ensayo=False
    else:
      ensayob.setLocalColorScheme(GCScheme.RED_SCHEME)
      ensayo=False
    #println("ENSAYO: : ",ensayo)
    #_CODE_:ensayob:488936:

def textfield2_change1(source, GEvent event) { #_CODE_:defmax:735874:

  
} #_CODE_:defmax:735874:

def textfield2_change2(source, GEvent event) { #_CODE_:esfmax:360899:

} #_CODE_:esfmax:360899:

public void button1_click1(GButton source, GEvent event) { #_CODE_:refresh:433294:
  
  Rmax=int(defmax.getText())
  Pmax=int(esfmax.getText())
  area=float(areatext.getText())
  area=PI*pow(area,2)/4
  
  if(isInteger(esfmax.getText())){
    if(isInteger(defmax.getText())){
      if(isFloat(areatext.getText())){
        #background(230)
        #createGUI()
        customGUI()
        defmax.setText(str(Rmax))
        esfmax.setText(str(Pmax))
        areatext.setText(str(sqrt(area*4/PI)))
        fill(#FF0000)
        print("Area:",area)
        
      }
      else{
        Mensaje("Error en el Área","Proporciona el valor correspondiente\ndel área de la probeta en mm2")
      }
    }
    else{
      Mensaje("Error en la distancia Maxima","Proporciona un valor entero de distancia max\nentre 0 y 300 mm(para la escala del gráfico)")
    }
  }
  else {
    Mensaje("Error en el Esfuerzo Máximo","Proporciona un valor de Esfuerzo \nMáximo (para la escala del gráfico)")
  }
    
} #_CODE_:refresh:433294:

public void longitudt(source, GEvent event) { #_CODE_:longitud:943048:
  #println("longitud - >> GEvent." + event + " @ " + millis())
} #_CODE_:longitud:943048:

public void descripciont(source, GEvent event) { #_CODE_:descripcion:814678:
  #println("descripcion - >> GEvent." + event + " @ " + millis())
} #_CODE_:descripcion:814678:

public void operadort(source, GEvent event) { #_CODE_:operador:295925:
  #println("operador - >> GEvent." + event + " @ " + millis())
} #_CODE_:operador:295925:

public void unidades_change1(source, GEvent event) { #_CODE_:unidades:251274:
  #println("unidades - >> GEvent." + event + " @ " + millis())
} #_CODE_:unidades:251274:

public void FAButton(GButton source, GEvent event) { #_CODE_:FAB:482523:
  cambiarGrafico(FA)
  #println("FAB - GButton >> GEvent." + event + " @ " + millis())
} #_CODE_:FAB:482523:

public void PVbutton(GButton source, GEvent event) { #_CODE_:PVb:408001:
  PV=true
  ensayob.setLocalColorScheme(GCScheme.ORANGE_SCHEME)
  valvulab.setLocalColorScheme(GCScheme.ORANGE_SCHEME)
  bombab.setLocalColorScheme(GCScheme.ORANGE_SCHEME)
  Mensaje("ENSAYO DETENIDO","Se detuvo el ensayo, por favor libere las mordazas y saque las probetas. \nUna vez retirada la probeta desactive la precarga, y por ultimo la bomba. Luego Puede volver a comenzar")
  #println("PVb - GButton >> GEvent." + event + " @ " + millis())
} #_CODE_:PVb:408001:



# Create all the GUI controls. 
# autogenerated do not edit
public void createGUI(){
  G4P.messagesEnabled(false)
  G4P.setGlobalColorScheme(GCScheme.ORANGE_SCHEME)
  G4P.setCursor(ARROW)
  surface.setTitle("Sketch Window")
  bombab = new GButton(this, 500, 40, 80, 30)
  bombab.setText("BOMBA ON/OFF")
  bombab.setLocalColorScheme(GCScheme.RED_SCHEME)
  bombab.addEventHandler(this, "bombabutton")
  proporcionalb = new GCustomSlider(this, 200, 530, 160, 80, "red_yellow18px")
  proporcionalb.setShowValue(true)
  proporcionalb.setShowLimits(true)
  proporcionalb.setLimits(50, 50, 0)
  proporcionalb.setNbrTicks(25)
  proporcionalb.setShowTicks(true)
  proporcionalb.setNumberFormat(G4P.INTEGER, 0)
  proporcionalb.setOpaque(true)
  proporcionalb.addEventHandler(this, "proporcionalslider")
  recorridot = new GTextField(this, 800, 70, 150, 34, G4P.SCROLLBARS_NONE)
  recorridot.setOpaque(true)
  recorridot.addEventHandler(this, "recorridotext")
  valvulab = new GButton(this, 500, 90, 80, 30)
  valvulab.setText("PRECARGA")
  valvulab.setLocalColorScheme(GCScheme.RED_SCHEME)
  valvulab.addEventHandler(this, "valvulabutton")
  esfuerzot = new GTextField(this, 800, 120, 150, 34, G4P.SCROLLBARS_NONE)
  esfuerzot.setOpaque(true)
  esfuerzot.addEventHandler(this, "esfuerzotext")
  areatext = new GTextField(this, 200, 310, 160, 34, G4P.SCROLLBARS_NONE)
  areatext.setText("1")
  areatext.setOpaque(true)
  areatext.addEventHandler(this, "areat")
  label1 = new GLabel(this, 70, 310, 130, 35)
  label1.setTextAlign(GAlign.CENTER, GAlign.MIDDLE)
  label1.setText("AREA DE LA PROBETA (mm2)")
  label1.setLocalColorScheme(GCScheme.RED_SCHEME)
  label1.setOpaque(true)
  ensayob = new GButton(this, 500, 140, 80, 30)
  ensayob.setText("ENSAYO")
  ensayob.setLocalColorScheme(GCScheme.RED_SCHEME)
  ensayob.addEventHandler(this, "ensayobutton")
  label2 = new GLabel(this, 70, 530, 129, 78)
  label2.setTextAlign(GAlign.CENTER, GAlign.MIDDLE)
  label2.setText("FUERZA")
  label2.setLocalColorScheme(GCScheme.RED_SCHEME)
  label2.setOpaque(true)
  label3 = new GLabel(this, 70, 140, 130, 35)
  label3.setTextAlign(GAlign.CENTER, GAlign.MIDDLE)
  label3.setText("DEFORMACIÓN ESP. MÁX. (mm)")
  label3.setLocalColorScheme(GCScheme.RED_SCHEME)
  label3.setOpaque(true)
  defmax = new GTextField(this, 200, 140, 160, 35, G4P.SCROLLBARS_NONE)
  defmax.setText("30")
  defmax.setOpaque(true)
  defmax.addEventHandler(this, "textfield2_change1")
  label4 = new GLabel(this, 70, 100, 130, 35)
  label4.setTextAlign(GAlign.CENTER, GAlign.MIDDLE)
  label4.setText("ESFUERZO MÁX. (kg/mm2)")
  label4.setLocalColorScheme(GCScheme.RED_SCHEME)
  label4.setOpaque(true)
  esfmax = new GTextField(this, 200, 100, 160, 35, G4P.SCROLLBARS_NONE)
  esfmax.setText("8000")
  esfmax.setOpaque(true)
  esfmax.addEventHandler(this, "textfield2_change2")
  refresh = new GButton(this, 75, 220, 280, 25)
  refresh.setText("CAMBIAR ESCALA")
  refresh.addEventHandler(this, "button1_click1")
  label5 = new GLabel(this, 700, 70, 100, 35)
  label5.setTextAlign(GAlign.CENTER, GAlign.MIDDLE)
  label5.setText("DEFORMACIÓN ESP. (mm/mm)")
  label5.setLocalColorScheme(GCScheme.RED_SCHEME)
  label5.setOpaque(true)
  label6 = new GLabel(this, 700, 120, 100, 35)
  label6.setTextAlign(GAlign.CENTER, GAlign.MIDDLE)
  label6.setText("ESFUERZO (kg/mm2)")
  label6.setLocalColorScheme(GCScheme.RED_SCHEME)
  label6.setOpaque(true)
  label7 = new GLabel(this, 70, 350, 130, 35)
  label7.setTextAlign(GAlign.CENTER, GAlign.MIDDLE)
  label7.setText("LONGITUD INICIAL (mm)")
  label7.setLocalColorScheme(GCScheme.RED_SCHEME)
  label7.setOpaque(true)
  label8 = new GLabel(this, 70, 450, 130, 35)
  label8.setTextAlign(GAlign.CENTER, GAlign.MIDDLE)
  label8.setText("DESCRIPCIÓN DEL ENSAYO")
  label8.setLocalColorScheme(GCScheme.RED_SCHEME)
  label8.setOpaque(true)
  label9 = new GLabel(this, 70, 490, 130, 35)
  label9.setTextAlign(GAlign.CENTER, GAlign.MIDDLE)
  label9.setText("OPERADOR")
  label9.setLocalColorScheme(GCScheme.RED_SCHEME)
  label9.setOpaque(true)
  label10 = new GLabel(this, 70, 70, 290, 30)
  label10.setTextAlign(GAlign.CENTER, GAlign.MIDDLE)
  label10.setText("DATOS PARA EL GRÁFICO")
  label10.setLocalColorScheme(GCScheme.PURPLE_SCHEME)
  label10.setOpaque(true)
  label11 = new GLabel(this, 70, 280, 290, 30)
  label11.setTextAlign(GAlign.CENTER, GAlign.MIDDLE)
  label11.setText("DATOS DE LA PROBETA")
  label11.setLocalColorScheme(GCScheme.PURPLE_SCHEME)
  label11.setOpaque(true)
  label12 = new GLabel(this, 70, 420, 290, 30)
  label12.setTextAlign(GAlign.CENTER, GAlign.MIDDLE)
  label12.setText("DATOS DEL ENSAYO")
  label12.setLocalColorScheme(GCScheme.PURPLE_SCHEME)
  label12.setOpaque(true)
  longitud = new GTextField(this, 200, 350, 160, 35, G4P.SCROLLBARS_NONE)
  longitud.setText("1")
  longitud.setOpaque(true)
  longitud.addEventHandler(this, "longitudt")
  descripcion = new GTextField(this, 200, 450, 160, 35, G4P.SCROLLBARS_NONE)
  descripcion.setOpaque(true)
  descripcion.addEventHandler(this, "descripciont")
  operador = new GTextField(this, 200, 490, 160, 35, G4P.SCROLLBARS_NONE)
  operador.setText("Nombre del Operador")
  operador.setOpaque(true)
  operador.addEventHandler(this, "operadort")
  label13 = new GLabel(this, 70, 180, 130, 35)
  label13.setTextAlign(GAlign.CENTER, GAlign.MIDDLE)
  label13.setText("CANT. DE DIVISIONES (unidades)")
  label13.setLocalColorScheme(GCScheme.RED_SCHEME)
  label13.setOpaque(true)
  unidades = new GTextField(this, 200, 180, 160, 35, G4P.SCROLLBARS_NONE)
  unidades.setText("10")
  unidades.setOpaque(true)
  unidades.addEventHandler(this, "unidades_change1")
  FAB = new GButton(this, 700, 20, 250, 40)
  FAB.setText("Esfuerzo / Def. Esp.")
  FAB.addEventHandler(this, "FAButton")
  PVb = new GButton(this, 70, 640, 290, 60)
  PVb.setText("DETENER")
  PVb.setLocalColorScheme(GCScheme.RED_SCHEME)
  PVb.addEventHandler(this, "PVbutton")
}

# Variable declarations 
# autogenerated do not edit
GButton bombab 
GCustomSlider proporcionalb 
GTextField recorridot 
GButton valvulab 
GTextField esfuerzot 
GTextField areatext 
GLabel label1 
GButton ensayob 
GLabel label2 
GLabel label3 
GTextField defmax 
GLabel label4 
GTextField esfmax 
GButton refresh 
GLabel label5 
GLabel label6 
GLabel label7 
GLabel label8 
GLabel label9 
GLabel label10 
GLabel label11 
GLabel label12 
GTextField longitud 
GTextField descripcion 
GTextField operador 
GLabel label13 
GTextField unidades 
GButton FAB 
GButton PVb 