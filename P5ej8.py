# Escribe un programa que pida la anchura de un triángulo y lo dibuje de la siguiente manera:
# Altura del triángulo: 4
# *
# **
# ***
# ****
# ***
# **
# *
altura=int(input("Introduce la altura del triangulo "))
asterisco=0
for i in range (altura):
    asterisco=asterisco+1
    for j in range(asterisco):
        print("*",end="")
    print("\n")
for i in range (altura):
    # aqui el paso a tener en cuenta es que la variable asterisco ya venia con el valor incrementado,
    # por lo tanto el descenso comienza desde el numero definido por altura
    asterisco=asterisco-1
    for j in range(asterisco):
        print("*",end="")
    print("\n")