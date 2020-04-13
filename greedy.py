import cs50


# Tarea principios basicos de computacion cientifica cs50
# https://www.google.com/search?client=firefox-b-d&q=greedy+cs50


def main():
    i = 100*get_money()
    count(i)
    
def get_money():
    while True:
        print("Amount of money to change? ", end="")
        n = cs50.get_float()
        if n > 0:
            break
    return n
    

def count(n):
    i = 1
    while i*25 <= n:
      i += 1
    i-=1
    
    i2 = 1
    n2=n-i*25
    while i2*10 <= n2:
        i2 += 1        
    i2-=1
        
    i3 = 1
    n3=n2-i2*10
    while i3*5 <= n3:
        i3 += 1
    i3-=1
      
    i4 = 1
    n3=n3-i3*5
    while i4 <= n3:
        i4 += 1
    i4-=1
   
        

    #print("coins 25: ", i)
    #print("coins 10: ", i2) 
    #print("coins 5: ", i3) 
    #print("coins 1: ", i4) 
    
    print("",i+i2+i3+i4, end="") 


if __name__ == "__main__":
    main()
    
