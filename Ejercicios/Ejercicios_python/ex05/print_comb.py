
def print_comb():
    """
    Prints all possible combinations of three distinct digits in ascending order
    """
    result = ""

    for i in range(10):
        for j in range(i+1, 10):
            for k in range(j+1, 10):
                result += (f"{i}{j}{k}, ") # ijk = 012, 013, 014...
    
    # Eliminar el último ",_"  
    result = result[:-2]
    print(result)

        

    

    

def main():
    print_comb()


if __name__ == "__main__":
    main()