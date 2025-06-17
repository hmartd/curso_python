
import string

def print_reverse_alphabet():
    """
    Prints the uppercase alphabet on a single line, in descending order.
    """
    alphabet = string.ascii_uppercase
    print(alphabet[::-1])

def main():
    print_reverse_alphabet()

if __name__=="__main__":
    main()