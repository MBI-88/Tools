# -*- coding: utf-8 -*-
""" Este programa calcula la cantidad de dias de un año"""
"""Autor:Root"""
import sys as syst
#Areas de Funciones
def Año_Bisiesto(a):
    bisiesto=366
    nobisiesto=365
    divisor0=4
    divisor1=100
    divisor2=400
    if a % divisor0 == 0:
        if a % divisor1 != 0:
            return bisiesto
        else:
            if a % divisor2 == 0:
                return bisiesto
            else:
                return nobisiesto
    else:
        return nobisiesto
#Programa principal
print("*****Calculo de los dias de un año*****")
op=""
while op != "a":
    try:
      año = int(input(" Ingrese el año:-> "))
    except:
        print(" Introdujo caracteres alfabeticos ")
        print("\n")
    respuesta = Año_Bisiesto(año)
    print(" El año tiene",respuesta,"dias ")
    salida= input(" Para salir pulse 'x',para continuar pulse cualquier otro boton :-> ")
    if salida=="x":
        print(" Saliendo del programa...")
        syst.exit()
    else:
        continue

