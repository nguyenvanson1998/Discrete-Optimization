import numpy as np
from fractions import Fraction


zero = Fraction(0)
one = Fraction(1)
ngone = Fraction(-1)

class Simplex:
    def __init__(self, tbl, base):
        self.M = base.size  # num constrains
        self.N = tbl[0].size - 1       # num variables
        self.tbl = tbl 
        self.base = base #  gia tri b[i] la bien co so
    
    # finding the pivot each round
    def pivot(self,p : int , q: int ):
        self.base[p] = q

        # cap nhat trong so cho cac phan tu khong nam tren hang p cot q
        for i in range(0, self.M + 1 ):
            for j in range(0, self.N+1 ):
                if (i != p and j != q):
                    self.tbl[i][j] -= self.tbl[p][j]*self.tbl[i][q]/self.tbl[p][q]
        #  bien o cot q ma khac hang p thi bi khu gauss
        for i in range(0, self.M+1):
            if ( i != p ):
                self.tbl[i][q] = zero
        # bien o hang p cot khac q ta co  gia tri bang chia co gia tri cua pivot
        for  j in range(0, self.N+1):
            if (j != q):
                self.tbl[p][j] /= self.tbl[p][q]
        # bien tbl[p][q] = 1
        self.tbl[p][q] = one


    def nomalize(self):

        # dam bao cac he so bien co so = 1
        for i in range( self.M):
            c = self.tbl[i][self.base[i]]
            for j in range(0, self.N +1 ):
                self.tbl[i][j] /= c
        """for i in range(self.M):
            for j in range(self.N +1):
                self.tbl[i][j] /= self.tbl[i][self.base[i]]"""

        # khoi tao gia tri cho bien co so    
        for i in range(self.M) :
            c = Fraction(self.tbl[self.M][self.base[i]]/self.tbl[i][self.base[i]])
            for j in range(self.N + 1 ):
                self.tbl[self.M][j] -= c*self.tbl[i][j]
        print(">>> nomalizze")
        print_table(self.tbl)
        print ('Base = ',self.base)
    def Solve(self):
        solver : bool 
        self.nomalize()
        k = 0
    
        while True:
            k = k +1
            p : int
            q : int
            q = 0
            while q  < self.N:
                if (self.tbl[self.M][q] > 0):
                    break
                q = q + 1
            
            if (q >= self.N ) :
                solver = True
                break
            
            p = 0
            while p < self.M:
                if (self.tbl[p][q] > 0):
                    break
                p = p+1
            if (p >= self.M):
                solver = False
                break
           
            for i in range (p+1, self.M):
                if(self.tbl[i][q] > 0 ):
                    if (self.tbl[i][self.N]/self.tbl[i][q] < self.tbl[p][self.N]/self.tbl[p][q]):
                        p = i
            
            self.pivot(p,q)
                
            #print('p = ' + str(p) + ' q = ' +str(q))
            #print_table(self.tbl)
            #print('Base = ', self.base)
            
            
        
        return solver

def print_table(a):
    s = a.shape
    for i in range(s[0]):
        print(' '.join(list(map(str, list(a[i, :])))))      

def main():
    # test chuc nang cua file
    f = open("data/simplex_02", "r")
    lines = f.read().split('\n')
    parts = lines[0].split()
    m = int(parts[0])
    n = int(parts[1])
    tbl = np.empty((m+1, n+1), dtype = Fraction)
    b = np.empty(m  , dtype = 'int')

    for i in range(m):
        parts = lines[i+1].split()
        for j in range(n+1):
            tbl[i][j] = Fraction(parts[j])
        b[i] = parts[-1]

    parts = lines[-1].split()
    for j in range(n):
        tbl[m][j] = Fraction(parts[j])
    tbl[m][n] = zero   
    #print_table(tbl)
    #print(" gia tri cua b la:")
    #print(b)
    simplex = Simplex(tbl, b)
    simplex.Solve()
    print("the maximum Values: " + str(simplex.tbl[m][n]))
    

if __name__ == "__main__":
    main()

    




