# Este programa calcula ecuaciones de segundo y primer orden
# Menu de inicio, tiene 2 obciones
from math import sqrt
opcion = ''
while opcion !='a' or opcion!= 'b':
    print("Escoge una opcion :")
    print("a) Resolver ecuacion lineal (mx+n)")
    print("b) Resolver ecuacion cuadratica (mx**2+nx+z)")
    opcion = input()
    if opcion == 'a':
        print("Dame los valores de m y n")
        m = float(input())
        n = float(input())
        if m == 0:
            print("La ecuacion no tiene solucion")
        elif n == 0:
            print("La solucion es : 0")
        else:
            x = float(-n / m)
            print("El resultado es :",x)

    elif opcion >'b':
        print("Opcion incorrecta, repita la opcion")
    else:
        print("Dame los valores de m,n y z :")
        m = float(input())
        n = float(input())
        z = float(input())
        discriminante = n ** 2 - 4 * m * z
        if m == 0:
            print("La ecuacion no tiene solucion")
        else:
            if discriminante < 0:
                print("La solucin escapa del domineo de los reales")
            else:
                x1 = float((-n + sqrt(n ** 2 - 4 * m * z)) / (2 * m))
                x2 = float((-n - sqrt(n ** 2 - 4 * m * z)) / (2 * m))
                if x1 == x2:
                    print("La solucion es : x1=", x1)
                else:
                    print("La solucion es : x1=", x1, "\t x2=", x2)
















