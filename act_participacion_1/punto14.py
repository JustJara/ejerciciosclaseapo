#14. Escribir una función que calcule la media aritmética de una lista de números

def media_aritmetica_de_una_lista(lista):
    contador = 0
    suma_numeros=0
    for i in range(0,len(lista),1):
        suma_numeros+= lista[i]
        contador+=1
    media = suma_numeros / contador
    return media

print(media_aritmetica_de_una_lista(lista=[2,4,6,8,10]))