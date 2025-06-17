

def print_comb2():
    """
    Prints all possible combinations of two numbers (XX XX) between 0 and 99, in ascending order.
    """
    result = ""

    for i in range(100):
        for j in range (i+1, 100):
            result += (f"{i:02d} {j:02d}, ") # Formato con dos dígitos de i y dos dígitos de j: ii jj

    # Elimina el último ",_"
    result = result[:-2]
    print(result)

def main():
    print_comb2()


if __name__ == "__main__":
    main()