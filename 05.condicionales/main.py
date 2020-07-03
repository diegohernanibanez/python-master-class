# Comparadores logicos
# == igual
# != diferente
# < menor
# > mayor
# <= menor o igual
# >= mayor o igual
# or o
# and y
# not invierte el resultado logico


# Ejemplo 1
print("---Ejemplo 1----")

color = "rojo"

if color == "rojo":
    print("El color es rojo")
else:
    print("El color no es rojo")

# Ejemplo 2
print("\n----Ejemplo 2----")

num_1 = 101

if (num_1 < 100) or (num_1 and 2 == 0):
    print("True")
else:
    print("False")

print("\n----Ejemplo 3----")

nombre = "Alejo"
edad = 20
toma_cerveza = False
mayoria_edad = 18
if edad >= mayoria_edad:
    if toma_cerveza:
        print(f"{nombre} tiene {edad} y le gusta la cerveza.")
        print("Convidar cerveza ;)")
    else:
        print(f"{nombre} tiene {edad} y le no gusta la cerveza.")
        print("Convidar fernet ;)")
else:
    print(f"{nombre} tiene {edad} y no puede tomar cerveza.")
    print("Convidar juguito :(")

print("\n----Ejemplo 4----")

dia = 4
# dia = int(input("Ingrese un numero de dia de la semana: "))

if dia == 1:
    print("Es domingo")
elif dia == 2:
    print("Es lunes")
elif dia == 3:
    print("Es martes")
elif dia == 4:
    print("Es miercoles")
elif dia == 5:
    print("Es jueves")
elif dia == 6:
    print("Es viernes")
elif dia == 7:
    print("Es sabado")
else:
    print("Ingrese un numero del 1 al 7")

