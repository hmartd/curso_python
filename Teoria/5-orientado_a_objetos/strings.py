"""Trabajando con Strings"""

string = "Mi texto"
# print(dir(string)) -> Muestra todos los metodos que se pueden hacer con la variable string

# Transformaciones

string = "mOrEnItO rEcHuLon"
print(string.capitalize()) # Morenito rechulon -> Pone todo en minúscula excepto la primera en Mayus.
print(string) # mOrEnItO rEcHuLon -> Los strings son inmutables. Por eso después de hacer .capitalize() sigue teniendo el mismo valor.

print(string.lower()) # morenito rechulon -> Todo a minus.
print(string.swapcase()) # MoReNiTo ReChUlON -> Invierte las mayus por minus y al revés.
print(string.title()) # Morenito Rechulon -> Pone en mayus todas las primeras letras.
print(string.upper()) # MORENITO RECHULON -> Todo en Mayus

texto = "aoo boo coo"

print(texto.count("oo")) # 6 -> cuenta cuantas veces 
print(texto.find("boo")) # 4 -> indica el índice de la primera letra donde se encuentra "boo"

""" Ejercicio: Encuentra el boo de en medio"""

# A mi manera
texto = "aoo boo coo boo coo boo"

nuevo_texto = ""
indx = texto.find("boo")
for elem in range(indx+3, len(texto)):
    nuevo_texto += texto[elem]

nuevo_idx = nuevo_texto.find("boo")
print(indx+3 + nuevo_idx)

print("-"*30)

# Solución:
texto = "aoo boo coo boo coo boo"

primer_boo = texto.find("boo") # 4
segundo_boo = texto.find("boo", primer_boo + 1) # Busca el segundo "boo" a partir de la posición donde se encontraba el primer "boo" + 1 (posición letra b + 1)
tercer_boo = texto.find("boo", segundo_boo + 1) # Busca el tercer "boo"

print("Nº de boo: ", texto.count("boo")) # Cuenta cuantas veces aparece "boo" en la cadena texto.

print("1 boo", primer_boo)
print("2 boo", segundo_boo)
print("3 boo", tercer_boo)

print("-"*30)
# Clasificaciones de caracteres

texto1 = "123abc"
texto2 = "123$abc"

print("Es alpha numérico:", texto2.isalnum()) # False -> $ no pertenece a alfabeto/numero
print("Es un digito:", texto1.isdigit()) 

print("-"*30)
# Format

texto3 = "Hola mundo"
print('|', texto3.center(20), '|')
print(texto3.rjust(20), "|")

print("-"*30)
texto4 = "                  HOla           m    undo"
print(texto4)

print("-"*30)
print(texto4.lstrip())

print("-"*30)
print(texto4.rstrip(), "|")

print("-"*30)
print('#'+texto4.strip()+'#') # strip() -> Elimina los espacion en blanco que hay al principio y al final. Por defecto son espacios, pero si se pone otro caracter split('@') -> quita los @ del prinicio y del final

print("-"*30)
print(texto4.replace(" ","")) # replace() -> Reemplaza los espacios " " por ""(sin espacio)

texto5 = "          HOlA qUE tAL"
# Cambiarlo a -> Hola Que Tal

texto6 = texto5.title() # Pone la primera letra de cada palabra en mayus y el resto minus
texto6 = texto6.strip() # Elimina los espacion en blanco que hay al principio y al final.
texto6 = ' '.join(texto6.split())
print(texto6)

texto7 = "Hola" 
print(texto7.zfill(15)) # 00000000000Hola | zfill()-> Rellena con 0 15 espacios al inicio.

texto8 = "10"
print(texto8.zfill(8)) # 00000010 | Rellena con 8 ceros delante. Sirve sobretodo para Bytes

