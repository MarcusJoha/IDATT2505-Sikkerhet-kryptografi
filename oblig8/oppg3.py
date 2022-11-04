import array as arr


alpha = "abcdefghijklmnopqrstuvwxyzæøå"


def encrypt(text, key:int):
    stream = alpha[key]+ text[:(len(text)-1)]
    encry = ""
    for i in range(0,len(text)):
        p = alpha.find(text[i])
        c = alpha.find(stream[i])
        index = (p+c)%29
        encry += alpha[index]
    return encry

def decrypt(text, key:int):
    k = key
    decry = ""
    for i in range(0,len(text)):
        c = alpha.find(text[i])
        p = alpha.find(alpha[k])
        decry += alpha[(c-p)%29]
        k = alpha.find(decry[i])
    return decry

def numbers_tostring(numbers):
    str = ""
    for num in numbers:
        str += alpha[num]        
    return str



if __name__ == '__main__':
    
    print(encrypt("goddag", 17))
    
    numbers = arr.array('i',[23, 8, 23, 12, 21, 2, 4, 3, 17, 13, 19])
    str = numbers_tostring(numbers)
    print(decrypt("xurgdg", 17)) # dekryptert til goddag
    
    print(decrypt(str, 5)) # steinsprang
