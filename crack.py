import pwd
import crypt
import getpass
import cs50
import sys
import crypt
from hmac import compare_digest as compare_hash


# Tarea principios basicos de computacion cientifica cs50
# https://www.google.com/search?client=firefox-b-d&q=crack+cs50


def combination():
    for p in range(65, 122):
        for q in range(65, 122):
            for r in range(65, 122):
                for s in range(65, 122):
                    hashed = crypt.crypt(chr(p)+chr(q)+chr(r)+chr(s), salt=a+b)
                    if compare_hash(plaintext1, crypt.crypt(chr(p)+chr(q)+chr(r)+chr(s), hashed)):
                        #print(chr(p)+chr(q)+chr(r)+chr(s))
                        pp=chr(p)+chr(q)+chr(r)+chr(s)
                        return pp
                        break 
    
if len(sys.argv) == 2:
    plaintext1 =sys.argv[1]
else:
        print("missing command-line argument")
        exit(1)    
#plaintext1 = cs50.get_string()


plaintext=plaintext1
n=1
b="d"
for r in plaintext:
    if n==1:
       a=chr(ord(r))
    if n==2:
       b=chr(ord(r))
    n=n+1

#plaintext= plaintext.lstrip(a)
#plaintext= plaintext.lstrip(b)
#print(plaintext)

#print(a,b)

#hashed = crypt.crypt(plaintext, salt=a+b)

#print(a+b)
pp=combination()
print(pp)

def main():
    return 0

if __name__ == "__main__":
    main()


#print(hashed)
#if not compare_hash(hashed, crypt.crypt(plaintext, hashed)):
 #  raise print("hashed version doesn't validate against original", end="")

