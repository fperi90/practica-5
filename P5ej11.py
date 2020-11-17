# Escribe un programa que pida un número e imprima todos sus divisores.
# Dame un número: 200
# Los divisores de 200 son: 1 2 4 5 8 10 20 25 40 50 100 200
numero=int(input("Introduce el numero a evaluar "))
for i in range(numero+1):
    if(i==0):
        print("Comenzamos ")
    elif(((numero%i)==0) or (i==numero)):
        print(i)
    