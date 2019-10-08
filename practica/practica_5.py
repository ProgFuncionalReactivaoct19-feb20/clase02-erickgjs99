"""
    autor: @erickgjs99
    file: practica_5.py
    Use:
    Función map
    Dos funciones anónimas
    que permita presentar en otra lista; para las primeras posiciones la raiz cuadrada,
    para las segundas posiciones el cuadrado del número
"""
import math

lista = [(10,2), (8,7), (5,4), (3,11), (10,11)]

operacion = lambda x: x[0]
operacion_2 = lambda x: x[1]
funcion = lambda x: (math.sqrt(operacion(x)), operacion_2(x)**2)

print(list(map(funcion, lista)))






