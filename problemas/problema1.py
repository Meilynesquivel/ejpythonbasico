frase = input("Ingresa una frase: ")

# Convertimos la frase a minúsculas y eliminamos espacios y signos de puntuación
frase = frase.lower().replace(" ", "").replace(",", "").replace(".", "").replace("?", "").replace("¿", "").replace("¡", "").replace("!", "")

# Creamos la cadena invertida
invertida = frase[::-1]

# Comparamos la cadena original con la invertida
if frase == invertida:
    print("La frase es palíndromo")
else:
    print("La frase no es palíndromo")
