nombres = ["Jose", "Marcos", "Alejandra", "Romina", "Bastian", "Leandro"]

numeros = [2, 4, 8, 6, 1, 3, 5, 8, 2]

# Ordenar listas
nombres.sort ()
numeros.sort ()
print (nombres)
print (numeros)

# Insertar elemento con indice
nombres.insert (0, "Damian")
print (nombres)

# Eliminar elementos de la lista con indice
nombres.pop (2)
print (nombres)

# Eliminar elementos por valor
nombres.remove ("Romina")
numeros.remove (8)
print (nombres)
print (numeros)

# Revertir orden de la lista
nombres.reverse ()
print (nombres)

# Saber si hay un elemento en una lista
print ("Esta Romina en la lista 'nombres': " + str("Romina" in nombres))
print ("Esta Alejandra en la lista 'nombres': " + str("Alejandra" in nombres))

# Contar cantidad de elementos de una lista
print (len(nombres))

# Contar cuantas veces aparece un elemento en una lista
print (numeros.count (2))

# Conseguir un indice desde un valor
print (nombres.index ("Leandro"))

# Unir dos listas
nombres.extend(numeros)

print (nombres)