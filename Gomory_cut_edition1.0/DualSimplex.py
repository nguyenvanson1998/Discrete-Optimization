import numpy as np
import math
from fractions import Fraction
from Simplex import Simplex, zero, one, ngone, print_table
from TwoPhase import TwoPhase
from math import floor

class DualSimplex(Simplex):
    def __init__(self, tbl:np.asarray, base: []):
        super().__init__(tbl, base)
    
    
    def Solve(self):
        print("The dual program : ")
        x = self.solveDual()
        if(x == False):
            return False
        print("The dual solution:")
        print_table(self.tbl)
        print('Base = ', self.base)

        print("Solve the Primal problem:")
        if(super().Solve() != True):
            return False
        
        print("Primal Solution:")
        print_table(self.tbl)
        print('Base = ',self.base)
        return True
    
    



    
    def solveDual(self):
        self.nomalize()
        solve_able : bool
        while True:
            p :int 
            q: int

            p = 0
            while p < self.M:
                if(self.tbl[p][self.N] < 0):
                    break
                p = p+1

            if(p >= self.M):
                solve_able = True
                break
            q  = 0
            while q < self.N:
                if(self.tbl[p][q] < 0):
                    break
                q = q + 1

            if q >= self.N :
                solve_able = False
                break

            for i in range(q+1, self.N):
                if(self.tbl[p][i]< 0):
                    if(self.tbl[self.M][i]/self.tbl[p][i] < self.tbl[self.M][q]/ self.tbl[p][q]):
                        q = i
           
            self.pivot(p,q)
        return solve_able






