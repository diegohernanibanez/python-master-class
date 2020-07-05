# Las mejores practicas son no hacer un print dentro de una funcion
# dentro de lo posible, definir arriba de todo a las funciones, 
# que retornen valores y pasarle variables por parametro.
# Eso para mantener nuestro codigo limpio y correcto

def funcion (arg):
    return f"Soy una funcion y recibo un argumento {arg}"

def otra_funcion (arg):
    return f"Soy otra funcion y recibo un argumento {arg}"

texto = "Texto generico"
texto_2 = "Texto generico 2"

print(funcion(texto))
print(otra_funcion(texto_2))