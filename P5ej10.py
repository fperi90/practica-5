# Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:
# Altura de un triángulo: 5
#     *
#    ***
#   *****
#  *******
# *********
altura=int(input("Introduce la altura del triangulo "))
apoyo=(altura*2)-1
flotanteA=altura-2
flotanteB=altura
for i in range(altura):
    for j in range(apoyo):
        if((j>flotanteA) and (j<flotanteB)):
            print("*",end="")
        else:
            print(" ",end="")
    flotanteA-=1
    flotanteB+=1    
    print("\n")   