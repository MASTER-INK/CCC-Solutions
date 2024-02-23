
import time
#l = [3, 1, 4, 1, 5, 9, 2]
#n = len(l)

#n = int(input())

#l = list(map(int, input().split()))

l = list(map(int, open('input_text.txt').read().split()))

n = len(l)

start = time.time()

most_sym = []

def shorten(l):
    new_l = l
    return new_l

for i in range(0, n, 2):
    l[i] *= -1

for size in range(n):
    l = shorten(l)
    cur_lowest = sorted(l, key = lambda x: abs(x))
    print(l)