import math
import sys
from fractions import Fraction

from two_phase import Model
from dual_simplex import DualSimplex, one, zero
from simplex import print_table

class BB:
    def __init__(self, A, b, c, int_list=None):
        self.A = A
        self.b = b
        self.c = c
        self.int_list = int_list
        if self.int_list is None:
            self.int_list = list(range(len(self.c)))
        self.best = float('inf')
        self.solution = None

    def find_frac(self, x):
        for j in self.int_list:
            if x[j].denominator != 1:
                return j, x[j]
        return -1, zero

    def branching(self, node: DualSimplex):
        # print('Current node:')
        # print_table(node.a)
        # print(node.get_vars())
        if node.get_objective() >= self.best:
            return

        x = node.get_vars()
        # print(x)
        j, v = self.find_frac(x)
        if j == -1:
            self.best = node.get_objective()
            self.solution = node
            return

        # print('left')
        left = node.duplicate()
        left.add_int_cut(j, math.floor(v), True)
        if left.dual_pivot():
            self.branching(left)
        # print_table(left.a)
        # left.dual_pivot()
        #
        # print(left.get_vars())
        # print_table(left.a)

        # print('right')
        right = node.duplicate()
        right.add_int_cut(j, math.ceil(v), False)
        if right.dual_pivot():
            self.branching(right)
        # print_table(right.a)
        # print(right.get_vars())
        # right.dual_pivot()
        # print_table(right.a)

        # print(right.get_vars())

    def solve(self):
        BFS = Model(self.A, self.b, self.c)
        status = BFS.lp_solve()
        if status != Model.OPTIMAL:
            BFS.print_solution(status)
            return

        start_node = BFS.simplex
        self.branching(start_node)

        if self.solution is None:
            BFS.print_solution(Model.INFEASIBLE)
        else:
            BFS.simplex = self.solution
            BFS.print_solution(Model.OPTIMAL)


def read_data(path):
    with open(path) as f:
        N, M = list(map(int, f.readline().split()))
        c = list(map(Fraction, f.readline().split()))
        A = []
        b = []
        for _ in range(M):
            line = list(map(Fraction, f.readline().split()))
            A.append(line[:-1])
            b.append(line[-1])

        return A, b, c


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Missing input file!!!')
    else:
        A, b, c = read_data(sys.argv[1].strip())
        model = BB(A, b, c)
        model.solve()
