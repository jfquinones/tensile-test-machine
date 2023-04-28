import csv
import logging
from datetime import datetime
from serial import Serial

Mensajes=0 #GWindow  
label20,label21 = 0,0 #GLabel 

class Arduino():
  arduinoPort= Serial()
  
  """
  * Internal class used by the Arduino class to parse the Firmata protocol.
  """

  """
  * Constant to set a 
   to input mode (in a call to pinMode()).
  """
  INPUT = 0 
  """
  * Constant to set a pin to output mode (in a call to pinMode()).
  """
  OUTPUT = 1 
  """
  * Constant to set a pin to analog mode (in a call to pinMode()).
  """
  ANALOG = 2 
  """
  * Constant to set a pin to PWM mode (in a call to pinMode()).
  """
  PWM = 3 
  """
  * Constant to set a pin to servo mode (in a call to pinMode()).
  """
  SERVO = 4 
  """
  * Constant to set a pin to shiftIn/shiftOut mode (in a call to pinMode()).
  """
  SHIFT = 5 
  """
  * Constant to set a pin to I2C mode (in a call to pinMode()).
  """
  I2C = 6 

  """
  * Constant to write a high value (+5 volts) to a pin (in a call to
  * digitalWrite()).
  """
  LOW = 0 
  """
  * Constant to write a low value (0 volts) to a pin (in a call to
  * digitalWrite()).
  """
  HIGH = 1 

  MAX_DATA_BYTES = 4096 
    
  I2C_WRITE=int("00000000",2) 
  I2C_READ=int("00001000",2) 
  I2C_READ_CONTINUOUSLY=int("00010000",2) 
  I2C_STOP_READING=int("00011000",2) 

  DIGITAL_MESSAGE        = 0x90  # send data for a digital port
  ANALOG_MESSAGE         = 0xE0  # send data for an analog pin (or PWM)
  REPORT_ANALOG          = 0xC0  # enable analog input by pin #
  REPORT_DIGITAL         = 0xD0  # enable digital input by port
  SET_PIN_MODE           = 0xF4  # set a pin to INPUT/OUTPUT/PWM/etc
  REPORT_VERSION         = 0xF9  # report firmware version
  SYSTEM_RESET           = 0xFF  # reset from MIDI
  START_SYSEX            = 0xF0  # start a MIDI SysEx message
  END_SYSEX              = 0xF7  # end a MIDI SysEx message

  # extended command set using sysex (0-127/0x00-0x7F)
  """ 0x00-0x0F reserved for user-defined commands  """
  SERVO_CONFIG           = 0x70  # set max angle, minPulse, maxPulse, freq
  STRING_DATA            = 0x71  # a string message with 14-bits per char
  SHIFT_DATA             = 0x75  # a bitstream to/from a shift register
  I2C_REQUEST            = 0x76  # send an I2C read/write request
  I2C_REPLY              = 0x77  # a reply to an I2C read request
  I2C_CONFIG             = 0x78  # config I2C settings such as delay times and power pins
  EXTENDED_ANALOG        = 0x6F  # analog write (PWM, Servo, etc) to any pin
  PIN_STATE_QUERY        = 0x6D  # ask for a pin's current mode and value
  PIN_STATE_RESPONSE     = 0x6E  # reply with pin's current mode and value
  CAPABILITY_QUERY       = 0x6B  # ask for supported modes and resolution of all pins
  CAPABILITY_RESPONSE    = 0x6C  # reply with supported modes and resolution
  ANALOG_MAPPING_QUERY   = 0x69  # ask for mapping of analog to pin numbers
  ANALOG_MAPPING_RESPONSE= 0x6A  # reply with mapping info
  REPORT_FIRMWARE        = 0x79  # report name and version of the firmware
  SAMPLING_INTERVAL      = 0x7A  # set the poll rate of the main loop
  SYSEX_NON_REALTIME     = 0x7E  # MIDI Reserved for non-realtime messages
  SYSEX_REALTIME         = 0x7F  # MIDI Reserved for realtime messages

  # ADS1115 Commands
  ADS1115 = 0x72 
  CONFIG=0 
  SINGLEMODE=1 
  DIFERENCIALMODE=2 
  GAIN_1=1   # ads.setGain(GAIN_TWOTHIRDS)   # 2/3x gain +/- 6.144V  1 bit = 3mV      0.1875mV (default)
  GAIN_2=2   # ads.setGain(GAIN_ONE)         # 1x gain   +/- 4.096V  1 bit = 2mV      0.125mV
  GAIN_3=3   # ads.setGain(GAIN_TWO)         # 2x gain   +/- 2.048V  1 bit = 1mV      0.0625mV
  GAIN_4=4   # ads.setGain(GAIN_FOUR)        # 4x gain   +/- 1.024V  1 bit = 0.5mV    0.03125mV
  GAIN_5=5   # ads.setGain(GAIN_EIGHT)       # 8x gain   +/- 0.512V  1 bit = 0.25mV   0.015625mV
  GAIN_6=6   # ads.setGain(GAIN_SIXTEEN)     # 16x gain  +/- 0.256V  1 bit = 0.125mV  0.0078125mV
  #


  ESCRITURADIGITAL    =3 
  ESCRITURAANALOGICA  =4 
  PINMODO             =5 
  LECTURADIGITAL      =6 
  LECTURAANALOGICA    =7 

  waitForData = 0 
  executeMultiByteCommand = 0 
  multiByteChannel = 0 
  storedInputData = [] #new int[MAX_DATA_BYTES] 
  storedInputData1 = [] #new byte[8] 
  parsingSysex=False 
  sysexBytesRead=0 

  digitalOutputData = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] 
  digitalInputData  = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] 
  analogInputData   = [ 0, 0, 0, 0, 0]

  MAX_PINS = 128 

  ipinModes = []      #new int[MAX_PINS] 
  analogChannel = []  #new int[MAX_PINS] 
  pinModes = []        #new int[MAX_PINS] 

  inBuffer=[]

  majorVersion = 0 
  minorVersion = 0 
  sumas1=0
  sumas2=0
  cants1=0
  cants2=0 
  promedios1=0,0
  promedios2=0,0


  
  def __init__(self,
      VIR:int=3470,
      VIF:int=2200,
      Debug:bool=False,
      port_baudrate:int = 57000,
      port_name:str|None = "COM4", #Select the corresponding Arduino Port
      port_timeout: int = 1):
    self.VIR = VIR
    self.VIF = VIF
    self.DEBUG = Debug
    print(port_baudrate)
    self.arduinoPort.baudrate = port_baudrate
    self.arduinoPort.timeout = port_timeout
    self.arduinoPort.port = port_name

    if not self.arduinoPort.is_open:self.arduinoPort.open()
    self.arduinoPort.write(0xFF)
    
    


  def digitalRead(self,pin): 
      return (self.digitalInputData[pin >> 3] >> (pin & 0x07)) & 0x01 
    

  def analogRead(self,pin): 
      return self.analogInputData[pin] 
    
  def writeSYSEX(self,command,data:list):
    array=[self.START_SYSEX,command]
    #self.arduinoPort.write(chr(self.START_SYSEX).encode('utf-8'))
    #self.arduinoPort.write(chr(command).encode())
    array+=data
    array+=[self.END_SYSEX]
    self.arduinoPort.write(bytearray(array))
    #for d in data:
      #self.arduinoPort.write(chr(d).encode())
      #self.arduinoPort.write(chr(self.END_SYSEX).encode())

    

  def pinMode(self,pin,mode):
      self.writeSYSEX(self.PINMODO,data=[pin,mode])
      """ self.arduinoPort.write(self.START_SYSEX) 
      self.arduinoPort.write(self.PINMODO) 
      self.arduinoPort.write(pin) 
      self.arduinoPort.write(mode) 
      self.arduinoPort.write(self.END_SYSEX)  """

  def digitalWrite(self,pin, value):
      #if (value == 0)  value=0 
      #else  value=1 
      self.writeSYSEX(self.ESCRITURADIGITAL,data=[pin,value])  
      """ self.arduinoPort.write(self.START_SYSEX) 
      self.arduinoPort.write(self.ESCRITURADIGITAL) 
      self.arduinoPort.write(pin) 
      self.arduinoPort.write(value) 
      self.arduinoPort.write(self.END_SYSEX) """


  def analogWrite(self,pin, value):
      self.writeSYSEX(self.ESCRITURAANALOGICA,data=[pin,value & 0x7F,value >> 7])
      """ self.arduinoPort.write(self.START_SYSEX)     
      self.arduinoPort.write(self.ESCRITURAANALOGICA) 
      self.arduinoPort.write(pin) 
      self.arduinoPort.write(value & 0x7F) 
      self.arduinoPort.write(value >> 7) 
      self.arduinoPort.write(self.END_SYSEX)  """

  def processInput(self,inputData): 

      if (parsingSysex):
        if (inputData == self.END_SYSEX):
          parsingSysex = False 
          if(self.storedInputData[0]==self.SINGLEMODE):
            self.adsSingleMode(self.storedInputData) 
          elif(self.storedInputData[0]==self.DIFERENCIALMODE):
            self.adsDiferencialMode(self.storedInputData)
          elif(self.storedInputData[0]==self.LECTURADIGITAL):
            self.setlectdigital(self.storedInputData) 
          elif(self.storedInputData[0]==self.LECTURAANALOGICA):
            self.setlectanalogica(self.storedInputData)
          else: 
            self.storedInputData[sysexBytesRead] = inputData 
            sysexBytesRead+=1
        else:
          if(inputData < 0xF0):
            command = inputData & 0xF0 
            multiByteChannel = inputData & 0x0F 
          else:
            command = inputData 
            # commands in the 0xF* range don't use channel data
          
          if command == self.DIGITAL_MESSAGE: pass     
          if command == self.ANALOG_MESSAGE:
          
            while (self.arduinoPort.in_waiting > 0):
              inBuffer = self.arduinoPort.read_until(size=2)#readBytesUntil(129) 
              self.analogInputData[multiByteChannel]=(inBuffer[0]+inBuffer[1]<<7) 
            
          if command == self.START_SYSEX:
            parsingSysex = True 
            sysexBytesRead = 0
        
    
  def adsConfig(self,modo,ganancia):
    self.arduinoPort.write(self.START_SYSEX) 
    self.arduinoPort.write(self.ADS1115) 
    self.arduinoPort.write(modo) 
    self.arduinoPort.write(ganancia) 
    self.arduinoPort.write(self.END_SYSEX) 

  def adsSingleMode(self,inputdata:list):
    sensor1=(inputdata[1]+inputdata[2]<<7+inputdata[3]<<14) 
    sensor2=(inputdata[4]+inputdata[5]<<7+inputdata[6]<<14) 

  def adsDiferencialMode(self,inputdata:list):
    sensor1=((inputdata[1])+(inputdata[2]<<7)+(inputdata[3]<<14)) 
    sensor2=((inputdata[4])+(inputdata[5]<<7)+(inputdata[6]<<14)) 
    recorrido=map(float(sensor1), self.VIR, 24936, 0, 300) 
    fuerza=map(float(sensor2), self.VIF, 25330, 0, 8000) 
    self.cants1+=1

  def setlectanalogica(self,values:list):
    self.analogInputData[values[0]]=values[1]+values[2]<<7 

  def setlectdigital(self,values:list):
    self.digitalInputData[values[0]]=values[1] 

  def writeBytes(self,data):
    pass
