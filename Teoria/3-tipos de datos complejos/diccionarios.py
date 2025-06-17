# Diccionario

# tipo "dict"
# {Key: value, key2: value2, ..., keyn: valuen}
my_dic = {
    "Nombre": "Helena",
    "Apellidos": "Martín Delgado",
    "DNI": "12345678A",
    "País": "España",
    "Ciudad": "Barcelona"    
}

print(my_dic)

# Se puede hacer un diccionario con dict(). Se puede llamar las claves con comillas y luego ":"  o podemos llamar las claves sin comillas y luego ":"

dic2 = dict(
    Nombre = "Helena",
    Apellido = "Martín",
    Ciudad = "Barcelona"
)

print(dic2)

# Acceso a un elemento []
print(my_dic["DNI"]) # 12345678A

dic3 = {
    0 : "Helena",
    1 : "Martín",
    "Ciudad" : "Barcelona"
}

print(dic3[0]) # Helena

dic4 = {
    0 : "Helena",
    1 : "Martín",
    (13, "hey") : "Barcelona"
}

print(dic4[(13, "hey")]) #Barcelona


my_dic = {
    "Nombre": "Helena",
    "Apellidos": "Martín Delgado",
    "DNI": "12345678A",
    "País": "España",
    "Ciudad": "Barcelona"    
}

my_dic["Nombre"] = "Sergi"
my_dic["Apellidos"] = "Gonzalez"

print(my_dic) # {'Nombre': 'Sergi', 'Apellidos': 'Gonzalez', 'DNI': '12345678A', 'País': 'España', 'Ciudad': 'Barcelona'}

my_dic["Edad"] = 30 # Se añade la clave Edad con el valor 30 en el diccionario.
print(my_dic) # {'Nombre': 'Sergi', 'Apellidos': 'Gonzalez', 'DNI': '12345678A', 'País': 'España', 'Ciudad': 'Barcelona', 'Edad': 30}

my_dic2 = {
    "int": 10,
    "float": 2.0,
    "string": "Fernandito",
    "lista": [1,2,3,4],
    "tupla": ("a",2,"c"),
    "dic":{"k1":"value1", "k2":"value2"}
}

print(my_dic2["lista"][2]) # Imprime la posición 2 de la lista -> 3
print(my_dic2["dic"]["k1"]) # Imprime el valor de la clave k1 -> value1

my_dic = {
    "k1":10,
    "k2":30
}

print(my_dic) # {'k1': 30} -> Si hay dos claves que se llaman iguales, se modifica el valor de la clave con el último valor.


my_dic2 = {
    "k1": 10,
    "k2": 30,
}

print(my_dic is my_dic2) # False. Aunque tengan las mismas claves con los mismos valores no son lo mismo. Tienen diferente posición de memoria
print(my_dic == my_dic2) # True. Los dos diccionarios tienen los mismos valores.

# No se pueden sumar dos diccionarios.
