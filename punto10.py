#10. Escribir una función que calcule el factorial de un número dado.

def calcular_factorial(numero):
    factorial = numero
    for i in range(numero-1,0,-1):
        factorial *= i
    return factorial

print(calcular_factorial(5))