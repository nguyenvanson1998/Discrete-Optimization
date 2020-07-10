import numpy as np
import math
from fractions import Fraction


from Simplex import Simplex, zero, one, ngone, print_table

class TwoPhase:
    def __init__(self, tbl: np.asarray):
        self.M = tbl.shape[0] -1   # num constraint
        self.N = tbl.shape[1] -1 #num variables
        #tbl last row is objtive last colum is value 
        self.base = np.empty(self.M, dtype = 'int')
        self.tbl = np.empty((self.M+1, self.N +1), dtype = Fraction)
        for i in range (self.M+1):
            for j in range(self.N +1):
                self.tbl[i][j] = Fraction(tbl[i][j])

    #Find a basic feasible solution
    def BFS(self):
        solver: bool
        # giai bai toan voi dau vao chua them bien
        tbl = np.empty((self.M+1, self.M + self.N +1), dtype = Fraction)
        b = np.empty(self.M , dtype = 'int') # b[i] =k if k-th is the base variable

        # xac dinh he so cac bien thuc
        for i in range (self.M):
            for j in range(self.N):
                tbl[i][j] = self.tbl[i][j]
        
        for i in range (self.M):
            for j in range(self.N, self.N +self.M ):
                tbl[i][j] = zero
            tbl[i][self.N+i] = one
            tbl[i][self.N +self.M] = self.tbl[i][self.N]
            b[i] = self.N +i
        
        for j in range (self.N):
            tbl[self.M][j] = zero
        
        for j in range(self.N, self.N +self.M):
            tbl[self.M][j] = ngone
        tbl[self.M][self.M+ self.N] = zero

        print("BFS with SLack vars")
        print_table(tbl)
        print('Base =  ', b)

        sim = Simplex(tbl, b)
        if(sim.Solve() != True):
            solver = False
            return solver
        
        b = sim.base
        tbl = sim.tbl

        print("Anwser after Simplex 1-th")
        print_table(tbl)
        print('Base' ,b)

        if(tbl[-1][-1] != zero ):
            print("Not have BFS!")
            solver = False
            return solver
        
        for i in range (self.M):
            for j in range(self.N):
                self.tbl[i][j] = tbl[i][j]
            self.tbl[i][self.N] = tbl[i][self.N +self.M]
        
        flag = np.full(self.N,False, dtype = bool)
        for  i in range(self.M):
            if(b[i]< self.N):
                self.base[i] = b[i]
                flag[b[i]] = True
        for i in range(self.M):
            if(b[i] >= self.N):
                for j in range(self.N):
                    if(flag[j] == False):
                        self.base[i] = j
                        flag[j] = True
                        break
        solver = True
        return solver


    def Solve(self):
        print(" The intit BFS:")
        findBFS = self.BFS()
        if(findBFS != True):
            print("No have BFS!")
            return False
        print("Find the LP maximum solution: ")
        print("First Step: ")
        print_table(self.tbl)
        print('Base = ', self.base)
        simplex = Simplex(self.tbl, self.base)
        if(simplex.Solve() != True):
            print("Can't solve phase 2")
            return False
        self.tbl = simplex.tbl
        self.base = simplex.base

        print("LP optimum solution!")
        print_table(self.tbl)
        print('Base = ', self.base)

        return True

def main():
    # test chuc nang cua file
    f = open("data/twophase_01", "r")
    lines = f.read().split('\n')
    parts = lines[0].split()
    m = int(parts[0])
    n = int(parts[1])
    tbl = np.empty((m+1, n+1), dtype = Fraction)

    for i in range(m):
        parts = lines[i+1].split()
        for j in range(n+1):
            tbl[i][j] = Fraction(parts[j])

    parts = lines[-1].split()
    for j in range(n):
        tbl[m][j] = Fraction(parts[j])
    tbl[m][n] = zero  
    print('Input table') 
    print_table(tbl)
    TwoPhasesimplex = TwoPhase(tbl)
    TwoPhasesimplex.Solve()
    print("the maximum Values: " + str(TwoPhasesimplex.tbl[m][n]))
    

if __name__ == "__main__":
    main()
       

        


        
        








