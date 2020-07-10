from __future__ import print_function
from ortools.algorithms import pywrapknapsack_solver
import numpy as np
def ortool_solver(items,capacity):
    # Create the solver.
    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.
        KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')

    value = []
    weight = []
    for item in items:
       value.append(item.value)
       weight.append(item.weight)
    values = value
    weights = [weight]
    
    capacities = []
    capacities.append(capacity)
    #print(capacities)
    
   
    capacities = [capacity]


    solver.Init(values, weights, capacities)
    computed_value = solver.Solve()

    packed_items = []
    packed_weights = []
    total_weight = 0
    solution  = np.zeros(len(items), dtype = int)
    #print('Total value =', computed_value)
    for i in range(len(values)):
        if solver.BestSolutionContains(i):
            packed_items.append(i)
            packed_weights.append(weights[0][i])
            total_weight += weights[0][i]
    for i in packed_items:
        solution[i] = 1

    # print('Total weight:', total_weight)
    # print('Packed items:', packed_items)
    # print('Packed_weights:', packed_weights)
    return total_weight, solution
