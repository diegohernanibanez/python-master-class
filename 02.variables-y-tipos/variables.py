#Se inicializa una variable sin especificar el tipo de dato
variable = 98

#Se puede sobrescribir el tipo de dato de la variable volviendola a inicializar
variable = "hola"

decimal = 4.5

#Cuando se imprime la variable queda con el ultimo valor
print(variable)
print (decimal)

print("-----------------------")

nombre = "Diego"
apellido = "Ibañez"

#Concatenacion con simbolo '+'
print("Concatenación con simbolo '+': " + nombre + " " + apellido)

#Concatenacion con simbolo 'f' donde las variables se encierran con llaves
print(f"Concatenacion con simbolo 'f': {nombre} {apellido}")

#Concatenacion con metodo format donde las llaves dicen la posicion de las variables en el metodo
print("Concatenacion con metodo format: {} {}".format(nombre, apellido))