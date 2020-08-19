# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 19:00:05 2020

@author: Florencia Leiva
"""
import math

class Punto: 
    
    # Metodo constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
        
    def string(self):
        print(f'({self.x}, {self.y})')
        
    def cuadrante(self):        
        if ((self.x > 0) and (self.y > 0)):
            print(f'El punto ({self.x}, {self.y}) se sitúa en el primer cuadrante')
        elif ((self.x < 0) and (self.y > 0)):
            print(f'El punto ({self.x}, {self.y}) se sitúa en el segundo cuadrante')
        elif ((self.x < 0) and (self.y < 0)):
            print(f'El punto ({self.x}, {self.y}) se sitúa en el tercer cuadrante')
        elif ((self.x > 0) and (self.y < 0)):
            print(f'El punto ({self.x}, {self.y})se sitúa en el cuarto cuadrante')
        elif ((self.x == 0) and (self.y != 0)):
            print(f'El punto ({self.x}, {self.y})se sitúa sobre el eje Y')
        elif ((self.x != 0) and (self.y == 0)):
            print(f'El punto ({self.x}, {self.y})se sitúa sobre el eje X')
        else:
            print(f'El punto ({self.x}, {self.y}) se sitúa sobre el origen')

            
    def vector(self, p):        
        self.xVector = p.x - self.x
        self.yVector = p.y - self.y
        print(f'El vector resultante es: ({self.xVector}, {self.yVector})')


    def distancia(self, p):
        self.distancia = math.sqrt(((p.x - self.x)**2) - ((p.y - self.y)**2))
        print(f'La distancia entre ({self.x}, {self.y}) y ({p.x}, {p.y}) es {self.distancia}')


class Rectangulo:
    
    # Metodo constructor
    def __init__(self, inicial=0, final=0):
        self.inicial = inicial
        self.final = final
    
 #   def base(self):
        
        
        
        
        
# Creamos los objetos                                   
A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto(0, 0)

# Accedemos a los metodos y atributos
print('Los puntos ingresados son: ')
A.string()
B.string()
C.string()
D.string()
print()

print('Calculamos el cuadrante:')
A.cuadrante()
C.cuadrante()
D.cuadrante()
print()

print('Calculamos los vectores:')
A.vector(B)
B.vector(A)
print()

print('Calculamos la distancia:')
A.distancia(B)
B.distancia(A)
print()
