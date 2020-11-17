#     practica 5
#         ejercicio 5
# Escribe un programa que pida la altura y ancho de un rectángulo y lo dibuje de la siguiente manera:
# Anchura del rectángulo: 5
# Altura del rectángulo: 3
# *****
# *****
# *****
altura=int(input("Introduce la altura "))
ancho=int(input("Introduce el ancho "))
for i in range(altura):
    for j in range(ancho):
        print("*",end="")
    print("\n")