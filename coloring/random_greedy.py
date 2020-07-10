from random import shuffle
import itertools
import networkx as nx

from greedy import greedy


def get_adjacency_list(node_count: int, edges: list):
    adjacency_list = []
    for _ in range(node_count):
        adjacency_list.append([])
    for n0, n1 in edges:
        adjacency_list[n0].append(n1)
        adjacency_list[n1].append(n0)
    return adjacency_list


def custom_coloring(node_count: int, edges: list, max_iter: int, max_stall: int):
    adjacency_list = get_adjacency_list(node_count, edges)

    # degrees = list(range(node_count))
    # degrees.sort(key=lambda x: - len(adjacency_list[x]))
    total_sol = []
    totla_obj = node_count + 1

    G = nx.Graph(edges)

    for _ in range(max_iter):
        d = nx.coloring.greedy_color(G, strategy='random_sequential')
        solution = [0] * node_count
        for i in range(node_count):
            solution[i] = d[i]
        obj = max(solution) + 1

        improved = True
        while improved:
            improved = False
            color_groups = []
            for _ in range(obj):
                color_groups.append([])
            for i, c in enumerate(solution):
                color_groups[c].append(i)
            for g in color_groups:
                g.sort(key=lambda x: - len(adjacency_list[x]))

            for _ in range(max_stall):
                shuffle(color_groups)
                ordered_nodes = list(itertools.chain.from_iterable(color_groups))
                new_solution = greedy(ordered_nodes, adjacency_list)
                new_obj = max(new_solution) + 1
                if new_obj < obj:
                    obj = new_obj
                    solution = new_solution
                    improved = True
                    break
        if obj < totla_obj:
            totla_obj = obj
            total_sol = solution

    return totla_obj, total_sol
