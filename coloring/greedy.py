import numpy as np


def find_color(used: set):
    c = 0
    while c in used:
        c += 1
    return c



def greedy_by_max_deg(node_count, edge_count, edges):
    solution = [-1] * node_count
    opt = 0
    d = []
    c = []
    for i in range(node_count):
        d.append(set())
        c.append(set(range(node_count)))
    for e in edges:
        d[e[0]].add(e[1])
        d[e[1]].add(e[0])
    for i in range(node_count):
        idx = -1
        for j in range(node_count):
            if solution[j] == -1:
                if idx == -1:
                    idx = j
                elif len(d[j]) > len(d[idx]):
                    idx = j
        if idx != -1:
            solution[idx] = min(c[idx])
            for j in d[idx]:
                d[j].discard(idx)
                c[j].discard(solution[idx])
            print(idx, solution[idx])
    return solution, opt
def greedy(ordered_nodes: list, adjacency_list: list):
    # upperbound = max(len(adjacency_list[x]) for x in range(node_count)) + 1

    # degrees = list(range(node_count))
    # degrees.sort(key=lambda x: - len(adjacency_list[x]))
    # occurences = np.empty(len(ordered_nodes), int)

    solution = [-1] * len(ordered_nodes)
    used = set()
    for i in ordered_nodes:
        used.clear()
        # occurences.fill(0)
        for j in adjacency_list[i]:
            if solution[j] != -1:
                used.add(solution[j])
            # else:
            #     for k in adjacency_list[j]:
            #         if solution[k] != -1:
            #             occurences[solution[k]] -= 1
        # rank_color = np.argsort(occurences)
        # for c in rank_color:
        #     if c not in used:
        #         solution[i] = c
        #         break
        # for c in used:
        #     occurences[c] = 0
        # best = np.argmax(occurences)
        solution[i] = find_color(used)

    return solution
