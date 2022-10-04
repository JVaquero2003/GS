#Ejercicio 3:  ¡IMPLEMENTA TU PRIMER JUEGO! Realiza un programa Python que adivine el número.
# El programa generará un número aleatorio entre 0 y 20 y luego irá pidiendo números al usuario
# indicando “mayor” o “menor” según sea mayor o menor con respecto al número generado aleatoriamente.
# El proceso termina cuando el usuario acierta, y deberá mostrar un mensaje de felicitaciones
# junto al número de intentos que ha necesitado el usuario.

import random


numero = random.randint(0, 20)
count = 0
print(numero)

while True:
    x = int(input("Introduce un numero entre 0 y 20: "))
    if x > numero:
        print("¡El numero a adivinar es menor que el numero introducido!")
        count += 1
    elif x < numero:
        print("¡El numero a adivinar es mayor que el numero introducido!")
        count += 1
    else:
        print("¡Has acertado el numero!")
        print(f" Has realizado {count}  intentos")
        break