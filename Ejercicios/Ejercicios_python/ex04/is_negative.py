import sys

def is_negative(n):
    """
    Prints “N” or “P” depending on the sign of the integer used as a parameter. 
    If n is negative, prints “N”. If n is positive or zero, prints “P”.
    """
    if (n < 0):
        print("N")
    else:
        print("P")


def main():
    if (len(sys.argv) == 2):
        try:
            n = int(sys.argv[1])     
            is_negative(n)
        except ValueError:
            print("The argument must be an integer.")
    else:
        print("Use: python is_negative.py <integer>")


if __name__ == "__main__":
    main()