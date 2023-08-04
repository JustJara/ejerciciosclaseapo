#Crear una función que invierta el orden de los elementos en una lista dada

def invertir_orden_lista(lista):
    lista_invertida=[]
    for i in range(len(lista)-1,-1,-1):
        lista_invertida.append(lista[i])
    return lista_invertida

print(invertir_orden_lista(lista=[1,2,3,4,5,6,7,8,9,10]))