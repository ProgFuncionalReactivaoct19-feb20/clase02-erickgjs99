"""
    autor: @erickgjs99
    file: practica_3.py
Función map
Una función anónima
que permita presentar en otra lista, cada elemento elevado a la tercera potencia."""

lista = [10,2,8,7,5,4,3,11,0, 1]
funciones = lambda x: x**3

print(list(map(funciones, lista)))


