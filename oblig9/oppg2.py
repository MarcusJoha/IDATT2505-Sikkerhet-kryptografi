
def caesar_chiffer(x):
    return (x+3)%2**4


def cbc_mac(message):
    iv = 0b0
    stored = message[0]^iv
    for i in range(1,len(message)):
        new = stored^message[i]
        stored = caesar_chiffer(new)
    return "{:04b}".format(new)

if __name__ == '__main__':
    
    x = [0b1101, 0b1111, 0b1010, 0b0001]
    
    print(cbc_mac(x))