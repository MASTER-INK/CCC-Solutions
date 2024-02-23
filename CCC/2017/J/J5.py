import collections
import os

def go(file_n):



        with open(file_n + ".in") as data:
            n = None
            for line in data:
                if n == None:
                    n = line.strip()
                else:
                    a_list = list(map(int, line.strip().split()))
                

        #n = int(input())

        #a_list = list(map(int, input().split()))

        woods = [0 for i in range(2001)]

        ways = [0 for i in range(4002)]

        for i in a_list:
            woods[i] += 1

        print(len(woods))
            
        for k in range(len(woods)):
            for p in range(k, len(woods)):
                #print(a, b)
                #print(k, p)
                if k == p:
                    ways[k + p] += woods[p] // 2
                else:
                    ways[k + p] += min(woods[k], woods[p])
                #print(ways, woods, len(woods))
            print(k)

        m = sorted(ways, reverse = True)

        high = m[0]

        diff_high = 0
        #print(m, ways)
        while diff_high < len(m) and m[diff_high] == high:
            diff_high += 1
        my_ans = "".join(str(high) + " " + str(diff_high))

        with open(file_n + ".out") as end_p:
            ans = ""
            for k in end_p:
                ans = k.strip()
                
        print(ans, my_ans)
                
        print(ans == my_ans)
                
            

if __name__ == "__main__":
    os.chdir("C:\\Users\\rmath\\Visual Code\\CCC\\2017\\J\\j5")
    for k in range(1, 20):
        go("j5." + (2 - len(str(k))) * "0" + str(k))