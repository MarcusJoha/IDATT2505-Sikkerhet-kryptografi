
alpha = "abcdefghijklmnopqrstuvwxyzæøå"

# Vigenere cryptation
def cryptate(msg, key):
    n = len(key)
    crypt = ""
    for i in range(0,len(msg)):
        x = alpha.find(msg[i])
        y = alpha.find(key[i%n])
        crypt += alpha[(x+y)%29]
    return crypt
            

def decryptate(msg, key):
    n = len(key)
    decrypt = ""
    for i in range(0,len(msg)):
        x = alpha.find(msg[i])
        y = alpha.find(key[i%n])
        index = (x-y)%29
        decrypt += alpha[index]
    return decrypt
    


if __name__ == "__main__":
    
    
    msg = "snarthelg"
    key = "torsk"
    
    # Usikker om det skal være med store bokstaver og hvilke index de skulle ha
    # Også litt usikker om man skulle ha med mellomrom og hvilken index den skal ha
    
    # a)
    crypt = cryptate(msg, key)
    print(crypt)
    
    # Sjekker de-krypteringa
    de_cry = decryptate(crypt, key)
    print(de_cry)
    

    # b)
    decrypt = decryptate("qzqobvcaffksdc", "brus")
    print(decrypt) #pizza eller taco
    
    
    