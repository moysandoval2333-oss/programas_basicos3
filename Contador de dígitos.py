# Contador de dígitos 
numero = int(input("Ingresa un número entero: "))
temp = abs(numero)
contador = 0
if temp == 0:
    contador = 1
else:
    while temp > 0:
        temp = temp // 10  # División entera (elimina el último dígito)
        contador = contador + 1

print(f"El número {numero} tiene {contador} dígitos.")
