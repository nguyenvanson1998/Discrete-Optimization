from __future__ import print_function
from ortools.linear_solver import pywraplp
import numpy as np
import math
from greedy import Greedy
def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

def MipSolver(facilities: [] , customers: [] ):
    # Create the mip solver with the CBC backend.
    solver = pywraplp.Solver('simple_mip_program',pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    
    m = len(facilities)
    n  = len(customers)
    #define  vars
    x = np.empty(m, dtype = object)
    y = np.empty((m,n) , dtype = object)
    for i in range (m):
        x[i] = solver.IntVar(0,1, 'X[%d]'%i)
        for j in range(n):
            y[i][j] = solver.IntVar(0,1, 'Y[%d' %i + ']' +'[' +str(j)+']')
    #define the constraint
    # rang buoc ve demand and capacity
    for i in range(m):
        constraint_capacity = solver.RowConstraint(0, facilities[i].capacity, '')
        for j in range(n):
            constraint_capacity.SetCoefficient(y[i][j], customers[j].demand)


    for i in range(m):
        constraint1 = solver.RowConstraint(0, n, '')
        constraint1.SetCoefficient(x[i], n)
        for j in range(n):
            constraint1.SetCoefficient(y[i][j], -1)
            
    for j in range(n):
        constaint = solver.Constraint(1,1, '')
        for i in range(m):
            constaint.SetCoefficient(y[i][j], 1)
    # minimum 
    objective = solver.Objective()
    for j in range(m):
        objective.SetCoefficient(x[j], facilities[j].setup_cost) 
    for i in range(m):
        for j in range(n):
            twc = length(facilities[i].location, customers[j].location)
            objective.SetCoefficient(y[i][j], twc)
    objective.SetMinimization()

    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        obj = solver.Objective().Value()
        solution = np.empty(n, dtype = int)
        for j in range(n):
            for i in range(m):
                if(y[i][j].solution_value() == 1):
                    solution[j]  = i
        return obj, solution
    else:
        return Greedy(customers, facilities)
            




    
    
    