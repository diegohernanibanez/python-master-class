# Imprimir por pantalla los primero 60 numeros naturales elevados al cuadrado

numero = 1

while numero <= 60 :
    print(f"El cuadrado de {numero} es {numero ** 2}")
    numero += 1

print("------------------------")

for i in range(1, 61):
    print(f"El cuadrado de {i} es {i ** 2}")