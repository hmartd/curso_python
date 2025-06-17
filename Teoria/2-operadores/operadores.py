"""
Divisiones:

a / b = float
a // b = int 

Módulo: a % b -> residuo de la división

"""
# SUMA (a + b)

# Enteros
a = 10
b = 5

c = a + b
print(c)

# Float
d = 1.2
e = 3.2

f = d + e
print(f)

# Strings 
text1 = "Hola "
text2 = "Mundo"

text3 = text1 + text2
print(text3)

# RESTA (a - b)

# Enteros 
a = 10
b = 5

c = a - b
print(c)

# Float
d = 1.2
e = 3.2

f = d - e
print(f)

# Las cadenas de texto se pueden sumar pero no restar

# UNARIOS (+a | -a)
a = 10
print(-a) # -10
print(+a) # +10

# MULTIPLICACIÓN (a * b)

# Enteros
a = 1
b = 2

c = a * b
print(c)

# Floats
a = 1.4
b = 2.6

c = a * b
print(c)

# Strings
text = "Hola"
text2 = text1 * 2 #Multiplicar mismo STR por n veces -> Hola Hola
print(text2)

# DIVISIÓN FLOAT (a / b)
a = 2.3
b= 6.8

c = a / b 
print("a / b =", c)

# DIVISIÓN ENTERO (a // b)
a = 6
b= 2

c = a / b
print("a / b =", c) # 3.0 (división float)

c = a // b
print("a // b =", c) # 3 (división entera)

# MÓDULO (%)
a = 24
b = 7

c = a % b
print("a % b = ",c)

# EXPONENCIAL (a ** b)
a = 8.9
b = 9

c = a ** b 
print("a ** b =", c)