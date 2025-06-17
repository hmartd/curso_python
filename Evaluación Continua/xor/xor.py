def xor_manual(a, b):
    """
    Operación XOR. A XOR B
    """
    i = 0
    result_xor = 0

    while i < 8:
        bit_a = (a >> i) & 1     # 'a >> i' -> desplaza los bits de a hacia la derecha i posiciones  '& 1' -> se queda solo con el bit que quedó más a la derecha
        bit_b = (b >> i) & 1
       
        xor_bits = (bit_a + bit_b) % 2
        result_xor |= (xor_bits << i) # '|=' es un OR.  (xor_bits << i) -> Desplaza el bit xor_bits a la izquierda i posiciones.

        i = i + 1

    return result_xor

a = int(input("A: "))
b = int(input("B: "))
result = xor_manual(a,b)
print(result)
print(chr(result))