while True:
    limite = int(input("¿Cuántos cuadrados deseas generar? (0 para salir): "))
    
    if limite <= 0:
        break
        
    for i in range(1, limite + 1):
        print(f"{i} al cuadrado es: {i ** 2}")
        
    break
