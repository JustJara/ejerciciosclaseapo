#15. Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no.
def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    longitud = len(cadena)
    for i in range(longitud // 2):
        if cadena[i] != cadena[longitud - i - 1]:
            return False
    return True

texto = input("Ingresa una cadena de texto: ")

if es_palindromo(texto):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")
