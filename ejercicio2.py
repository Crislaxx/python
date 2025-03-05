frase = input("Escribe una frase: ")

palabras = frase.split()

if palabras:
    print(f"Número de palabras: {len(palabras)}")
    print(f"Longitud promedio: {sum(len(p) for p in palabras) / len(palabras):.2f}")
    print(f"Palabra más larga: {max(palabras, key=len)}")
else:
    print("No ingresaste ninguna palabra.")
