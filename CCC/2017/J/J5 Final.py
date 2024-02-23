import collections

def go():
        n = int(input())

        a_list = list(map(int, input().split()))

        woods = [0 for i in range(2001)]

        ways = [0 for i in range(4002)]

        for i in a_list:
            woods[i] += 1

            
        for k in range(len(woods)):
            for p in range(k, len(woods)):
                #print(a, b)
                #print(k, p)
                if k == p:
                    ways[k + p] += woods[p] // 2
                else:
                    ways[k + p] += min(woods[k], woods[p])
                #print(ways, woods, len(woods))

        m = sorted(ways, reverse = True)

        high = m[0]

        diff_high = 0
        #print(m, ways)
        while diff_high < len(m) and m[diff_high] == high:
            diff_high += 1
        print(high, diff_high)
                
            

go()