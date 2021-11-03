
from televisores.tv import TV

class Control:
    def __init__(self):
        pass

    
    def enlazar(self, tv):
        self.tv = tv
        tv.setControl(self)


    def turnOn(self):
        if(self.tv.getEstado()==False):
            self.tv.turnOn()
    

    def turnOff(self):
        if(self.tv.getEstado()==True):
            self.tv.turnOff()
    
    def canalUp(self):
        self.tv.canalUp()

    def canalDown(self):
        self.tv.canalDown()

    def volumenUp(self):
        self.tv.volumenUp()

    def volumenDown(self):
        self.tv.volumenDown()

    def setCanal(self, canal):
        self.tv.setCanal(canal)
    
    def getTV(self):
        return self.tv
    def setTV(self, tv):
        self.tv=tv


