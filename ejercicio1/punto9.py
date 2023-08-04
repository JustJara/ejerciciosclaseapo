# Crear un programa que genere una matriz de números y la imprima en pantalla.
matriz=[]
for i in range(0,5,1):
    lista=[]
    for j in range(0,5,1):
        lista.append(j)
    matriz.append(lista)
print(matriz)