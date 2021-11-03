

class TV:

    numTV=0

    def __init__(self, marca, estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        TV.numTV = TV.numTV +1
    
    def getMarca(self):
        return self._marca
    def setMarca(self, marca):
        self._marca=marca

    def getControl(self):
        return self._control
    def setControl(self, control):
        self._control=control

    def getPrecio(self):
        return self._precio
    def setPrecio(self, precio):
        self._precio=precio

    def getVolumen(self):
        return self._volumen

    def setVolumen(self, volumen):
        if(self.getVolumen()<=7 and self.getVolumen()>=0 and self.getEstado()==True):
            self._volumen=volumen

    def getCanal(self):
        return self._canal
    def setCanal(self, canal):
        if(self.getCanal<=120 and self.getCanal()>=1 and self.getEstado()==True):
            self._canal=canal

    def turnOn(self):
        self._estado=True
    def turnOff(self):
        self._estado=False
    
    def getEstado(self):
        return self._estado

    
    def canalUp(self):
        if(self.getCanal()<120 and self.getEstado()==True):
            self._canal = self._canal+1
        return
    
    def canalDown(self):
        if(self.getCanal()>1 and self.getEstado()==True):
            self._canal = self._canal-1
        return

    def volumenUp(self):
        if(self.getVolumen()<7 and self.getEstado()==True):
            self._volumen = self._volumen+1
    
    def volumenDown(self):
        if(self.getVolumen()>0 and self.getEstado()==True):
            self._volumen = self._volumen-1




    @classmethod
    def getNumTV(cls):
        return cls.numTV



# Otro requerimiento en nuestros televisores es que implementemos el cambio de canal y el
# cambio de volumen, para esto definimos los métodos canalUp y canalDown, que se encargaran
# de cambiar el canal aumentándolo o disminuyéndolo, y los métodos volumenUp, y
# volumenDown que se encargan de cambiar el volumen aumentándolo o disminuyéndolo.
# Una de las dos limitaciones que se afronta en estos televisores, es que los canales disponibles
# solo van del canal 1 al canal 120 y para cambiar de canal necesariamente debe estar encendido
# el televisor, por obvias razones, así que en este diseño que se está construyendo, se debe
# implementar las condiciones que sean necesarias para representar lo anterior. También ocurre lo
# mismo con el volumen, esta ira de 0 a 7 y para que este cambie debe estar encendido el
# televisor. Para ambos casos, cambio de canal o subir volumen, en caso de un valor por encima o
# debajo de sus valores límites o que no se cumpla que esté encendido, no se debe hacer nada.



