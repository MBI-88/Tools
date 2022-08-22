# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 08:43:24 2019

@author: Root
"""
# Este programa comprueba si el numero introducido por el teclado es primo

primos = True

print("Introduce un numero para saber si es primo")
numero = abs(int(input()))
for i in range(2, numero):
    if numero % i == 0:
       primos = False
       break
    else:
        continue


if primos:
    print("El numero ", numero, "es primo")
else:
    print("El numero ", numero, " no es primo")

variable = input("Presione una tecla para salir :-> ")



