import cs50

def main():
    i = get_positive_int()
    escalones(i)
    
def get_positive_int():
    while True:
        print("hola , ¿cuantos escalones desea entre cero y 23?", end="")
        n = cs50.get_int()
        if n > 0 and n < 24:
            break
    return n
    

def escalones(n):
    for w in range(n):
        for i in range(n-w-1):
            print(" ", end="")
        for i in range(w+1):
            print("-", end="")
        print("-")


if __name__ == "__main__":
    main()
    