"""
    autor: @erickgjs99
    file: ejercicios_5.py
    
"""

datos = ((100, 170), (200, 180))

anios = lambda x: x[0]
estatura = lambda x: x[1]

funciones = lambda x: (anios(x)/12.0, estatura(x)/100)


print(list(map(funciones, datos)))