# Este programa calcula la combinatoria de n,m siempre que n sea >= m
op = ""
while op !="a":
    print("Introdusca valores de n y m tenga en cuenta que n deve ser mayor o igual a m\n")
    n = int(input())
    i = n
    a = n
    m = int(input())
    l = m
    b = m
    tem = int(n-m)
    p = tem

    if n >= m:
# Calculo del factorial de n
        while i > 1:
            i -= 1
            n *= i
        while l > 1:
            l -=1
            m *=l
        while p > 1 :
            p -=1
            tem *=p
# Calculo de la divicion de la Combinatoria
        divicion =int( n/(tem*m))
        print("La combinatoria de", a, "y", b, "es :", divicion)
        variable = input("Itroduce (x) para salir :-> ")
        if variable =="x":
            break
    else:
        print("No se cumple n >= m")


