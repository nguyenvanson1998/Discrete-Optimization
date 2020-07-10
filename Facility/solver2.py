#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
import math
from MIP import MipSolver
from utils import length


Point = namedtuple("Point", ['x', 'y'])
Facility = namedtuple("Facility", ['index', 'setup_cost', 'capacity', 'location'])
Customer = namedtuple("Customer", ['index', 'demand', 'location'])


def slice_solution(facilities, customers):
    obj: float
    solution: list
    if(len(facilities) < 1000):
        obj, solution = MipSolver(facilities, customers)
    # elif(len(facilities) == 100):
    #     m = len(facilities)
    #     n = len(customers)
    #     solution: list
    #     obj = 0
    #     obj2, solution2 = MipSolver(facilities[m//2:],customers[n//2:] )
    #     obj1, solution1 = MipSolver(facilities[:m//2],customers[:n//2] )
    #     obj = obj1 + obj2
    #     solution = list(solution1) + list(solution2)
    else:
        m = len(facilities)
        n = len(customers)
        
        sorted_facilities = sorted(facilities, key = lambda k: k.location.x* k.location.x)
        sorted_customers = sorted(customers, key = lambda k: k.location.x* k.location.x)
        obj = 0
        solution = []
        for i in range(10):
            obj1, solution1 = MipSolver(sorted_facilities[i*m//10:(i+1)*m//10],sorted_customers[i*n//10:(i+1)*n//10] )
            obj += obj1
            solution += list(solution1)
    return obj , solution

    



def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    parts = lines[0].split()
    facility_count = int(parts[0])
    customer_count = int(parts[1])
    
    facilities = []
    for i in range(1, facility_count+1):
        parts = lines[i].split()
        facilities.append(Facility(i-1, float(parts[0]), int(parts[1]), Point(float(parts[2]), float(parts[3])) ))

    customers = []
    for i in range(facility_count+1, facility_count+1+customer_count):
        parts = lines[i].split()
        customers.append(Customer(i-1-facility_count, int(parts[0]), Point(float(parts[1]), float(parts[2]))))

    # build a trivial solution
    # pack the facilities one by one until all the customers are served

    
    obj, solution = slice_solution(facilities, customers)

    # prepare the solution in the specified output format
    output_data = '%.2f' % obj + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, solution))

    return output_data


import sys

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/fl_16_2)')

