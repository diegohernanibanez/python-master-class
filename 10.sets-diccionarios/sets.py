# Set es un objeto que almacena una coleccion de valores sin ningun orden

personas = {
    "Juan",
    "Pedro",
    "Leandro",
    "Ramiro"
}

print (personas, type(personas))

personas.add("Diego")
personas.remove("Pedro")
print (personas, type(personas))

