# Mostrar por consola todos los numeros pares del 1 al 120

contador = 1

for i in range(1, 121):
    if i % 2 == 0:
        print(i)

print("----------------------------")

while contador <= 120:
    if contador % 2 == 0:
        print(contador)
    contador += 1