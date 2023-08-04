#. Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.

import random 

lista=[]
for i in range(0,10,1):
    lista.append(random.randint(0,10000))
print(lista)