# Hacer un ejercicio que calcule un porcentaje de un numero

num = int(input("Ingrese un numero: "))
porcentaje = int(input("Ingrese que porcentaje desea calcularle: "))

resultado = num * porcentaje / 100

print(f"El {porcentaje}% de {num} es {resultado}")