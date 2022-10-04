#Ejercicio 2:  Escribe un programa Python que pregunte al usuario por 10 números enteros 
# y muestre por pantalla el número total de veces que
# el usuario ha introducido el 0, el número total de enteros mayores que 0 
# introducidos y el número total de enteros menores que 0 introducidos.

contador1 = 0
contador2 = 0
contador3 = 0
listaNumeros=[]

for i in range(10):
    x = int(input('Escribe el numero '+str(i+1)+' :'))
    listaNumeros.append(x)

for i in range(len(listaNumeros)):
    if listaNumeros[i] == 0:
        contador1 += 1
    elif listaNumeros[i] > 0:
        contador2 += 1
    elif listaNumeros[i]<0:
        contador3 += 1

print(f"NUMERO DE VECES INTRODUCIDO EL 0:  {contador1}")
print(f"NUMEROS MAYORES QUE 0:  {contador2}")
print(f"NUMEROS MENORES DE 0:  {contador3}")