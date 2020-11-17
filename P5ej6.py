# Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:
# Altura del triángulo: 4
# *
# **
# ***
# ****
altura=int(input("Introduce la altura del triangulo "))
asterisco=0
for i in range (altura):
    asterisco=asterisco+1
    for j in range(asterisco):
        print("*",end="")
    print("\n")