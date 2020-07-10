import math 


from collections import namedtuple

Point = namedtuple("Point", ['x', 'y'])

def distance(v1: Point ,v2 :Point):
    return math.sqrt( (v1.x - v2.x)**2 + (v1.y - v2.y)**2 )
def get_point(Points, v: int):
    x : Point
    x = Points[v]
    return x
def edges_cost(Points: [Point], v1:int, v2:int):
    a = Points[v1]
    b = Points[v2]
    return distance(a, b)
def get_obj(Points : [Point],solution: list):
    s = 0
    for v1, v2 in zip(solution[:-1], solution[1:]):
        s += edges_cost(Points,v1,v2)
    return s

def find_nearest(Points: [Point], v: int, candidates: set):
    min = math.inf
    node = None
    for i in candidates:
        if(edges_cost(Points,v, i) < min):
            min = edges_cost(Points, v, i )
            node = i
    return node


def Greedy(Points: [Point]):
    cycle = [0]

    path = list(set(range(len(Points)))) + [0]
    candidates = set(path[1:-1])
    while candidates:
        curr_point = cycle[-1]
        nearest_point = find_nearest(Points, curr_point, candidates)
        cycle.append(nearest_point)
        candidates.remove(nearest_point)

    cycle.append(0)
    obj = get_obj(Points, cycle)
    return obj, cycle[:-1]




