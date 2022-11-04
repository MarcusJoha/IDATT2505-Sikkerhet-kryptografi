
alpha = " abcdefghijklmnopqrstuvwxyzæøå,."

def cbc_crypt(text):
    crypt = ""
    xor = lambda x, y: x ^ y
    ce = lambda num, shif: (num+shif)%32
    current = ce(xor(13, alpha.find(text[0])), 3)
    crypt += alpha[current]
    for i in range(1, len(text)):
        next = xor(current, alpha.find(text[i]))
        current = ce(next, 3)
        crypt += alpha[current]
    return crypt

def cbc_decrypt(text):
    decrypt = ""
    xor = lambda x,y: x^y
    ce_re = lambda num, shif: (num-shif)%32
    for i in range(len(text)-1,0,-1):
        current = ce_re(alpha.find(text[i]), 3)
        next = alpha.find(text[i-1])
        index = xor(next, current)
        decrypt += alpha[index]
    current = ce_re(alpha.find(text[0]), 3)
    index = xor(13, current)
    decrypt += alpha[index]
    return decrypt
    

if __name__ == '__main__':

    print(cbc_crypt("aaaaaa"))
    print(cbc_crypt("dette er en test"))
    
    print(cbc_decrypt("oqsuwy"))
    
    print(cbc_decrypt("qvxæyy hkgdgk,,oqhdnc")[::-1])
    