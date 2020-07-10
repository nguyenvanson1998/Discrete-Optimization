import sys

from branch_and_bound import read_data
from two_phase import Model

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Missing input file!!!')
    else:
        A, b, c = read_data(sys.argv[1].strip())
        model = Model(A, b, c)
        status = model.lp_solve()
        model.print_solution(status)
