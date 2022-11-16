import numpy as np

def calculate(x: int):
    row = []
    for i in range(0,x+1,1):
        for j in range(0, x+1,1):
            row.append((i**j)%11)
        print(row)
        row.clear()
        
        
def orden(n):
    indexes = []
    for i in range(1,n): indexes.append(i)
    print("\nindexes")
    print(indexes,"\n")
    ord = lambda a,k: (a**k)%n
    row = []
    for i in range(0,n):
        for j in range(1,n):
            val = ord(i,j)
            if (val == 1):
                row.append(val)
                break
            row.append(val)
        print(row)
        row.clear()


def log_table(B_range, a_range):
    log = lambda base, x: np.log(x)/np.log(base)
    row = []
    for B in range(1, B_range+1):
        for a in range(2,a_range+1):
            val = round(log(a,B),3)
            row.append(val)
        print(row)
        row.clear()
            

if __name__ == '__main__':
    
    print("a)")
    calculate(10)
    
    print("\nb)\nVi ser at (p-1) = 11-1 = 10, vi ser at orden til Z11 er når n=1,5,10.\nAlle disse deler (p-1 = 10)\n")
    orden(11)
    
    print("\nc)")
    log_table(10,10)
    
    
    