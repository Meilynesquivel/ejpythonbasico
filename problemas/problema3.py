# Pedimos al usuario que ingrese un número entero
num = int(input("Ingrese un número entero: "))

# Convertimos el número a una cadena y ordenamos sus dígitos en orden ascendente
num_str = str(num)
num_sorted = "".join(sorted(num_str))

# Comprobamos si el número resultante es divisible por 5
if int(num_sorted) % 5 == 0:
    print("Los dígitos del número", num, "se pueden ordenar de tal forma que el resultado es un múltiplo de 5.")
else:
    print("Los dígitos del número", num, "no se pueden ordenar de tal forma que el resultado sea un múltiplo de 5.")
    
