"""
Ejercicio 06: Verificando la integridad de un mensaje con funciones hash

Objetivo: Usar funciones hash para verificar que un mensaje no ha sido alterado durante su transmisión

Instrucciones:
1. Crea una función llamada `calc_hash` que reciba un string `mensaje` y devuelva su hash SHA256 como string hexadecimal
2. Crea una función llamada `v_message` que reciba:
   - `mensaje_original`: string original
   - `hash_recibido`: string hash que acompaña al mensaje
   - La función debe calcular el hash del mensaje y compararlo con `hash_recibido`
   - Si coinciden, devuelve `True`. Si no, devuelve `False`
3. Guarda el resultado de `verificar_mensaje("Hola mundo", "<hash_correcto>")` en una variable llamada `verificacion`
4. Imprime el contenido de `verificacion`

Requisitos:
- Utiliza `hashlib` y SHA256
- Documenta tus funciones con DocStrings
"""
import hashlib

# Tu programa empieza aquí:
def calc_hash (mensaje):
    """
    Calcula Hash SHA256
    Entrada: String
    Salida: Hash SHA356 en Hex
    """
    n_bytes = mensaje.encode() # Convierte texto en Bytes REQUIERE HASHLIB
    hash_obj = hashlib.sha256(n_bytes) # Codifica a SHA256
    hash_hex = hash_obj.hexdigest() # Convierte a Hexadecimal
    return hash_hex


def v_message(mensaje_original, hash_recibido):
    """
    Compara el hash del mensaje_original calculado por mi, con el hash real del mensaje_original. Devuelve True si son iguales.
    Entrada: String, String
    Salida: True (Si el hash es igual) | False (Si el hash es diferente)
    """
    hash = calc_hash(mensaje_original)
    return hash == hash_recibido

verificacion = v_message("Hola mundo", "ca8f60b2cc7f05837d98b208b57fb6481553fc5f1219d59618fd025002a66f5c")
print(verificacion)



