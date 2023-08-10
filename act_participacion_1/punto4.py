#4. Escribir un programa que determine si un número dado es par o impar

print("Este programa es para determinar si un número es par o impar")
numero = int(input("Ingrese cualquier número entero: "))
if numero % 2==0:
    print(numero, "es par")
else:
    print(numero, "es impar")