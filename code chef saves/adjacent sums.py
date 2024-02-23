# cook your dish here
#https://www.codechef.com/problems/CHFADJSUM
from collections import defaultdict


def adjacent_sum(a_col):
    s = sorted(list(a_col), reverse=True)
    lowest = s[0] // 2
    finished = False
    c = 0
    while lowest > 0 and finished == False:
        num = s[c]
        while a_col[num] > 0 and lowest > 0:
            if a_col[lowest] > 0:
                a_col[lowest] -= 1
                a_col[num] -= 1
            else:
                lowest -= 1
        c += 1
        if c == len(s):
            finished = True

    if finished == True:
        return "YES"
    else:
        return "NO"


for t in range(int(input())):
    n = int(input())

    a = list(map(int, input().split()))
    a_col = defaultdict(int)

    z_list = [0, 0]
    z = 0
    for i in a:
        if i > z_list[0]:
            z_list[1] = z_list[0]
            z_list[0] = i
        elif i > z_list[1]:
            z_list[1] = i
        a_col[i] += 1

    print(adjacent_sum(a_col))
