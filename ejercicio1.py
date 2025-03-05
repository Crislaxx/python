def numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Ingresa un número entero válido.")

num1 = numero("Escribe el primer número entero: ")
num2 = numero("Escribe el segundo número entero: ")

print("La suma de", num1, "y", num2, "es:", num1 + num2)
print("La resta de", num1, "y", num2, "es:", num1 - num2)
print("La multiplicación de", num1, "y", num2, "es:", num1 * num2)

if num2 != 0:
    print("La división de", num1, "y", num2, "es: %.2f" % (num1 / num2))
else:
    print("No se puede dividir entre cero.")
