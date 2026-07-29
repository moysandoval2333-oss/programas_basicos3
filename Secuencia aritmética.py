n = int(input("Ingresa un número entero positivo límite (N): "))
suma = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        suma = suma + i

print(f"La suma de los números pares desde 1 hasta {n} es: {suma}")
