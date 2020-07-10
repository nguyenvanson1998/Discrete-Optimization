from random import shuffle
import itertools 
import networkx as nx


from greedy1 import greedy

def get_adjlist(nodecount: int, edges: list):
    adj_list = []
    for _ in range(nodecount):
        adj_list.append(set())
    for e in edges:
        adj_list[e[0]].add(e[1])
        adj_list[e[1]].add(e[0])
    return adj_list

    

def permulation(node_count: int, edges: list, iter: int , max_stall: int):
    adj_list = get_adjlist(node_count, edges)
    global_sol = []
    global_obj = node_count +1
    G = nx.Graph(edges)
    n = int(iter)
    m = int(max_stall)
    for _ in range(n):
        # sinh ra d la 1 phuong an to mau theo pp ngau nhien return dict
        d = nx.coloring.greedy_color(G, strategy ='random_sequential')
        solution = [0]*node_count
        for i in range(len(solution)):
            solution[i] = d[i]
        obj = max(solution) + 1

        increase = True

        while increase:
            increase = False
            color_cases = []
            for j in range(obj):
                color_cases.append([])
            for i,c in enumerate(solution):
                color_cases[c].append(i)
            for case in color_cases:
                case.sort(key = lambda x: - len(adj_list[x]))
            
            for _ in range(m):
                shuffle(color_cases)
                order_nodes = list(itertools.chain.from_iterable(color_cases))
                solution1 = greedy(order_nodes, adj_list)
                obj1 = max(solution1) + 1
                if(obj1 < obj):
                    obj = obj1
                    solution = solution1
                    increase = True
                    break
        if(obj < global_obj):
            global_obj = obj
            global_sol = solution
    return global_obj, global_sol
    
            

            
            
            
            
        






