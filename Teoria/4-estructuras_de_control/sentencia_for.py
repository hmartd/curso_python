colores = ["rojo", "azul", "verde"]

for yuju in colores:
    print(yuju)

print(yuju) # verde

# Objetos iterables

"""
Función iter()
=> Si un objeto es iterable
"""

print(iter("Cadena de texto"))
print(iter([1,2,3,4,"Hola"]))
print(iter({"k1":"valor1","k2":"valor2"}))

#  print(iter(45)) => ERROR: No se puede iterar un número

# next() => Devuelve valor uno a uno de un iterador

lista = ["Azul", "Rojo", "Verde"]

lista_iter = iter(lista)
print(type(lista_iter)) # 'list_iterator'

print("Lista sin inicializar", lista_iter) # Lista sin inicializar <list_iterator object at 0x000001BE74C3B4C0> => Al no estar inicializada, devuelve una posición en memoria que es donde se guarda la lista iterable.

print("Lista inicializada:",next(lista_iter)) # Ahora ya está inicializada con el primer valor de la lista: Azul (Coge el primer valor de la lista).
print(next(lista_iter)) # Rojo (Coge el siguiente valor)
print(next(lista_iter)) # Verde

print("Len de iter:", len(next(iter(lista)))) # Len: 4 => Hay 4 porque el primero es la posición de memoria + 3 valores de la lista (Azul, Rojo, Verde)


# Rango

print(range(5)) # range(0,5) => Los rangos siempre van de 0 hasta que acabe, en este caso 5. (Números positivos)
list_range = list(range(5))
print(list_range) # [0, 1, 2, 3, 4]

list_range = list(range(10, 20)) # Crea una lista con rango que empieza desde 10 hasta 20. [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(list_range) # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

list_range = list(range(10, 20, 2)) # Crea una lista con rango 10 hasta 20 con saltos de 2 en 2.
print(list_range) # [10, 12, 14, 16, 18]

for num in range(11):
    print(num)

print("---")

for num in range(11, 0, -1):
    print(num)

# Añadir a una lista vacía las letras del abecedario:

result = []

for letter in range(ord("a"), ord("z")+1):
    result.append(chr(letter))

print(result)