from sympy import sieve


class RSA:
    
    def __init__(self, p, q):
        self.p = p
        self.q = q
        
    def gcd(self, a, b) -> int:
        r = a%b
        while(r):
            a = b
            b = r
            r = a%b
        return b
            
    def ext_euclid(self, a, b):
        if a == 0 :
            return b,0,1
        gcd,x1,y1 = self.ext_euclid(b%a, a)
        x = y1 - (b//a) * x1
        y = x1
        return gcd,x,y
            
            
    def rsa_cryptate(self, m, p, q):
        return (m**p)%q

    def rsa_decryptate(self, e, p, q):
        return (e**p)%q


    def rsa_keygen(self):
        n = self.p*self.q
        phi = (self.p-1)*(self.q-1)
        e = 3
        while(self.gcd(e, phi) != 1):
            e += 1
        gcd, d, y = self.ext_euclid(e, phi)
        return e, n, d

       
        
if __name__ == '__main__':
    
    # list of primes in range smallest 16 bit number to largest 16 bit number
    primes = sieve.primerange(int(0b1000000000000000), int(0b1111111111111111))
    primes_list = list(primes)
    # print(primes_list)
    
    rsa = RSA(primes_list[0], primes_list[1])
    
    # Prøvde å finn riktige verdier men funket ikke helt
    # e,n,d = rsa.rsa_keygen()
    # print("e: {},n: {} ,d: {}".format(e, n, d)) 
    
    
    print((923827*1388389)%3)
    
    # Fikk litt hjelp med å finne riktige keypair
    encrypted = rsa.rsa_cryptate(12345, 3, 1388389)
    print("Meldingen '12345' kryptert: ", encrypted)
    decrypted = rsa.rsa_decryptate(encrypted,923827, 1388389)
    print("Meldingen '{}' dekryptert: {}".format(encrypted, decrypted))
    