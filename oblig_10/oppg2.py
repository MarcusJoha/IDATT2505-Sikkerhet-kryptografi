

def gcd(a, b) -> int:
        r = a%b
        while(r):
            a = b
            b = r
            r = a%b
        return b

def find_primitive_element(z_range: int):
    prim_el = lambda a, k: (a**k)%k
    prim_el_list = []
    for i in range(1, z_range):
        for j in range(1, z_range):
            pri_el = prim_el(i,j)
            gcd_calc = gcd(j,z_range-1)
            if (pri_el == 0 and gcd_calc == 1):
                pair = "({}^{})%{}={} og gcd({},{})={}\n".format(i,j,j,pri_el,j,z_range-1,gcd_calc)
                prim_el_list.append(pair)
    return prim_el_list


if __name__ == '__main__':

    print("1) og 3)\nPrimitive element in Zp\n")
    [print(i) for i in find_primitive_element(17)]
    