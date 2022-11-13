import sympy as sy

def euclid(a, b):
    r = a%b
    while(r):
        a = b
        b = r
        r = a%b
    print(" GDC: " + str(b))

def ext_euclid(a, b):
    # Base Case
    if a == 0 :
        return b,0,1
             
    gcd,x1,y1 = ext_euclid(b%a, a)
     
    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1
     
    return gcd,x,y

def crypt_rsa(m, k):
    return (m**k[0])%k[1]

def decrypt_rsa(e, k):
    return (e**k[0])%k[1]

if __name__ == "__main__":
    #relativt prim betyr at gdc = 1
    #print(list(sy.sieve.primerange(500, 2000)))
    encrypted = crypt_rsa(12345, [3, 1388389])
    print("Meldingen '12345' kryptert: ", encrypted)
    decrypted = decrypt_rsa(encrypted,[923827, 1388389])
    print("Meldingen '{}' dekryptert: {}".format(encrypted, decrypted))
    