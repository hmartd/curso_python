import sys
import string

def print_char(char):
    """
    Imprime un caracter
    """
    print(char)

def main():
    if len(sys.argv) == 2:
        char = sys.argv[1]
        if (char not in string.ascii_letters):
            print("ERROR: Tiene que ser un caracter.")
        else:
            print_char(char)
    else:
        print("Uso: python print_char.py <char>")

if __name__=="__main__":
    main()