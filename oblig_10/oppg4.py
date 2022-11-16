import math
import numpy as np

# Shanks algoritme for å løse DLP for p=41, a_list=5, b_list=3
def shank(p:int, a:int, b:int):
    a_list = []
    b_list = []
    m = math.ceil(math.sqrt(p))
    for j in range(0, m):
        val = (pow(a,m*j))%p
        a_list.append(val)
    for j in range(0,m):
        val = (b*pow(a,-j,p))%p
        b_list.append(val)
    return m,a_list,b_list


if __name__ == '__main__':
    
    p = 41
    a = 6
    b = 3
    
    b_index, a_index = 0,0
    
    common_val = 0
    
    m,a_list,b_list = shank(p, a,b)
    
    print(a_list)
    print(b_list)
    
    log = lambda base, x: np.log(x)/np.log(base)
    func = lambda m,j,i,p: (m*j +i)%p
    
    for i in range(len(a_list)):
        if b_list[i] in a_list:
            common_val = b_list[i]
            b_index = i
    a_index = a_list.index(common_val)
    
    print("\ncommon value {} at a_index: {}, b_index: {}".format(common_val,a_index, b_index))
    val = func(m,a_index, b_index,p)
    print("\nlog_{} {} = ({}*{}+{})%p={}".format(a,b,m,a_index,b_index,val))
    
    calc = lambda a,val, p: (a**val)%p
    
    print("\n({}^{}) mod {} = {}, som vi ser stemmer med verdien til b".format(a,val,p, calc(a,val,p)))
    
    
            

    
    
    