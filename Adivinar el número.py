# Adivinar número aleatorio 
import random

numero_secreto = random.randint(1, 100)
print("¡He pensado en un número del 1 al 100! Intenta adivinarlo.")

while True:
    intento = int(input("Introduce tu número: "))
    
    if intento < numero_secreto:
        print("El número secreto es MAYOR. Intenta de nuevo.")
    elif intento > numero_secreto:
        print("El número secreto es MENOR. Intenta de nuevo.")
    else:
        print("¡Felicidades! Lograste adivinar el número secreto.")
        break  #Rompe el bucle y termina el programa al ganar
