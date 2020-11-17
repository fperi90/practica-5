# Escribe un programa que pida la anchura y la altura de un rectángulo y lo dibuje de la siguiente manera:
# Anchura del rectángulo: 5
# Altura del rectángulo: 4
# *****
# *   *
# *   *
# *****
altura=int(input("Introduce la altura "))
ancho=int(input("Introduce el ancho "))
for i in range(altura):
    if((i==0) or (i==(altura-1))):
        for j in range(ancho):
            print("*",end="")
        print("\n")
#en un principio para comprobar si estaba imprimiendo los datos correctos me apoye en dos letras para
#poder visualizar mejor el contenido de las columnas, la letra n y la t
    elif((i!=0) or (i!=altura)):
        for k in range(ancho):
            if ((k==0) or (k==(ancho-1))):
                print("*",end="")#en este asterisco iba la n
            elif(k!=0):
                print(" ",end="")#en este espacio vacio iba la t
        print("\n")