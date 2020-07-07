def recorrerLista(lista):
    cadena = ""
    for elemento in lista:
        cadena += str(elemento)
        cadena += "\n"
    return cadena


lista = [4, 6, 7, 5, 8, 2, 3, 1]
print("\n---- Lista ----")
print(recorrerLista(lista))

print("\n---- Lista ordenada ----")
print(recorrerLista(sorted(lista)))

print(f"\nCantidad de elementos: {len(lista)}")

numero = int(input("\nIngrese el numero que desea buscar: "))

if numero in lista:
    print("El numero está en la lista")
else:
    print("El numero no está en la lista")

