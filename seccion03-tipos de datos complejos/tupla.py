"""
TUPLAS: Objetos identicos a Listas excepto por las siguientes propiedades:

- Definición: mi_tupla = (obj1, obj2, obj3, ..., objn)
- Las tuplas son INMUTABLES
- type(mi_tupla) => tuple
"""

mi_nombrecito = (1,2,3,"string",4,5)
# mi_nombrecito[0] = 21 -> ERROR! No se puede modificar los valores de una tupla, a diferencia de las listas [..,...,..]

tupla1 = (12)
type(tupla1) # int -> lo identifica como un int.
tupla2 = (12,) 
type(tupla2) # tuple -> ahora lo identifica como una tupla. El 2 valor lo identifica como null y ppor lo tanto (12, null) = tupla

# Packing and Unpacking
mi_tuplita = (1,2,3,6,7)
num1, num2, num3, num4, mum5 = mi_tuplita
print(num1)

def func():
    return 5,6

print(func()) # (5,6) -> retorna una tupla

n1,n2 = func()
print(n1) # 5
print(n2) # 6
