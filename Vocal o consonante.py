print("Introduce letras una por una. Presiona [Espacio] y [Enter] para salir.")

while True:
    entrada = input("Ingresa una letra: ")

    if entrada == " ":
        print("Programa terminado.")
        break

    letra = entrada.lower()

    if letra in "aeiouáéíóú":
        print(f"'{entrada}' es una VOCAL.\n")
    else:
        print(f"'{entrada}' es una CONSONANTE.\n")
