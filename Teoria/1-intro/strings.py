# Strings en Python

var = "Mi primer string"
var2 = 'Segundo string'

# Indexación

nombre = 'Fernando'
print(nombre[0])
print(nombre[4])
print(nombre[-1])
print(nombre[-5])

# Slicing -> Extrae conjunto de caracteres

nombre = "Fernando Aguilar"
print(nombre[0:8]) # Extrae desde el caracter 0 al 8-1, es decir, al 7. --> Fernando
print(nombre[-9:-1]) # --> o Aguila
print(nombre[-9:]) # Extrae desde el caracter en la posición -9 hasta el final
print(nombre[:4]) # Extrae desde el inicio hasta el caracter 4-1, es decir, 3.
print(nombre[:]) # Extrae todo, desde el inicio hasta el final

# Stride -> Salto de caracter para obtener un nuevo caracter

nombre = "Fernando Aguilar"
print(nombre[0:8:2]) # Imprime de la posición 0 a la 8-1:7, haciendo saltos de dos en dos. 
print(nombre[::2]) # Imprime todo, desde inicio a fin, haciendo saltos de dos en dos.

# Inmutabilidad

nombre = "Fernando"
print(nombre[3]) # n -> Si quisiera cambiar el valor nombre[3] = 'p' me aparecería un error. No se pueden modificar los strings.

# Multiples Lineas

nombre = 'Nombre: Fernando\nApellidos: Aguilar Espinosa\nDNI: 12345678A'
print(nombre)

nombre2 = """Nombre: Fernando
Apellidos: Aguilar Espinosa
DNI: 12345678A"""
print(nombre2)