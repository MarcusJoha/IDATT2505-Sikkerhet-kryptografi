
bitstring = "{:04b}".format(0b1001)

bit = (int(bitstring[0]) + int(bitstring[1]) + int(bitstring[2]) + int(bitstring[3])) % 2
print(bit)
bitstring = bitstring + str(bit)
print(bitstring)
z = int(bitstring, 2)& 0b1111
print("{:04b}".format(z))

x = 0b1111
# print("{:04b}".format(x))

y = (x << 2)
print("{:04b}".format(y))