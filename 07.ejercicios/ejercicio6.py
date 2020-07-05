# Mostrar todas las tablas de multiplicar del 1 al 10 con sus titulos

numero = 1
numero2 = 1

while numero <= 10:
    print(f"\nTabla del {numero}")
    while numero2 <= 10:
        print(f"{numero} x {numero2} = {numero2 * numero}")
        numero2 += 1
    numero += 1
    numero2 = 1