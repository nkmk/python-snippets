import heapq

l = [3, 6, 7, -1, 23, -10, 18]

print(heapq.nlargest(3, l))
# [23, 18, 7]

print(heapq.nsmallest(3, l))
# [-10, -1, 3]

print(l)
# [3, 6, 7, -1, 23, -10, 18]
