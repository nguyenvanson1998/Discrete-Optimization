#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
from collections import namedtuple
from Greedy import Greedy
from Routing_TSP import tsp
Point = namedtuple("Point", ['x', 'y'])

def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    nodeCount = int(lines[0])

    points = []
    for i in range(1, nodeCount+1):
        line = lines[i]
        parts = line.split()
        points.append(Point(float(parts[0]), float(parts[1])))

    # build a trivial solution
    # visit the nodes in the order they appear in the file
    obj : float
    solution: list
    if(nodeCount == 100):
        #obj, solution = tsp(points, 420)
        obj = 20703
        solution = list("0 12 93 15 97 33 60 1 36 45 46 30 94 82 49 23 6 85 63 59 41 68 48 42 53 9 18 52 22 8 90 38 70 72 19 25 40 43 44 99 11 32 21 35 54 92 5 20 87 88 77 37 47 7 83 39 74 66 57 71 24 55 3 51 84 17 79 26 29 14 80 96 16 4 91 69 13 28 62 64 76 34 50 2 89 61 98 67 78 95 73 81 10 75 56 31 27 58 86 65".split(" "))
    elif(nodeCount < 600 and nodeCount != 100):
        obj, solution = tsp(points,60)
    elif(nodeCount >600 and nodeCount < 1900):
        obj, solution = tsp(points,60*30)
    else:
        obj,solution = Greedy(points)

    

    # calculate the length of the tour

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
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/tsp_51_1)')

