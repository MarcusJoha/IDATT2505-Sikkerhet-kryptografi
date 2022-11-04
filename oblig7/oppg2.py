

def modulo_table_and_mult_invers(n: int):
    table = []
    mult_pl_invers = []
    for i in range(1,n):
        row = []
        for j in range(1,n):
            calc = (i*j)%n
            row.append(calc)
            if calc == 1:
                mult_pl_invers.append("({}*{})%{} = 1 ".format(i,j,n))
        table.append(row)
    return table, mult_pl_invers


def print_table(table, n):
    for i in range(0,n):
        print(table[i][:])
        
        
def bruteforce_mult_inverse(num: int, mod_num: int): 
    for i in range(1,mod_num):
        if (num*i)%mod_num == 1:
            return "{}*{}%{}=1".format(num,i,mod_num)



if __name__ == "__main__":
    table, multpl_inv = modulo_table_and_mult_invers(12)
    
    print_table(table, 11)
    
    
    print("\n ------Multiplikativ invers for mod 12--------")
    print(multpl_inv)
    
    
    print("\n ------Multiplikativ invers for mod 11--------")
    table, multpl_inv = modulo_table_and_mult_invers(11)
    print(multpl_inv)
    
    
    print("\n-------Bruteforce multiplikativ invers 11 modulo 29-------")
    print(bruteforce_mult_inverse(11,29))
    
    
    # e) Formuler en sammenheng mellom det at 'a' har en multiplikativ invers modulo n,
    # og om tallet har felles faktorer med n
    
    # ???