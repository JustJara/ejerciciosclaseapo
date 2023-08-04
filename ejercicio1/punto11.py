# Crear un programa que genere una lista de números pares entre 1 y 100.
import random

lista=[]
tamano_lista = random.randrange(0,100,2)
for i in range(1,tamano_lista,1):
    num_random= random.randrange(0,100,2)
    lista.append(num_random)
    num_random=0
print(lista)