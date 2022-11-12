
def lsfr_1(k):
    bitstring = "{:04b}".format(k)
    period = 0
    key = 0
    while (k != key):
        bit = (int(bitstring[0]) + int(bitstring[1]) + int(bitstring[2]) + int(bitstring[3]))%2
        bitstring = bitstring + str(bit)
        key = int(bitstring)&0b1111
        period += 1
        bitstring = "{:04b}".format(key)
    return period, key

def lsfr_2(k):
    bitstring = "{:04b}".format(k)
    period = 0
    key = 0
    while (k != key):
        bit = (int(bitstring[0]) + int(bitstring[3]))%2
        bitstring += str(bit)
        key = int(bitstring)&0b1111
        period += 1
        bitstring = "{:04b}".format(key)
    return period, key


# Annet eksempel jeg prøvde
def lsfr(k):
    key = k
    periods = 1
    newbit = (key ^ (key >> 1)) & 1
    key = (key >> 1) | (newbit << 3)
    while(key != k):
        periods += 1
        newbit = (key ^ (key >> 1)) & 1
        key = (key >> 1) | (newbit << 3)
        
    return periods, key

def print_answer(func, k):
    rounds, key = func(k)
    print("Perioder: {}, siste key: {:04b}".format(rounds, key))

if __name__ == '__main__':   
      
    print("Oppgave 1")
    print_answer(lsfr_1, 0b1000)
    print_answer(lsfr_1,0b0011)
    print_answer(lsfr_1,0b1111)
    
    print("\nOppgave 2")
    print_answer(lsfr_2, 0b1000)
    print_answer(lsfr_2,0b0011)
    print_answer(lsfr_2,0b1111)
    
    