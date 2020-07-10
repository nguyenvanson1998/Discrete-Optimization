#!/usr/bin/python
# -*- coding: utf-8 -*-
from ortoolx import ortool_solver
from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def greedy(items, weight, taken,value,capacity):
    sorted_items = sorted(items, key = lambda x: -x.value/x.weight)
    for item in sorted_items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight

def dp(W,n,items,weight, taken):
    K = [[0 for w in range(W + 1)] 
            for i in range(n + 1)]
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif items[i-1].weight <= w:
                 K[i][w] = max(items[i - 1].value   + K[i - 1][w - items[i - 1].weight], K[i - 1][w])
            else:
                K[i][w] = K[i-1][w]
    weight = K[n][W]
    
    w = W
    res = weight
    for i in range(n, 0, -1): 
        if res <= 0: 
            break
        if res == K[i - 1][w]: 
            continue
        else:  
            taken[i-1] = 1
            res = res - items[i-1].value 
            w = w - items[i-1].weight 
    
    
            
    
def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    # a trivial algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0]*len(items)
    opt = 0
    if(item_count > 300 and capacity > 500):
       #greedy(items, weight, taken,value,capacity)
        value, taken = ortool_solver(items, capacity)
        opt = 0
    else:
        dp(capacity,item_count,items,weight, taken)
        opt = 1
        

  
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(opt) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

