#Escribe un programa que pida un número y calcule su factorial.
#Dame un número: 5
#El factorial de 5 es: 120
numero=int(input("Introduce el numero a calcular "))
a=b=1
for i in range(numero,0,-1):   #aqui hacemos la iteración hacia 0, sin cinluir a este último
   a=i
   b=b*a                        #aqui almacenamos en b el valor de b*a, asi en la proxima vuelta, b seguira valiendo la multiplicacion anterior
print(b)