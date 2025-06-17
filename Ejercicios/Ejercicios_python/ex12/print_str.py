import sys

def print_str(string):
    """
    Imprime cada caracter del string con un salto de línea
    """
    for letter in string:
        print(letter)


def main():
    if (len(sys.argv)== 2):
        string = sys.argv[1]
        print_str(string)            
    else:
        print("Uso: python print_str.py <string>")
        
if __name__ == "__main__":
    main()