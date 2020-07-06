# Listas son colecciones de datos bajo un unico nombre
# Podemos usar un indice numerico para acceder a los datos

pelicula = "Batman"
peliculas = ["Batman", "Superman", "Mujer Maravilla"]

print (peliculas)

cantantes = list (("Drake", "Riahana", "Hayley Williams", "Miley Cyrus", "Dua Lipa"))

print (cantantes)

years = list (range(1990, 2021))

print (years)

variada = ["Juan", "Perez", 1990, True, 3.2, 'a']

print (variada)

# Indices

print (f"Indice 1 {peliculas [1]}")
print (f"Indice 1 empezando desde atras para adelante {peliculas[-2]}")
print (f"Indices 1, 2, 3 {cantantes [1:4]}")
print (f"Todos los elementos a partir del indice 1 {cantantes [1:]}")

peliculas [1] = "Superman"

print (peliculas)

# Añadir elemento a lista

cantantes.append ("Bruno Mars")

print (cantantes)

cantante = ""

# while cantante != "N" :
#     cantante = input ("Agregue un/a nuevo/a cantante. Para salir ingrese N:\n")
#     if cantante != "N" :
#         cantantes.append (cantante)

# Recorrer una lista con bucle for

for i in cantantes :
    print (f"{cantantes.index(i) + 1 }. {i}")

# Lista multidimensionales

print ("\n---- Lista de contactos ----")

contactos = [
    [
        "Antonio",
        "antonio@mail.com"
    ],
    [
        "Luis",
        "luis@mail.com"
    ],
    [
        "Juan",
        "juan@mail.com"
    ]
]

print (contactos [1][1])

for contacto in contactos : 
    print (contacto[0], contacto[1])

for contacto in contactos :
    print ("\n")
    for elemento in contacto :
        if contacto.index(elemento) == 0 :
            print ("Nombre: " + elemento)
        elif contacto.index(elemento) == 1 :
            print ("Email: " + elemento)