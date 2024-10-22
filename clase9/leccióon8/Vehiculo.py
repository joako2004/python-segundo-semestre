class Vehiculo:
    def __init__(self, color, ruedas):
        self._color = color
        self._ruedas = ruedas
        
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color
        
    @property
    def ruedas(self):
        return self._ruedas
    
    @ruedas.setter
    def ruedas(self, ruedas):
        self._ruedas = ruedas
    
    def __str__(self):
        return f'{self._color}, {self._ruedas}' 

class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    
    def __str__(self):
        return f'{self.velocidad}, {super().__str__()}'

class Bicileta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self._tipo = tipo
    
    def __str__(self):
        return f'{self._tipo}, {super().__str__()}'

vehiculo1 = Vehiculo('rojo', 4)
print(vehiculo1)

auto1 = Auto('azul', 2, 100)
print(auto1)

bicileta1 = Bicileta('verde', 4, 'montaña')
print(bicileta1)