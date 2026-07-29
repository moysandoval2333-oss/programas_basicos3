while True:
    print("\n--- CALCULADORA ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == "5":
        print("Programa terminado.")
        break
        
    if opcion in ["1", "2", "3", "4"]:
        num1 = float(input("Primer número: "))
        num2 = float(input("Segundo número: "))
        
        if opcion == "1":
            print(f"Resultado: {num1 + num2}")
        elif opcion == "2":
            print(f"Resultado: {num1 - num2}")
        elif opcion == "3":
            print(f"Resultado: {num1 * num2}")
        elif opcion == "4":
            if num2 != 0:
                print(f"Resultado: {num1 / num2}")
            else:
                print("Error: No se puede dividir entre cero.")
    else:
        print("Opción no válida.")
