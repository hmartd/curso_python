import sys
import string

def repeat_case(cadena):
    """
    Imprime el string repitiendo cada caracter alfabético tantas veces como su índice alfabético.
    """
    abc_lowercase = string.ascii_lowercase
    abc_uppercase = string.ascii_uppercase
    result = ""
    idx = 0

    for elem in cadena:
        if (elem in abc_lowercase):
            idx = abc_lowercase.index(elem) # Busca el índice del elemento en la cadena del abecedario en minúsculas
            result += elem*(idx+1)
        elif (elem in abc_uppercase):
            idx = abc_uppercase.index(elem)
            result += elem*(idx+1)
        else:
            result += elem

    print(result)

def main():
    if (len(sys.argv) == 2):
        string = str(sys.argv[1])
        repeat_case(string)
    else:
        print()

if __name__=="__main__":
    main()