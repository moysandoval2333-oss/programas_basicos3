suma = 0
contador = 0

while True:
    numero = float(input("Ingresa un número: "))
    
    if numero < 0:
        break
        
    suma += numero
    contador += 1

if contador > 0:
    media = suma / contador
    print(f"La media es: {media}")
else:
    print("No se ingresaron números positivos.")
