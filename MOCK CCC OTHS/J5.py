from collections import defaultdict
n, m, k = 4, 4, 3
make = [9, 10, 10]
items = [1, 1, 1]
builds = [[3], [4], [2]]
"""
for o in range(k):
    builds.append(list(map(int, input().split())))
"""

roads = {1: [(2, 3)],
        2: [(3, 5), (4, 4)],
        3: [(4, 10)]}
"""
roads = defaultdict(list)
for i in range(m):
    a, b, c = map(int, input().split())
    roads[a].append((b, c))
    roads[b].append((a, c))
    """
    