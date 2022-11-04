

def letters(func):
    letter_list = []
    for i in range(0,29):
        num:int = func(i) + 97
        match (num):
            case 123: # æ
                letter_list.append(chr(230))
            case 124: # ø
                letter_list.append(chr(248))
            case 125: # å
                letter_list.append(chr(229))
            case _:
                letter_list.append(chr(num))
    return letter_list


def function(func, text, alpha):
    str = ""
    numbers = []
    for letter in text:
        num:int = func(alpha.find(letter))
        str += alpha[num]
        numbers.append(num)
    return str, numbers


def function_inverse(func, text, alpha):
    str = ""
    numbers = []
    for letter in text:
        num:int = alpha.find(letter)
        index = func(num)
        str += alpha[index]
        numbers.append(index)
    return str, numbers
    

if __name__ == "__main__":
    
    alpha = "abcdefghijklmnopqrstuvwxyzæøå"
    
    # a)
    func = lambda x: (11*x-5)%29
    str_crypt, numbers = function(func,alpha,alpha)
    print(numbers)
    print(str_crypt)
    
    
    # c) 
    func_inv = lambda y: (11*y+8)%29
    letters_inv, numbers_inv = function_inverse(func_inv, str_crypt, alpha) #
    print(numbers_inv) 
    print(letters_inv) # skal være alfabetet dette her
    
    
    
    # d) kryptere alice
    crypt, num = function(func, "alice", alpha)
    print("d) : {}".format(crypt))
    
    decrypt, num = function_inverse(func_inv, crypt, alpha)
    print("decrypt : {}".format(decrypt))
    
    # e)
    decrypt2, num2 = function_inverse(func_inv,"siøpbe", alpha)
    print(decrypt2)
    
    
    
    