# Factorial de un número
numero = int(input("Ingresa un número entero positivo: "))
factorial = 1

if numero < 0:
    print("El factorial no existe para números negativos.")
elif numero == 0:
    print("El factorial de 0 es 1")
else:
    # REGLA: Usamos un bucle 'for' para realizar las multiplicaciones repetitivas
    for i in range(1, numero + 1):
        factorial = factorial * i
        
    print(f"El factorial de {numero} es: {factorial}")
