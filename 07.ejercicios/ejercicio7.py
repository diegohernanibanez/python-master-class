# Mostrar todos los numeros impares entre dos numeros que elija el usuario

check = True
while check:
    num_1 = int(input("Ingrese el numero mas chico: "))
    num_2 = int(input("Ingrese el numero mas grande: "))
    if num_1 > num_2:
        print("El primer numero ingresado es mas grande que el segundo")
        check = True
    else:
        for i in range(num_1, num_2 + 1):
            if i % 2 != 0:
                print(i)
        else:
            check = False    
