"""
    autor: @erickgjs99
    file: ejercicios_4.py
    
"""

datos = ((30, 1.79), (25, 1.60), (35, 1.68))

dato = lambda x: x[2]
edad = lambda x: x[1] * 100


print(edad(dato(datos)))