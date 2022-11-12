import string

def midsquare(x):
    h = (x**2) % (2**8)
    return "{}".format(bin(h)[4:8].zfill(8))

def hmac(key, message, opad, ipad):
    k_opad = "{:04b}".format(key^opad)
    k_ipad = "{:04b}".format(key^ipad)
    crypt = k_opad + midsquare(int(k_ipad + message, 2))
    return crypt
    

if __name__ == '__main__':

    # a)
    # HMAC til melding 0110
    print(hmac(int('1001',2), '0110', int('0101', 2), int('0011',2)))
    
    # b)
    # Mottar meldig 0111 og HMAC 0100. Grunn til å tro at melding ikke er autentisk
    hmac(int('1001', 2), '0111', int('0101', 2), int('0011', 2))
    
    # Svar: vi ser at hmac til a) og b) er lik som er grunn til å tro at melding er autentisk
    
    