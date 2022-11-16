

def ext_euclid(a, b):
    if a == 0 :
        return b,0,1
             
    gcd,x1,y1 = ext_euclid(b%a, a)
    x = y1 - (b//a) * x1
    y = x1
     
    return gcd,x,y

def euclid(a, b):
    r = a%b
    while(r):
        a = b
        b = r
        r = a%b
    print(" GDC: " + str(b))

if __name__ == "__main__":
    print(ext_euclid(12**5, 19))
    print(-7%19)     