""" def Mensaje(a:str,b:str):
  Mensajes = GWindow.getWindow(this, "Advertencia", 500, 500, 400, 200, JAVA2D) 
  Mensajes.noLoop() 
  Mensajes.setActionOnClose(G4P.CLOSE_WINDOW) 
  Mensajes.addDrawHandler(this, "win_draw1") 
  label20 = new GLabel(Mensajes, 0, 0, 400, 20) 
  label20.setLocalColorScheme(GCScheme.PURPLE_SCHEME) 
  label20.setOpaque(true) 
  label20.setTextAlign(GAlign.CENTER, GAlign.MIDDLE) 
  label20.setFont(labelfont) 
  label20.setText(a) 
  
  label21 = new GLabel(Mensajes, 0, 20, 400, 180) 
  label21.setLocalColorScheme(GCScheme.ORANGE_SCHEME) 
  label21.setOpaque(true) 
  label21.setTextAlign(GAlign.CENTER, GAlign.MIDDLE) 
  label21.setFont(labelfont) 
  label21.setText(b) 
  
  Mensajes.loop()  """


def guardarArchivo(a:list,b:list,c:list,d:list):
  """
  The function "guardarArchivo" takes four lists as input and creates a new table with the data from
  the lists.
  
  :param a: The parameter "a" is a list containing values for force (Fuerza)
  :param b: The parameter "b" is a list that contains values for elongation (Alargamiento)
  :param c: The parameter "c" is a list that contains values for the strain or stress (Esfuerzo)
  :param d: The parameter "d" is a list containing the values of specific strai
  """
  datos=[] #new Table() 
  """ datos.addColumn("Fuerza") 
  datos.addColumn("Alargamiento") 
  datos.addColumn("Esfuerzo") 
  datos.addColumn("Def. Esp.")  """
  for i in range(0,len(a),1):
     datos += [[a[i],b[i],c[i],d[i]]] 
     """ TableRow newrow=datos.addRow() 
     newrow.setFloat("Fuerza",a.get(i)) 
     newrow.setFloat("Alargamiento",b.get(i)) 
     newrow.setFloat("Esfuerzo",c.get(i)) 
     newrow.setFloat("Def. Esp.",d.get(i))  """
  root='/home/pi/Document/Ensayos/'
  now=datetime.now()
  date="-".join([now.year,now.month,now.day])
  time=":".join([now.hour,now.minute,now.second])
  description=""#descripcion.getText()
  csv_writer=csv.writer('home/pi/Document/Ensayos/' + date + ' ' + time + ' - '+ description + '.csv')
  csv_writer.writerows()
  
  #exec("/home/pi/sketchbook/maquinadetraccion/GdriveSync.sh") 
