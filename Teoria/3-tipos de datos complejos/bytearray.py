"""
ByteArray y Byte

- 1 byte = 8 bits
- Los objetos bytes son inmutables
- Dato: bytes
- Sintaxis b'<cadena de bytes>' 
"""

# BYTE
#-------------------------------------------------------------------------------------------------------

cadena_byte = b"\x02\x1f" # 543   # \x es un espacio en UNICODE.  la b'...' quiere decir que es en bytes.
print(type(cadena_byte)) # class 'bytes'
print(cadena_byte) # b'\x02\x1f'

print(bin(543)) # Entra un int y sale un string en binario -> 0b1000011111
print(hex(543)) # Convierte el int a un string con valor hexadecimal -> 0x21f

num_bytes = b"\x02\x1f"
num = int.from_bytes(num_bytes, 'big') # Convierte a int el valor hexadecimal de la variable num_bytes. 'big' -> número grande
print(num) # 543

cadena_bytes2 = bytes(3) # Crea una variable con 3 bytes. Guarda una posición en memoria que no contiene nada.
print(cadena_bytes2) # b'\x00\x00\x00'

texto = "No me mateis"
texto_bytes = b'No me mateis'

print(type(texto)) # 'str'
print(type(texto_bytes)) # 'bytes'

print(texto_bytes)
texto_bytes = b'\x41\x42\x43'

hex_to_dec = int("41", base=16) # Convierte 41 de hexadecimal a decimal.
print(hex_to_dec) # 65.
print(texto_bytes) # b'ABC' porque el valor 65 en código ASCII es 'A'. 42 es 'B' y 43 es 'C'


texto_bytes = b'\x20\x19\x61\x62\x39\x40'
print(texto_bytes) # b' \x19ab9@'
hex_to_dec = int("20", base=16) # 32 = espacio en ASCII, por eso se representa con ' '
print(hex_to_dec)

hex_to_dec = int("19", base=16) # 25 = EM en ASCII (no se puede representar), por eso se pone '\x19'.
print(hex_to_dec)

hex_to_dec = int("61", base=16) # 97 = 'a' en ASCII 
print(hex_to_dec)

hex_to_dec = int("62", base=16) # 98 = 'b' en ASCII 
print(hex_to_dec)

hex_to_dec = int("39", base=16) # 57 = '9' en ASCII 
print(hex_to_dec)

print(texto_bytes[-1]) # 64 -> Python interpreta el valor que hay en la posición [-1] = \x40 que en base decimal es 64 = '@' en código ASCII
print(hex(texto_bytes[-1])) # 0x40 -> Pasa a hexadecimal el valor 64 de texto_bytes[-1]

slicing = texto_bytes[-1:] # b'@' -> Cuando haces slicing se ve el valor ASCII (texto_bytes[-1] = @). Cuando accedes a la posición te da el valor decimal (texto_byetex[-1] = 64)
print(slicing)

# Los Bytes son inmutables
# cadena_bytes = b'4' -> ERROR

# Operaciones

cadena_byte1 = b'\x20\x19\x61'
cadena_byte2 = b'\x62\x39\x40'

cad = cadena_byte1 + cadena_bytes2 # b' \x19a\x00\x00\x00'

print(cad) 
cad = cadena_byte1 * 3 # b' \x19a \x19a \x19a'
print(cad)


# BYTEARRAY
# ---------------------------------------------------------------------------------------------------------------

# Cadenas de bytes similar a bytes pero son MUTABLES

cadena_bytes = bytearray(b'\x20\x19\x61\x62\x39\x40')
print(cadena_bytes) # b' \x19ab'

print(type(cadena_bytes)) # 'bytearray'

# Acceso a los elementos
print(cadena_bytes[0]) # 32
print(cadena_bytes[0:4]) # b' \x19ab'

# Modificación
cadena_bytes[0:1]= b'A' # -> Si se quiere modificar el valor gráfico de una posición, haces slicing.
print(cadena_bytes)     # b'A\x19ab9@'

cadena_bytes[1] = 126 # Si quieres modificar el valor ASCII, accedes a la posición. El valor 126 ASCII equivale al símbolo gráfico ~
print(cadena_bytes)  # b'A~ab9@'


"""
NOTA!! Se imprime el símbolo gráfico ASCII desde el valor 32 al 126. El resto se imprime en valor hexadecimal.

Ej:

texto_bytes = b'\x20\x19\x61\x62\x39\x40'
print(texto_bytes) # b' \x19ab9@'   -> El valor \x19 en decimal es 25. -> 25 < 32 por lo tanto, no se puede representar gráficamente. Se imprime en hexadecimal.

"""

# ord() -> devuelve el código UNICODE.        RECORDAR: UNICODE contiene casi todos los abecedarios/simbolos. ASCII es solo el abecedario inglés.

print(ord('8')) # 56 en UNICODE es '8'.

print(chr(97)) # 97 en UNICODE es 'a' en símobolo gráfico.

cadena_bytes[2] = ord('X') # cadena_bytes[2] = 88
print(cadena_bytes) # b'A~Xb9@'

cad4 = bytearray(bytes(9)) # b'\x00\x00\x00\x00\x00\x00\x00\x00\x00'
print(cad4) 

c = 97
i = 0

while i < 9:
    cad4[i] = c
    c += 1
    i += 1
print(cad4) # b'abcdefghi

