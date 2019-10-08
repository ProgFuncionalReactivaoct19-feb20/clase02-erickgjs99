"""
    autor: @erickgjs99
    file: practica_2.py
    Desarrollar una función anónima que permita retornar la siguiente salida, ejemplo:
    CUENCA capital de AZUAY
"""
mensaje = lambda cad, cad_2: "%s Capital de %s" % (cad.upper(), cad_2.upper())

print(mensaje("Cuenca", "Azuay"))