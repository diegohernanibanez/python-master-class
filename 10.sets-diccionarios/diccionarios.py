# Los diccionarios son objetos que almacenan datos con un id 

persona = {
    "nombre": "Juan",
    "apellido": "Perez",
    "dni": 123123123
}


print(persona.get("nombre"))
print(persona["apellido"])

# Lista con diccionarios
print("\n---- Diccionarios dentro de listas ----\n")

contactos = [
    {
        "nombre": "Antonio",
        "email": "antonio@mail.com",
    },
    {
        "nombre": "Luis",
        "email": "luis@mail.com",
    },
    {
        "nombre": "Salvador",
        "email": "salvador@mail.com",
    }
]
print(contactos[0]["nombre"])

print(contactos[0].get("email"))

print("\n---- Lista de contactos ----\n")

print("------------------------------")

for contacto in contactos:
    print(f"Nombre: {contacto.get('nombre')}")
    print(f"Email: {contacto.get('email')}")
    print("------------------------------")
