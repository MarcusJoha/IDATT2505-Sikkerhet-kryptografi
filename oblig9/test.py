def find_period_a(key):
    period = 0
    z = 0b0
    bitstring = "{:04b}".format(key)
    while(key != z):
        bit = (int(bitstring[0]) + int(bitstring[1]) + int(bitstring[2]) + int(bitstring[3])) % 2
        bitstring = bitstring + str(bit)
        z = int(bitstring, 2)&0b1111
        print("{:04b}".format(z))
        period += 1
        bitstring = "{:04b}".format(z)
    print("Antall perioder: " + str(period))

def find_period_b(key):
    period = 0
    z = 0b0
    bitstring = "{:04b}".format(key)
    while(key != z):
        bit = (int(bitstring[0]) + int(bitstring[3])) % 2
        bitstring = bitstring + str(bit)
        z = int(bitstring, 2)&0b1111
        print("{:04b}".format(z))
        period += 1
        bitstring = "{:04b}".format(z)
    print("Antall perioder: " + str(period))

if __name__ == "__main__":
    print("Oppgave 3 a)\nFinn perioden for K=> '1000' '0011' '1111'")
    find_period_a(0b1000)
    find_period_a(0b0011)
    find_period_a(0b1111)
    print("\n\nb) \nFinn perioden for samme nøkler med annen LFSR")
    find_period_b(0b1000)
    find_period_b(0b0011)
    find_period_b(0b1111)