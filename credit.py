import cs50

# Tarea principios basicos de computacion cientifica cs50
# https://www.google.com/search?client=firefox-b-d&q=credit+cs50

def main():
    i = numerodet()
    digitos(i)
    
def numerodet():
    while True:
        print("Number: ", end="")
        n = cs50.get_int()
        if n > 0:
            break
    return n
    

def digitos(n):
    m=1
    w=0
    while m<=n:
        m=m*10
        w+=1
    #print(" Los números de su credit card son: ", w) 
    
    
    j=1
    while j*(10**(w-1))<=n:
       j+=1 
    j-=1
    #print(" ", j,end="") 
    
    j2=0
    j3=0
    j4=0
    j5=0
    j6=0
    j7=0
    j8=0
    j9=0
    j10=0
    j11=0
    j12=0
    j13=0
    j14=0
    j15=0
    j16=0
    
    
    if w>1:
        n2=n-j*10**(w-1)
        j2=1
        while j2*(10**(w-2))<=n2:
           j2+=1 
        j2-=1
        #print(" ", j2,end="")     
    
    if w>2:  
        n3=n2-j2*10**(w-2)
        j3=1
        while j3*(10**(w-3))<=n3:
           j3+=1 
        j3-=1
        #print(" ", j3,end="")  
     
    if w>3:  
        n4=n3-j3*10**(w-3)
        j4=1
        while j4*(10**(w-4))<=n4:
           j4+=1 
        j4-=1
        #print(" ", j4,end="")  
    
    if w>4:  
        n5=n4-j4*10**(w-4)
        j5=1
        while j5*(10**(w-5))<=n5:
           j5+=1 
        j5-=1
        #print(" ", j5,end="")  
         
    if w>5:  
        n6=n5-j5*10**(w-5)
        j6=1
        while j6*(10**(w-6))<=n6:
           j6+=1 
        j6-=1
        #print(" ", j6,end="")    

    if w>6:  
        n7=n6-j6*10**(w-6)
        j7=1
        while j7*(10**(w-7))<=n7:
           j7+=1 
        j7-=1
        #print(" ", j7,end="") 

    if w>7:  
        n8=n7-j7*10**(w-7)
        j8=1
        while j8*(10**(w-8))<=n8:
           j8+=1 
        j8-=1
        #print(" ", j8,end="")   
        
    if w>8:  
        n9=n8-j8*10**(w-8)
        j9=1
        while j9*(10**(w-9))<=n9:
           j9+=1 
        j9-=1
        #print(" ", j9,end="")        

    if w>9:  
        n10=n9-j9*10**(w-9)
        j10=1
        while j10*(10**(w-10))<=n10:
           j10+=1 
        j10-=1
        #print(" ", j10,end="")

    if w>10:  
        n11=n10-j10*10**(w-10)
        j11=1
        while j11*(10**(w-11))<=n11:
           j11+=1 
        j11-=1
        #print(" ", j11,end="")

    if w>11:  
        n12=n11-j11*10**(w-11)
        j12=1
        while j12*(10**(w-12))<=n12:
           j12+=1 
        j12-=1 
        #print(" ", j12,end="")

    if w>12:  
        n13=n12-j12*10**(w-12)
        j13=1
        while j13*(10**(w-13))<=n13:
           j13+=1 
        j13-=1
        #print(" ", j13,end="")

    if w>13:  
        n14=n13-j13*10**(w-13)
        j14=1
        while j14*(10**(w-14))<=n14:
           j14+=1 
        j14-=1
        #print(" ", j14,end="")
        
    if w>14:  
        n15=n14-j14*10**(w-14)
        j15=1
        while j15*(10**(w-15))<=n15:
           j15+=1 
        j15-=1
        #print(" ", j15,end="")
    
    if w>15:  
        n16=n15-j15*10**(w-15)
        j16=1
        while j16*(10**(w-16))<=n16:
           j16+=1 
        j16-=1
        #print(" ", j16,end="")
    
    r2=j2*2
    r4=j4*2
    r6=j6*2
    r8=j8*2
    r10=j10*2
    r12=j12*2
    r14=j14*2   
    r16=j16*2 

    r1=0
    while r2+r1<100:
        r1+=10
    r1=100-r1
    r2=r2-r1
    r1=r1/10
    
    r3=0
    while r4+r3<100:
        r3+=10
    r3=100-r3
    r4=r4-r3
    r3=r3/10
    
    r5=0
    while r6+r5<100:
        r5+=10
    r5=100-r5
    r6=r6-r5
    r5=r5//10

    r7=0
    while r8+r7<100:
        r7+=10
    r7=100-r7
    r8=r8-r7
    r7=r7//10

    r9=0
    while r10+r9<100:
        r9+=10
    r9=100-r9
    r10=r10-r9
    r9=r9//10

    r11=0
    while r12+r11<100:
        r11+=10
    r11=100-r11
    r12=r12-r11
    r11=r11//10

    r13=0
    while r14+r13<100:
        r13+=10
    r13=100-r13
    r14=r14-r13
    r13=r13/10

    r15=0
    while r16+r15<100:
        r15+=10
    r15=100-r15
    r16=r16-r15
    r15=r15/10
    
    sumando=r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r13+r14+r15+r16+j+j3+j5+j7+j9+j11+j13+j15



    #print("suma es ",sumando) 
    

    #print(" r1: ",r1)
    #print(" r2: ",r2)
    #print(" r3: ",r3)
    #print(" r4: ",r4)
    #print(" r5: ",r5)
    #print(" r6: ",r6)
    #print(" r7: ",r7)
    #print(" r8: ",r8)
    #print(" r9: ",r9)
    #print(" r10: ",r10)
    #print(" r11: ",r11)
    #print(" r12: ",r12)
    #print(" r13: ",r13)
    #print(" r14: ",r14)

    #print("")
    
    #print("El resto de la division con 10 es: ",sumando%10)
    #print("")
    b=0
    if sumando%10==0:
        if (w==16 or w==13) and j ==4:
            print("VISA")
            b=1
    
        if (w==15 and j ==3)and(j2==4 or j2==7):
            print("AMEX")
            b=2
            
        if (w==16 and j ==5)and(j2>=1 and j2<=5):
            print("MASTERCARD") 
            b=3
    if b==0:
        print("INVALID") 
    
            
if __name__ == "__main__":
    main()
