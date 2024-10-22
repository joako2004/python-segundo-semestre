class FiguraGeometrica:
    def __init__(self, ancho, alto):
        
        if self.validar_valores(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print('el valor es erroneo para el ancho')
         
        if self.validar_valores(alto):
            self._alto = alto
        else:
            self._alto = 0
            print('el valor es erroneo para el alto')
        

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self.validar_valores(alto):
            self._alto = alto
        else:
            print('el valor es erroneo para el ancho')
            

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self.validar_valores(ancho):
            self._ancho = ancho
        else:
            print('el valor es erroneo para el alto')
    
    def validar_valores(self, valor):
        return True if 0 < valor < 10 else False








