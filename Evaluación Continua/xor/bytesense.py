
def bytes_transform(string, slicing, verbose):
    """
    Modifica un string en bytes y devolverá el valor en hexadecimal.
    """
    # String to Bytes
    byte_text = string.encode('utf-8')

    # Extract bytes to evens bytes
    bytes_evens = byte_text[::2]

    # Concat evens bytes + bytes original
    bytes_concat = byte_text + bytes_evens

    bytes_finish = bytearray(bytes_concat) # Crea un bytearray

    if (verbose == "True") or (verbose == "T") or (verbose == "t"):
        print("-" * 50)
        i = 0
        len_bytes = len(bytes_finish)
        while i < len_bytes:
            original = chr(bytes_finish[i])
            key = (i + slicing) % 256
            bytes_finish[i] = bytes_finish[i] ^ key
            finish = chr(bytes_finish[i])
            print("[" + str(i) + "]" + "Original byte:" + original + "--> result:" + finish)
            i += 1
    else:
        i = 0
        len_bytes = len(bytes_finish)
        while i < len_bytes:
            bytes_finish[i] = bytes_finish[i] ^ (i + slicing) % 256 # ^ -> Operador XOR (bit a bit)
            i += 1
        print(bytes_finish)
    
    # Convert to Hex
    result = bytes_finish.hex()
    return result

# ======== PRUEBA INTERACTIVA ======== #
text_input = input("Introduce un texto para transformar: ")
slicing = int(input("Slicing: "))
verbose = input("Verbose [True/False]: ")
byte_sense = bytes_transform(text_input, slicing, verbose)
print("\nResultado transformado:", byte_sense)