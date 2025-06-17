import sys


def str_up_case(string):
    """
    Devuelve un nuevo string con las letras en mayúscula
    """
    print(string.upper())

def main():
    if (len(sys.argv) == 2):
        string = str(sys.argv[1])
        str_up_case(string)
    else:
        print("Uso: python str_up_case.py <string>")

if __name__=="__main__":
    main()