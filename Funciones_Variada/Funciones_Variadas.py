# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 19:47:26 2019

@author: Root
"""
"""Este programa realiza varias operaciones numericas """
import math as ma
import sys as system
# Seccion de funciones
def Raiz_Cubica(x):
    tem= float(round(1/3,4))
    raiz= float(round( x**tem,3))
    return raiz
def Area_Circulo(r):
    Area=float(round( 2*ma.pi*(r**2),3))
    return Area
    
def Farenheit_Centigrado(f):
    C=float(round(5/9*(f-32),3))
    return C
def Centigrados_Farenheit(c):
    F=float(round(9/5*c+32,3))
    return F
def Radianes_Grados(r):
    G=float(round((r*360)/(2*ma.pi),3))
    return G
def Grados_Radianes(g):
    R=float(round((g*2*ma.pi)/360,3))
    return R
#Programa principal
print("***********Hola este programa te ayudara a resolver operaciones matematicas**********")
print("*************************************************************************************")
print("    *****************************************************************************    ")
opcion =""
while opcion !="a":
    print("a)Calculo de la raiz cubica ")
    print("b)Calculo del area de un circulo")
    print("c)Convercion de grados farenheit a centigrados")
    print("d)Convercion de grados centigrados a farenheit")
    print("e)Convercion de radianes en grados")
    print("f)Convercion de grados en radianes")
    print("Para salir use 'x'")
    op=input("Elige una opcion :-> ")
    if op=="a":
        print("Calculo de la Raiz Cubica: ")
        valor= float((input("-> : ")))
        respuesta= Raiz_Cubica(valor)
        print("Resultado : ",respuesta)
        print("\n") 
    elif op=="b":
        print("Dame el radio en metros: ")
        valor1=float((input("-> : ")))
        respuesta1=Area_Circulo(valor1)
        print("Resultado : ",respuesta1,"m2")
        print("\n") 
    elif op=="c" :
        print("Dame el valor en farenheit: ")
        valor2=float((input("-> : ")))
        respuesta2= Farenheit_Centigrado(valor2)
        print("Resultado : ",respuesta2,"grados")
        print("\n") 
    elif op=="d" :
        print("Dame el valor en grados: ") 
        valor3=float((input("-> : ")))
        respuesta3=Centigrados_Farenheit(valor3)
        print("Resultado : ",respuesta3,"farenheit")
        print("\n")
    elif op=="e" :
        print("Dame el valor en radianes: ")
        valor4=float((input("-> : ")))
        respuesta4=Radianes_Grados(valor4)
        print("Resultado : ",respuesta4,"grados")
        print("\n")
    elif op=="f" :
        print("Dame el valor en grados: ")
        valor5=float((input("-> : ")))
        respuesta5=Grados_Radianes(valor5)
        print("Resultado : ",respuesta5,"radianes")
        print("\n")
    elif op=="x":
        print("Saliendo del programa....")
        system.exit()
    else:
        print("Puso una opcion incorrecta")
        print("\n")