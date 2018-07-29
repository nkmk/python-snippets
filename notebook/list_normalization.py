import statistics
import pprint

l = [0, 1, 2, 3, 4]

print(l)
# [0, 1, 2, 3, 4]

def min_max(l):
    l_min = min(l)
    l_max = max(l)
    return [(i - l_min) / (l_max - l_min) for i in l]

print(min_max(l))
# [0.0, 0.25, 0.5, 0.75, 1.0]

def standardization(l):
    l_mean = statistics.mean(l)
    l_stdev = statistics.stdev(l)
    return [(i - l_mean) / l_stdev for i in l]

pprint.pprint(standardization(l))
# [-1.2649110640673518,
#  -0.6324555320336759,
#  0.0,
#  0.6324555320336759,
#  1.2649110640673518]

def standardization_p(l):
    l_mean = statistics.mean(l)
    l_pstdev = statistics.pstdev(l)
    return [(i - l_mean) / l_pstdev for i in l]

pprint.pprint(standardization_p(l))
# [-1.414213562373095,
#  -0.7071067811865475,
#  0.0,
#  0.7071067811865475,
#  1.414213562373095]

l_2d = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

print(l_2d)
# [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

pprint.pprint([min_max(l_1d) for l_1d in l_2d], width=40)
# [[0.0, 0.5, 1.0],
#  [0.0, 0.5, 1.0],
#  [0.0, 0.5, 1.0]]

pprint.pprint([standardization(l_1d) for l_1d in l_2d], width=40)
# [[-1.0, 0.0, 1.0],
#  [-1.0, 0.0, 1.0],
#  [-1.0, 0.0, 1.0]]

pprint.pprint([standardization_p(l_1d) for l_1d in l_2d])
# [[-1.224744871391589, 0.0, 1.224744871391589],
#  [-1.224744871391589, 0.0, 1.224744871391589],
#  [-1.224744871391589, 0.0, 1.224744871391589]]

l_2d_min_max_col = list(zip(*[min_max(l_1d) for l_1d in list(zip(*l_2d))]))

pprint.pprint(l_2d_min_max_col, width=40)
# [(0.0, 0.0, 0.0),
#  (0.5, 0.5, 0.5),
#  (1.0, 1.0, 1.0)]

l_2d_standardization_col = list(zip(*[standardization(l_1d) for l_1d in list(zip(*l_2d))]))

pprint.pprint(l_2d_standardization_col, width=40)
# [(-1.0, -1.0, -1.0),
#  (0.0, 0.0, 0.0),
#  (1.0, 1.0, 1.0)]

l_2d_standardization_p_col = list(zip(*[standardization_p(l_1d) for l_1d in list(zip(*l_2d))]))

pprint.pprint(l_2d_standardization_p_col)
# [(-1.2247448713915892, -1.2247448713915892, -1.2247448713915892),
#  (0.0, 0.0, 0.0),
#  (1.2247448713915892, 1.2247448713915892, 1.2247448713915892)]

def min_max_2d_all(l_2d):
    l_flatten = sum(l_2d, [])
    l_2d_min = min(l_flatten)
    l_2d_max = max(l_flatten)
    return [[(i - l_2d_min) / (l_2d_max - l_2d_min) for i in l_1d]
            for l_1d in l_2d]

pprint.pprint(min_max_2d_all(l_2d), width=40)
# [[0.0, 0.125, 0.25],
#  [0.375, 0.5, 0.625],
#  [0.75, 0.875, 1.0]]

def standardization_2d_all(l):
    l_flatten = sum(l_2d, [])
    l_2d_mean = statistics.mean(l_flatten)
    l_2d_stdev = statistics.stdev(l_flatten)
    return [[(i - l_2d_mean) / l_2d_stdev for i in l_1d]
            for l_1d in l_2d]

pprint.pprint(standardization_2d_all(l_2d))
# [[-1.4605934866804429, -1.0954451150103321, -0.7302967433402214],
#  [-0.3651483716701107, 0.0, 0.3651483716701107],
#  [0.7302967433402214, 1.0954451150103321, 1.4605934866804429]]

def standardization_p_2d_all(l):
    l_flatten = sum(l_2d, [])
    l_2d_mean = statistics.mean(l_flatten)
    l_2d_pstdev = statistics.pstdev(l_flatten)
    return [[(i - l_2d_mean) / l_2d_pstdev for i in l_1d]
            for l_1d in l_2d]

pprint.pprint(standardization_p_2d_all(l_2d))
# [[-1.5491933384829668, -1.161895003862225, -0.7745966692414834],
#  [-0.3872983346207417, 0.0, 0.3872983346207417],
#  [0.7745966692414834, 1.161895003862225, 1.5491933384829668]]
