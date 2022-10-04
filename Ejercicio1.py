#Implementa un programa Python que PREGUNTE al usuario por dos números enteros (x, y)
# y muestre por pantalla la suma, resta, multiplicación, división y resto de ambos,
# con el siguiente formato:
# x + y = …
# x – y = …
# x * y = …
# x / y = …
# x % y = …

x = int(input('Escribe un numero: '))
y = int(input('Escribe un numero: '))

print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y}")
print(f"{x} % {y} = {x % y}")