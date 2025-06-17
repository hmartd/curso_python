import sys

def str_len(string):
    """
    Cuenta el número caracteres de un string y devuelve el número encontrado.
    """
    i = 0 
    for letter in string:
        i += 1
    return i

def main():
    if (len(sys.argv) == 2):
        string = sys.argv[1]
        resultado = str_len(string)
        print(f"El número de caracteres que tiene el string '{string}' es {resultado}.")
    else:
        print("Uso: python str_len.py <string>")

if __name__ == "__main__":
    main()