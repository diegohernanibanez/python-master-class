# Bucle while

print("Tabla de multiplicar:\n")

contador = 1
numero_usuario = int(input("Ingrese un numero: "))
while contador <= 10 :
    print(f"{numero_usuario} x {contador} = {numero_usuario * contador}")
    contador += 1
