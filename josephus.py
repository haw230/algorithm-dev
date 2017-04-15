def main():
    lt = ask()
    if len(lt) % 2 == 0:
        print("The survivor is " + josephus(lt[0::2], True))
    else:
        print("The survivor is " + josephus(lt[0::2], False))

def ask():
    a = None
    while a is None:
        try:
            a = int(input("Enter a number: "))
        except Exception:
            print("Not an integer value...")
    return range(1, a + 1)
    
def josephus(comrades, even): #even means first is spared
    soldiers = comrades
    print(soldiers)
    if len(soldiers) == 1:
        return str(soldiers[0])
    if even: #first guy lives
        if len(soldiers) % 2 == 0:
            return josephus(soldiers[0::2], True)
        else:
            return josephus(soldiers[0::2], False)
    else: #first guy dies
        if len(soldiers) % 2 == 0:
            return josephus(soldiers[1::2], False)
        else:
            return josephus(soldiers[1::2], True)
            
if __name__ == "__main__":
    main()