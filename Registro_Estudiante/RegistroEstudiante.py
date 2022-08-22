# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 10:35:49 2019

@author: Root
"""
#Este programa realiza la introduccion de el promedio de notas de los estudiantes de una univercidad y calcula su indice academico general despues de  graduado
import sqlite3 as conn
import sys as syst
#Clases
class Estudiante:
    def __init__(self,nombre,apellido1,apellido2,año1,año2,año3,año4,año5,año6):
        self.nombre = nombre.title()
        self.apellido1 = apellido1.title()
        self.apellido2 = apellido2.title()
        self.año1 = float(año1)
        self.año2 = float(año2)
        self.año3 = float(año3)
        self.año4 = float(año4)
        self.año5 = float(año5)
        self.año6 = float(año6)
    def Tupla (self):
        self.tupla =(self.nombre,self.apellido1,self.apellido2,self.año1,self.año2,self.año3,self.año4,self.año5,self.año6)
        return self.tupla

class Listado:
    def __init__(self):
        self.estudiante=[]
        self.base_datos= "Estudiante.db"
    def Agregar_Objeto(self,p):
         resultado = self.estudiante.append(p)
         return resultado
    def Crear_Basededatos(self):
        conexion = conn.connect(self.base_datos)
        puntero = conexion.cursor()
        sql='''CREATE TABLE IF NOT EXISTS BASE(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE TEXT ,
        APELLIDO_1 TEXT,
        APELLIDO_2 TEXT,
        PRIMER_AÑO INTEGER,
        SEGUNDO_AÑO INTEGER,
        TECER_AÑO INTEGER,
        CUARTO_AÑO INTEGER,
        QUINTO_AÑO INTEGER,
        SEXTO_AÑO INTEGER
        )'''
        try:
           puntero.execute(sql)
           puntero.close()
           conexion.commit()
           conexion.close()
          
        except :
            puntero.close()
            conexion.close()
            print("No se pudo crear base")
            syst.exit()
            
    def Insertar_Basededatos(self):
        conexion = conn.connect(self.base_datos)
        puntero = conexion.cursor()
        sql_insert= "INSERT INTO BASE VALUES(NULL,?,?,?,?,?,?,?,?,?)"
        try:
            puntero.executemany(sql_insert,self.estudiante)
            puntero.close()
            conexion.commit()
            conexion.close()
            
        except:
            puntero.close()
            conexion.close()
            print("Error al insertar datos")
    def Actualizar_BASEdedatos_Nombre(self):
        Nnombre = input("Nombre :__").title()
        while  not Nnombre.isalpha():
            Nnombre =  input("Nombre :__").title()
        while True:    
            try:
              ID=int(input("Dame ID:__"))
              break
            except:
                 print("Introdujo informacion incorrecta:...")
        nombre=(Nnombre,ID)        
        conexion = conn.connect(self.base_datos)
        sql_actualiza= "UPDATE BASE SET NOMBRE=? WHERE ID=?"
        puntero = conexion.cursor()
        try:
            puntero.execute(sql_actualiza,nombre)
            puntero.close()
            conexion.commit()
            conexion.close()
            
        except:
            puntero.close()
            conexion.close()
            print("Error al actualizar la base de datos")
    def Actualizar_BASEdedatos_Apellido_1(self):
        Napellido1 = input("Apellido_1 :__").title()
        while  not Napellido1.isalpha():
            Napellido1 = input("Apellido_1 :__").title()
        while True:    
            try:
              ID=int(input("Dame ID:__"))
              break
            except:
                 print("Introdujo informacion incorrecta:...")
        nombre=(Napellido1,ID) 
        conexion = conn.connect(self.base_datos)
        sql_actualiza= "UPDATE BASE SET Apellido_1=? WHERE ID=?"
        puntero = conexion.cursor()
        try:
            puntero.execute(sql_actualiza,nombre)
            puntero.close()
            conexion.commit()
            conexion.close()
            
        except:
            puntero.close()
            conexion.close()
            print("Error al actualizar la base de datos")
    def Actualizar_BASEdedatos_Apellido_2(self):
        Napellido2 = input("Apellido_2 :__").title()
        while  not Napellido2.isalpha():
            Napellido2 = input("Apellido_2 :__").title()
        while True:    
            try:
              ID=int(input("Dame ID:__"))
              break
            except:
                 print("Introdujo informacion incorrecta:...")
        nombre=(Napellido2,ID) 
        conexion = conn.connect(self.base_datos)
        sql_actualiza= "UPDATE BASE SET Apellido_2=? WHERE ID=?"
        puntero = conexion.cursor()
        try:
            puntero.execute(sql_actualiza,nombre)
            puntero.close()
            conexion.commit()
            conexion.close()
            
        except:
            puntero.close()
            conexion.close()
            print("Error al actualizar la base de datos")
    def Actualizar_BASEdedatos_Año_1(self):
        while True:    
            try:
              Naño1=float(input("Promedio de año_1:__"))
              break
            except:
                 print("Introdujo letras,repita la informacion:...")
        while True:    
            try:
              ID=int(input("Dame ID:__"))
              break
            except:
                 print("Introdujo informacion incorrecta:...")
        nombre=(Naño1,ID)
        conexion = conn.connect(self.base_datos)
        sql_actualiza= "UPDATE BASE SET PRIMER_AÑO=? WHERE ID=?"
        puntero = conexion.cursor()
        try:
            puntero.execute(sql_actualiza,nombre)
            puntero.close()
            conexion.commit()
            conexion.close()
            
        except:
            puntero.close()
            conexion.close()
            print("Error al actualizar la base de datos")
    def Actualizar_BASEdedatos_Año_2(self):
        while True:    
            try:
              Naño2=float(input("Promedio de año_2:__"))
              break
            except:
                 print("Introdujo letras,repita la informacion:...")
        while True:    
            try:
              ID=int(input("Dame ID:__"))
              break
            except:
                 print("Introdujo informacion incorrecta:...")
        nombre=(Naño2,ID)
        conexion = conn.connect(self.base_datos)
        sql_actualiza= "UPDATE BASE SET SEGUNDO_AÑO=? WHERE ID=?"
        puntero = conexion.cursor()
        try:
            puntero.execute(sql_actualiza,nombre)
            puntero.close()
            conexion.commit()
            conexion.close()
            
        except:
            puntero.close()
            conexion.close()
            print("Error al actualizar la base de datos")
    def Actualizar_BASEdedatos_Año_3(self):
        while True:    
            try:
              Naño3=float(input("Promedio de año_3:__"))
              break
            except:
                 print("Introdujo letras,repita la informacion:...")
        while True:    
            try:
              ID=int(input("Dame ID:__"))
              break
            except:
                 print("Introdujo informacion incorrecta:...")
        nombre=(Naño3,ID)
        conexion = conn.connect(self.base_datos)
        sql_actualiza= "UPDATE BASE SET TERCER_AÑO=? WHERE ID=?"
        puntero = conexion.cursor()
        try: 
            puntero.execute(sql_actualiza,nombre)
            puntero.close()
            conexion.commit()
            conexion.close()
            
        except:
            puntero.close()
            conexion.close()
            print("Error al actualizar la base de datos")
    def Actualizar_BASEdedatos_Año_4(self):
        while True:    
            try:
              Naño4=float(input("Promedio de año_4:__"))
              break
            except:
                 print("Introdujo letras,repita la informacion:...")
        while True:    
            try:
              ID=int(input("Dame ID:__"))
              break
            except:
                 print("Introdujo informacion incorrecta:...")
        nombre=(Naño4,ID)
        conexion = conn.connect(self.base_datos)
        sql_actualiza= "UPDATE BASE SET CUARTO_AÑO=? WHERE ID=?"
        puntero = conexion.cursor()
        try: 
            puntero.execute(sql_actualiza,nombre)
            puntero.close()
            conexion.commit()
            conexion.close()
            
        except:
            puntero.close()
            conexion.close()
            print("Error al actualizar la base de datos")
    def Actualizar_BASEdedatos_Año_5(self):
        while True:    
            try:
              Naño5=float(input("Promedio de año_5:__"))
              break
            except:
                 print("Introdujo letras,repita la informacion:...")
        while True:    
            try:
              ID=int(input("Dame ID:__"))
              break
            except:
                 print("Introdujo informacion incorrecta:...")
        nombre=(Naño5,ID)
        conexion = conn.connect(self.base_datos)
        sql_actualiza= "UPDATE BASE SET QUINTO_AÑO=? WHERE ID=?"
        puntero = conexion.cursor()
        try:
            puntero.execute(sql_actualiza,nombre)
            puntero.close()
            conexion.commit()
            conexion.close()
            
        except:
            puntero.close()
            conexion.close()
            print("Error al actualizar la base de datos")
    def Actualizar_BASEdedatos_Año_6(self):
        while True:    
            try:
              Naño6=float(input("Promedio de año_6:__"))
              break
            except:
                 print("Introdujo letras,repita la informacion:...")
        while True:    
            try:
              ID=int(input("Dame ID:__"))
              break
            except:
                 print("Introdujo informacion incorrecta:...")
        nombre=(Naño6,ID)
        conexion = conn.connect(self.base_datos)
        sql_actualiza= "UPDATE BASE SET SEXTO_AÑO=? WHERE ID=?"
        puntero = conexion.cursor()
        try:
            puntero.execute(sql_actualiza,nombre)
            puntero.close()
            conexion.commit()
            conexion.close()
            
        except:
            puntero.close()
            conexion.close()
            print("Error al actualizar la base de datos")        
    def DELETE_BASEdedatos(self):
         conexion = conn.connect(self.base_datos)
         sql_delete="DELETE FROM BASE WHERE ID=?"
         while True:    
            try:
              ID=int(input("Dame ID:__"))
              valor=str(ID)
              break
            except:
                 print("Introdujo informacion incorrecta:...")
         puntero = conexion.cursor()
         try:
            puntero.execute(sql_delete,valor)
            puntero.close()
            conexion.commit()
            conexion.close()
            
         except:
            puntero.close()
            conexion.close()
            print("Error al eliminar dato en la base")
    def Mostrar_Datos(self):
        conexion = conn.connect(self.base_datos)
        sql_mostrar="SELECT * FROM BASE"
        puntero = conexion.cursor()
        try:
            puntero.execute(sql_mostrar)
            valores=puntero.fetchall()
            puntero.close()
            conexion.commit()
            for valor in valores:
                print(valor)
            conexion.close() 
        except:
            puntero.close()
            conexion.close()
            print("Error en la lectura de la base de datos")
        
    def DELETE_BASEdedatosall(self):
        conexion = conn.connect(self.base_datos)
        sql_delete= "DELETE FROM BASE "
        puntero = conexion.cursor()
        try:
            puntero.execute(sql_delete)
            puntero.close()
            conexion.commit()
            conexion.close()
            print("Base de datos eliminada")
            
        except:
            puntero.close()
            conexion.close()
            print("Error al eliminar base de datos")
#Programa Principal
print("****Bienvenido a el Registro de estudiantes :****")
op =""
lista= Listado()
lista.Crear_Basededatos()
while op !="a":
    print("a)Ingresar nuevo estudiante :")
    print("b)Ver archivo de estudiantes :")
    print("c)Actualizar base de datos:")
    print("d)Eliminar estudiante de base de datos:")
    print("e)Borrar base de datos")
    print("Salir presione [x]...")
    opcion = input("Inserte opcion :__")
    if opcion == "a":
        print("Ingrese los datos que se pide a continuacion :")
        Anombre = input("Nombre :__")
        while  not Anombre.isalpha():
            Anombre = input("Nombre :__")
        
        Aapellido1 = input("Apellido1:__")
        while not Aapellido1.isalpha():
            Aapellido1 = input("Apellido1:__")

        Aapellido2=input("Apellido_2:__") 
        while not Aapellido2.isalpha():
            Aapellido2 = input("Apellido2:__")
        while True:    
            try:
              Aaño1=float(input("Promedio de año_1:__"))
              break
            except:
                 print("Introdujo letras,repita la informacion:...")

        while True:
            try:
              Aaño2=float(input("Promedio de año_2:__"))
              break
            except:
                 print("Introdujo letras,repita la informacion:...")
          
        while True:
            try:
                Aaño3=float(input("Promedio de año_3:__"))

                break
            except:
                print("Introdujo letras,repita la informacion:...")

        while True:
            try:
                Aaño4=float(input("Promedio de año_4:__"))
                break
            except:
                print("Introdujo letras,repita la informacion:...")
                
        while True:
            try:
               Aaño5=float(input("Promedio de año_5:__"))
               break
            except:
                 print("Introdujo letras,repita la informacion:...")
               
        
        while True:
            try:
                Aaño6=float(input("Promedio de año_6:__"))
                break
            except:
                print("Introdujo letras,repita la informacion:...")

        alumno=Estudiante(Anombre,Aapellido1,Aapellido2,Aaño1,Aaño2,Aaño3,Aaño4,Aaño5,Aaño6)
        lista.Agregar_Objeto(alumno.Tupla())
        lista.Insertar_Basededatos()
    elif opcion =="b":
        lista.Mostrar_Datos()
        print("\n")
    elif opcion =="c":
        print("Para realizar la actualizacion de un estudiante siga los pasos:")
        opp=""
        while opp!="a":
            print("Seleccione el campo que desea actualizar:...")
            print("1)->Actualizar Nombre:")
            print("2)->Actualizar Primer apellido:")
            print("3)->Actualizar segundo apellido:")
            print("4)->Actualizar Primer año:")
            print("5)->Actualizar Segundo año:")
            print("6)->Actualizar Tercer año:")
            print("7)->Actualizar Cuarto año:")
            print("8)->Actualizar Quinto año:")
            print("9)->Actualizar Sexto año:")
            print("Para terminar presione (a).")
            opp =input("Dame valor:__")
            if opp=="1":
                lista.Actualizar_BASEdedatos_Nombre()
                print("\n")
            elif opp=="2":
                lista.Actualizar_BASEdedatos_Apellido_1()
                print("\n")
            elif opp=="3" :
                lista.Actualizar_BASEdedatos_Apellido_2()
                print("\n")
            elif opp=="4":
                lista.Actualizar_BASEdedatos_Año_1()
                print("\n")
            elif opp=="5":
                lista.Actualizar_BASEdedatos_Año_2()
                print("\n")
            elif opp=="6": 
                lista.Actualizar_BASEdedatos_Año_3()
            elif opp=="7":
                lista.Actualizar_BASEdedatos_Año_4()
                print("\n")
            elif opp=="8":
                lista.Actualizar_BASEdedatos_Año_5()
                print("\n")
            elif opp=="9" :
                lista.Actualizar_BASEdedatos_Año_6()
                print("\n")
            elif opp=="a":
                print("\n")
                continue
            else:
                print("Introdujo opcion icorrecta")
                print("\n")
                
    elif  opcion=="d":
        lista.DELETE_BASEdedatos()
        print("\n")
    elif opcion =="x":
        print("Usted esta saliendo del programa...")
        syst.exit()
    elif opcion=="e":
        lista.DELETE_BASEdedatosall()
        print("\n")
    else:
        print("Introdujo opcion incorrecta :..",opcion)
        print("\n")



        
        
        
