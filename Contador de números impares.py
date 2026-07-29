contador_impares = 0

while True:
    numero = int(input("Ingresa un número entero (0 para salir): "))
    
    if numero == 0:
        break
        
    if numero % 2 != 0:
        contador_impares += 1

print(f"Cantidad de números impares ingresados: {contador_impares}")
