# Pedir 15 notas de alumnos y decir cuantos aprobaron y cuantos no
nota = 0
desaprobados = 0
aprobados = 0
invalida = True

for numero in range(0, 15):
    while invalida:
        nota = int(input(f"Ingrese la nota del alumno {numero + 1}: "))
        if nota >= 7 and nota <= 10:
            aprobados += 1
            invalida = False
        elif nota >= 1 and nota <= 6:
            desaprobados += 1
            invalida = False
        else:
            print(f"{nota} no es una nota valida")
    invalida = True

print(f"\nLa cantidad de desaprobados es: {desaprobados}")
print(f"\nLa cantidad de aprobados es: {aprobados}")