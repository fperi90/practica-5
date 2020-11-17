#Escribe un programa que pida dos números y escriba
#la suma de enteros desde el primero hasta el último.
primero=int(input("Introduce el primer numero "))
segundo=int(input("Intoduce otro numero mayor que "))
a=0
if (primero>=segundo):
        print("No hay numeros intermedios positivos")
else:
    for i in range(primero,(segundo+1)):
       print(i,end=" ")
       a=a+i
print("La suma desde",primero,"hasta",segundo,"es",a)