def str_inv_case(cadena):
    """
    Imprime la cadena cambiando minúsculas por mayúsculas y viceversa.
    """
    abc_lowercase = string.ascii_lowercase
    abc_uppercase = string.ascii_uppercase
    long_abc = len(abc_lowercase)
    result = ""
    idx = 0

    for elem in cadena:
        if (elem in abc_lowercase):
            idx = abc_lowercase.index(elem) 
            result += abc_lowercase[(idx+13) % long_abc]
        elif (elem in abc_uppercase):
            idx = abc_uppercase.index(elem)
            result += abc_uppercase[(idx+13) % long_abc]
        else:
            result += elem

    print(result)
    print()

def main():
    if (len(sys.argv) == 2):
        string = str(sys.argv[1])
        str_inv_case(string)
    else:
        print()

if __name__=="__main__":
    main()