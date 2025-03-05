def generar_fibonacci(rango):
    a, b = 0, 1
    while True:
        if a > rango[1]:
            break
        if a >= rango[0]:
            yield a
        a, b = b, a + b

def main():
    rango = input("Ingrese el rango (separado por espacios): ")
    rango = [int(x) for x in rango.split()]
    rango.sort()  

    print("Números de Fibonacci dentro del rango:")
    for num in generar_fibonacci(rango):
        print(num)

if __name__ == "__main__":
    main()