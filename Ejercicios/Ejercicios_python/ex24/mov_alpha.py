import sys
import string

def mov_alpha(cadena):
    """
    Imprime la cadena moviendo cada letra 1 posición en el alfabeto.
    """
    abc_lowercase = string.ascii_lowercase
    abc_uppercase = string.ascii_uppercase
    long_abc = len(abc_lowercase)
    result = ""
    idx = 0

    for elem in cadena:
        if (elem in abc_lowercase):
            idx = abc_lowercase.index(elem) 
            result += abc_lowercase[(idx+1) % long_abc]
        elif (elem in abc_uppercase):
            idx = abc_uppercase.index(elem)
            result += abc_uppercase[(idx+1) % long_abc]
        else:
            result += elem

    print(result)

def main():
    if (len(sys.argv) == 2):
        string = str(sys.argv[1])
        mov_alpha(string)
    else:
        print()

if __name__=="__main__":
    main()