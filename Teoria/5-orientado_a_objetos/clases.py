"""
Clases
=> Estructura principal de los lenguajes orientados a objetos
=> Medio para agrupar datos y funcionalidades
=> Dentro de las clases hay instancias y estas se denominan objetos
=> Cada instancia puede tener atributos para mantener su estado y métodos para modificar su estado
=> La primera letra

class <Nombre_clase>:
    <sentencias>

<Nombre_clase>(<argumento>)
"""

class Coche:
    pass

coche1 = Coche()
print(coche1)

print(type(coche1))

print("Id coche1:",id(coche1))

#print(__name__)
if __name__ == "__main__":
    pass

coche2 = Coche()
print("Id coche2:", id(coche2))

print(coche1 is coche2)
print(coche1 == coche2)