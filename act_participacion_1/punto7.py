# 7. Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada.

print("El programa encontrará el número más grande y más pequeño en una lista dada.")
lista=[5,2,4,6,5,8,4,20,10,320,450]
mayor=0
menor=9999999
for i in range(0,len(lista),1):
    if lista[i]>mayor:
        mayor=lista[i]
    if lista[i]<menor:
        menor=lista[i]
print("El número más grande en la lista es: ",mayor, "y el número más pequeño es: ",menor)