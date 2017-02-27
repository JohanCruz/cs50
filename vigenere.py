import cs50
import sys

def main():
    i = get_positive_int()
    parrafo(i)
    
def get_positive_int():
    
    if len(sys.argv) == 2:
        sd =sys.argv[1]
        for r in sd:
            if ord(r)<48 or ord(r)>57:
                print("error return 2 ")
                exit(2) 
        n=int(sys.argv[1])
        while n>26: 
            n=n-26
     
        return n
    else:
        print("missing command-line argument")
        exit(1)
        

def parrafo(n):
    soco = cs50.get_string()
    #for s in sys.argv:

    for c in soco:
        c2=0
        c3=0            
        d=ord(c)
        if d==32:
            print(c,end="")
            c2=3
        if d+n <91 and d+n>64:
            print(chr(ord(c)+n), end="")
            c2=2
        if d+n >96 and d+n<123:
            print(chr(ord(c)+n), end="") 
            c3=3
        if d<91 and d>64 and c2==0:
            print(chr(ord(c)+n-26), end="")
            c2=4
        if d >96 and d<123 and c3==0:
            print(chr(ord(c)+n-26), end="") 
            c3=6
        if c2+c3==0:
            print(c,end="")
        
    print(" ",end="")


if __name__ == "__main__":
    main()
    print()
    
 