#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import math
import numpy as np
from collections import namedtuple

Point = namedtuple("Point", ['x', 'y'])

def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

def distance(points, nodeCount): #mang luu khoang cach giua cac dinh
    dis = np.zeros((nodeCount, nodeCount), dtype=float)
    for i in range(nodeCount):
        for j in range(nodeCount):
            dis[i][j] = length(points[i], points[j])
    return dis

def popsize(nodeCount): #100 con
    pop = np.empty((100, nodeCount), dtype=int)
    for i in range(nodeCount):
        pop[0][i] = i
    for i in range(1,100):
        rp = np.random.randint(nodeCount - 1, size=2)
        for j in range(nodeCount):
            pop[i][j] = pop[i-1][j]
        tmp = pop[i][rp[0]]
        pop[i][rp[0]] = pop[i][rp[1]]
        pop[i][rp[1]] = tmp
    return pop


def crossover(nodeCount): #lai hoa 100%, bat cap 2 cha me canh nhau
    pop = popsize(nodeCount)
    pop1 = popsize(nodeCount) #ban sao cua pop
    cro = np.empty((100, nodeCount), dtype=int)
    for i in range(100):
        rc = np.random.randint(nodeCount, size=1)
        if(i%2 == 0):
            for j in range(rc[0]):
                cro[i][j] = pop[i+1][j]
                for k in range(nodeCount):
                    if(pop1[i][k] == cro[i][j]):
                        pop1[i][k] = -1
            j = rc[0]
            for t in range(nodeCount):
                if(pop1[i][t] > -1):
                    cro[i][j] = pop1[i][t]
                    j = j + 1
        else:
            for j in range(rc[0]):
                cro[i][j] = pop[i-1][j]
                for k in range(nodeCount):
                    if(pop1[i][k] == cro[i][j]):
                        pop1[i][k] = -1
            j = rc[0]
            for t in range(nodeCount):
                if(pop1[i][t] > -1):
                    cro[i][j] = pop1[i][t]
                    j = j + 1
    return cro


def mutation(nodeCount): #xac xuat dot bien 100%
    mut = crossover(nodeCount)

    for i in range(100):
        rm = np.random.randint(nodeCount - 1, size=2)
        tmp = mut[i][rm[0]]
        mut[i][rm[0]] = mut[i][rm[1]]
        mut[i][rm[1]] = tmp
    return mut

def tsp(points, nodeCount):
    ans = np.empty(nodeCount, dtype=int)
    dis = distance(points, nodeCount)
    cyl = 1000
    minz = 10000000000000
    while(cyl >0):
        cyl = cyl - 1
        mut = mutation(nodeCount)
    for i in range(nodeCount - 1):
        cost = 0
        for j in range(nodeCount - 1):
            cost = cost + dis[mut[j]][mut[j + 1]]
        cost = cost + dis[mut[nodeCount - 1]][mut[0]]
        if (cost < minz):
            minz = cost
            an = i
    for k in range(nodeCount):
        ans[k] = mut[an][k]
        cost = minz
    return [ans, cost]

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
    print(mutation(nodeCount))
    ans = tsp(points, nodeCount)

    # build a trivial solution
    # visit the nodes in the order they appear in the file
    solution = ans[0]

    # calculate the length of the tour
    obj = ans[1]
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

