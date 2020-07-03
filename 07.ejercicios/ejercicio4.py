# Pedir dos numeros al usuario y realizar 4 operaciones basicas +, -, *, /

num_1 = int(input("Ingrese el primer nuemero: "))
num_2 = int(input("Ingrese el segundo numero: "))

print(f"{num_1} + {num_2} es {num_1 + num_2}")
print(f"{num_1} - {num_2} es {num_1 - num_2}")
print(f"{num_1} x {num_2} es {num_1 * num_2}")
if num_2 == 0:
    print(f"{num_1} / {num_2} es invalido. No se puede dividir por cero")
else:
    print(f"{num_1} / {num_2} es {num_1 / num_2}")