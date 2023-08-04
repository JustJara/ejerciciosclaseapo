#. Crear un programa que calcule la suma de los números en una lista dada.

lista = [2,4,6,8,10,20,40,10]
suma_numeros = 0
for i in range(0,len(lista),1):
    suma_numeros += lista[i]
print(suma_numeros)