# Contar letras 'a'
texto = input("Ingresa una palabra o texto: ")
contador = 0

for letra in texto:

    if letra.lower() == 'a':
        contador = contador + 1

print(f"La letra 'a' aparece {contador} veces.")
