import numpy as np
import math
from fractions import Fraction
from Simplex import Simplex, zero, one, ngone, print_table
from TwoPhase import TwoPhase
from math import floor
class Gomory:
    def __init__(self,tbl: np.asarray):
        self.M = tbl.shape[0] - 1 # num old constraint 
        self.N = tbl.shape[1] - 1  #num old variable
        self.m = self.M  # no. new constraint and new vars when add gomory cut
        self.n =self.N
        self.base = np.full(self.m, -1, dtype=int)
        self.tbl = tbl 
        self.result = np.empty(self.n, dtype = Fraction)


    
    def twoPhaseGomory(self,count: int):
        print("The " + str(count) + "-th :")
        print("The initial: ")

        print_table(self.tbl)
        print('Base = ', self.base)

        solver = TwoPhase(self.tbl)

        if(solver.Solve() != True):
            print("The problem nohave infisible solution")
            return -1

        tblLP = solver.tbl
        baseLP = solver.base

        self.result = np.full(self.N,zero,dtype=Fraction)

        p = -1

        for i in range(self.m):
            if(baseLP[i] >= self.N):
                continue
            self.result[baseLP[i]] = tblLP[i][self.n]/tblLP[i][baseLP[i]]
            if((self.result[baseLP[i]].denominator != 1)):
                p = i
                break
        
        if (p == -1):
            return 1

        add_tbl = np.empty((self.m +2, self.n +2), dtype = Fraction)
        add_tbl[self.m+1][self.n] = zero
        add_tbl[self.m +1][self.n +1] =self.tbl[self.m][self.n]
        for j in range(self.n):
            add_tbl[self.m +1][j] = self.tbl[self.m][j]

        add_tbl[self.m][self.n]  = ngone

        add_tbl[self.m][self.n +1] = tblLP[p][self.n] - floor(tblLP[p][self.n])
        
        for j in range(self.n):
            add_tbl[self.m][j]  = tblLP[p][j] - floor(tblLP[p][j])
        
        
        for i in range(self.m):
            for j in range(self.n):
                add_tbl[i][j] = tblLP[i][j]
            add_tbl[i][self.n] = zero
            add_tbl[i][self.n + 1] = tblLP[i][self.n]
        
        add_b  = np.empty(self.m +1, dtype = int)

        for i in range(self.base.size):
            add_b[i]  = baseLP[i]
        
        add_b[self.m] = self.n

        self.tbl = add_tbl
        self.base = add_b
        self.m +=1
        self.n += 1
        
        print("ending loop " + str(count) )
        return 0


    def solver(self):
        count: int
        count = 0
        while(True):
            count = count +1
            res = self.twoPhaseGomory(count)
            if(res == -1):
                return False
            elif(res == 1):
                break
        return True

def main():
    # test chuc nang cua file
    f = open("data/gomory_04", "r")
    lines = f.read().split('\n')
    parts = lines[0].split()
    m = int(parts[0]) # No constraints
    n = int(parts[1]) # no variables
    tbl = np.empty((m+1, n+1), dtype = Fraction)

    for i in range(m):
        parts = lines[i+1].split()
        for j in range(n+1):
            tbl[i][j] = Fraction(parts[j])

    parts = lines[m+1].split()
    for j in range(n):
        tbl[m][j] = Fraction(parts[j])
    tbl[m][n] = zero

  
    solver  =Gomory(tbl)
    if(solver.solver() == True):
        result = solver.result
        for i in range(n):
            print("x[" + str(i) +"] = " + str(result[i]))


if __name__ == "__main__":
    main()








            
