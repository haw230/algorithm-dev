def main():
    p_or_m = str(raw_input("Permutation ('P') or Combination ('C')? "))
    n = int(input("How many items? "))
    r = int(input("How many chosen? "))
    if p_or_m == 'P':
        print("There are " + str(perm(n, r)) + " arrangements")
    else:
        print("There are " + str(com(n, r)) + " arrangements")
def perm(n, r):
    return factorial(n) / factorial(n - r)

def com(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

def factorial(num):
    if(num <= 1):
        return 1
    return factorial(num - 1) * num
    
if __name__ == "__main__":
    main()