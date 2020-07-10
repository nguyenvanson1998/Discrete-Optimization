import numpy as np
import math
from fractions import Fraction
from Simplex import Simplex, zero, one, ngone, print_table
from TwoPhase import TwoPhase
from Gomory import Gomory
from math import floor
from DualSimplex import DualSimplex

class GomoryDualSimplex(Gomory):
    def __init__(self,tbl: np.asarray):
        super().__init__(tbl)


    def solver(self):
        count = 1
        res = self.twoPhaseGomory(count)
        if(res == -1):
            return False
        elif(res == 1):
            return True
        
        while True:
            count += 1
            res = self.dualSimplex(count)
            if(res == -1):
                return False
            elif(res == 1):
                break
        return True

    def dualSimplex(self, count:int):
        print("Loop " + str(count) + ":" )
        print("==>> initial")
        print_table(self.tbl)
        print(self.base)
        solve = DualSimplex(self.tbl, self.base)
        if(solve.Solve() == False):
            print("LP no have feasible Value")
            return -1
        tbl = solve.tbl
        self.base = solve.base

        for i in range(self.N):
            self.result[i] = zero
        
        p = -1

        for i in range(self.m):
            if(self.base[i] >= self.N):
                continue
            self.result[self.base[i]] = tbl[i][self.n]/ tbl[i][self.base[i]]

            if(self.result[self.base[i]].denominator != 1):
                p = i
                break

        if( p == -1):
            return 1
        
        add_tbl = np.empty((self.m+2, self.n+2), dtype = Fraction)

        add_tbl[self.m +1][self.n] = zero
        add_tbl[self.m +1][self.n+1] = self.tbl[self.m][self.n]

        for j in range(self.n):
            add_tbl[self.m +1][j] = self.tbl[self.m][j]
        
        add_tbl[self.m][self.n] = ngone
        add_tbl[self.m][self.n+1] = tbl[p][self.n] - floor(tbl[p][self.n])

        for j in range(self.n):
            add_tbl[self.m][j] = tbl[p][j] - floor(tbl[p][j])
        
        for i in range(self.m):
            for j in range (self.n):
                add_tbl[i][j] = tbl[i][j]
        
            add_tbl[i][self.n] = zero
            add_tbl[i][self.n +1] = tbl[i][self.n]
        
        add_b = np.empty(self.m +1, dtype =int)
        for i in range(self.base.size):
            add_b[i] = self.base[i]
        add_b[self.m] = self.n
      
        self.tbl = add_tbl
        self.base = add_b
        self.m = self.m +1
        self.n = self.n + 1
        print("End loop " +str(count) )
        
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

  
    solver  =GomoryDualSimplex(tbl)
    if(solver.solver() == True):
        result = solver.result
        for i in range(n):
            print("x[" + str(i) +"] = " + str(result[i]))


if __name__ == "__main__":
    main()      



    

    
