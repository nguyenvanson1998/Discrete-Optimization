import numpy as np


def greedy(order_nodes: list , adj_list: list):
    solution  = [-1] * len(order_nodes)
    colored = set()

    for node in order_nodes:
        colored.clear()
        for adj_node in adj_list[node]:
            if(solution[adj_node] != -1):
                colored.add(solution[adj_node])
    
        # add color for node i:
        c = 0
        while c in colored:
            c  += 1
        solution[node] = c

    return solution



    




    