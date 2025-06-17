import sys
import string

def str_inv(cadena):
    """
    Imprime la cadena invertida seguida de una nueva línea.
    """
    result = cadena[::-1]
    print(result)
    print()

def main():
    if (len(sys.argv) == 2):
        string = str(sys.argv[1])
        str_inv(string)
    else:
        print()

if __name__=="__main__":
    main()