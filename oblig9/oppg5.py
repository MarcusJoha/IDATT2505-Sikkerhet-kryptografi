
from math import factorial
from sympy import sieve

def gcd(a, b) -> int:
        r = a%b
        while(r):
            a = b
            b = r
            r = a%b
        return b

def pollard(n):
    a = 2
    B = factorial(5)
    A = (a**B)%n
    d = gcd((A-1), n)
    while(d <= 1):
        a += 1
        A = (a**B)%n
        d = gcd(A-a, n)
    return d

def factor_n(n, num_of_tries):
    for d in range(num_of_tries):
        s = int((n + d ** 2) ** (1 / 2))
        q = s + d
        p = s - d
        if p * q == n:
            return p, q
    return -1, -1

    

if __name__ == '__main__':
    
    # a) 
    p = pollard(1829)
    q = 1829/p
    print("a)\np: {}, q: {}".format(p,q))
    
    # b)
    p,q = factor_n(18779, 80)
    print("\nb)\np: {}, q: {}".format(p,q))
    
    # c)
    p = pollard(6319)
    q = 6319/p
    print("\nc)\np: {}, q: {}".format(p,q))
    