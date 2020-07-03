# Mostrar todos los numeros que se encuentran en un rango que defina el usuario
print("Ingrese dos numeros y le mostrare los que se encuentran entre ambos")
check = True
while check:
    num_1 = int(input("Ingrese el numero mas chico: "))
    num_2 = int(input("Ingrese el numero mas grande: "))
    if num_1 > num_2:
        print("El primer numero ingresado es mas grande que el segundo")
        check = True
    else:
        for i in range(num_1, num_2 + 1):
            print(i)
        else:
            check = False    
