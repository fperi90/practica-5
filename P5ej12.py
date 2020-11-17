# Escribe un programa que pida un número y escriba si primo o no
# Dame un número: 123
# El número 123 no es primo
# Dame un número:127
# El número 127 es primo
numero=int(input("Introduce el numero a evaluar "))
contador=0
for i in range(numero+1):
    if(i==0):
        print("Comenzamos ")
    elif(((numero%i)==0) or (i==numero)):
        print(i)
        contador+=1
if (contador==2):
    print("El numero es primo")
else:
    print("El numero no es primo")