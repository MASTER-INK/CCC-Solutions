n, m, k = 4, 4, 3
make = [9, 10, 10]
items = [1, 1, 1]
builds = [3, 4, 2]
"""
for o in range(k):
    builds.append(int(input()))
"""
roads = {}
for i in range(m):
    a, b, c = map(int, input().split())
    