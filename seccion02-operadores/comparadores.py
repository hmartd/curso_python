# COMPARACION

# IGUAL A (==) a == b
a = 3
b = 4
 
print(a == b)

# NO IGUAL (!=) a != b 
a = 3
b = 4

print(a != b)

# STRINGS
text1 = "Tengo Pecueca"
text2 = "Tengo pecueca"

print(text1 == text2) # False
print(text1 != text2) # True

# MENOR QUE ( < ) 
a = 5
b = 7
c = a < b
print(c)

# MENOR o IGUAL ( <= )
a = 6
b = 6 
c = a <= b 
print(c)

t1 = "Tengo Pecueca"
t2 = "Tengo pecueca"
print("El texto t1 <= t2 = ", t1 <= t2) # True -> Se suma los valores ASCII de cada cadena de caracteres y se comparan esos dos valores.

# MAYOR o IGUAL ( >= )
a = 6
b = 6 
c = a >= b 
print(c)

# COMANDO help() -> sirve para ver información sobre un comando cuando no sabes qué es lo que hace.

help(ord)

# Help on built-in function ord in module builtins:
# ord(c, /)
# Return the Unicode code point for a one-character string.

print("El valor de a es", ord('a')) # El valor de a es 97 -> El valor de 'a' es 97 en el código UNICODE (como el código ASCII pero admite múltiples lenguajes y símbolos)

# ASCII es un subconjunto de UNICODE. Es el abecedario en inglés. 

help(chr)

# chr(i, /)
# Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.

print("El string con valor 67 es",chr(67)) # -> El string con valor 67 es C -> El string 'C' tiene el valor 67 en el código UNICODE

print(chr(67) == 'Z') # False. El caracter con valor 67 no es 'Z'

