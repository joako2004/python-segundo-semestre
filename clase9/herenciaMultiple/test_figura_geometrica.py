from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print('creacion de la clase cuadrado '.center(50, '-'))
cuadrado1 = Cuadrado(5, "azul")
print(cuadrado1.alto)
print(cuadrado1.ancho)
print(cuadrado1.calcularArea())

print('creacion de la clase rectangulo '.center(50, '-'))
rectangulo1 = Rectangulo(5, 4, "rojo")
print(rectangulo1.alto)
print(rectangulo1.ancho)
print(rectangulo1.calcularArea())
