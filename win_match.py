import math

def main():
    matches = ask()
    print("It takes " + str(int(math.ceil(matches / 2.0) if matches % 2 != 0 else matches / 2 + 1)) + " wins in a match of " + str(matches) + " games.")
    
def ask():
    a = None
    while a is None:
        try:
            a = int(input("How many games total? "))
        except Exception:
            print("Not an integer value...")
    return a

if __name__ == "__main__":
    main()