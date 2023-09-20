from src.punto1 import Elemento, Conjunto

conjunto3= Conjunto("Estudiantes1")
conjunto2 = Conjunto("Estudiantes2")

elemento1= Elemento("Pablo")
elemento2= Elemento("Alejo")
elemento3= Elemento("Felipe")
elemento4= Elemento("Luis")
elemento5 = Elemento("Thomas")

conjunto3.agregar_elemento(elemento1)
conjunto3.agregar_elemento(elemento2)
conjunto3.agregar_elemento(elemento3)
conjunto3.agregar_elemento(elemento4)
conjunto2.agregar_elemento(elemento1)
conjunto2.agregar_elemento(elemento2)
conjunto2.agregar_elemento(elemento3)
conjunto2.agregar_elemento(elemento5)

union = conjunto3 + conjunto2
interseccion = Conjunto.intersectar(conjunto3,conjunto2)

print(conjunto3)
print(conjunto2)
print(f"{union}")
print(f"{interseccion}")
