for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    b = list(map(int, input().split()))
        
    """n = 7
    a = list(map(int, "6 7 3 4 4 6 5".split()))
    b = list(map(int, "6 3 4 4 7 6 5".split()))"""

    
    last = None
    greatest = 0
    greatest_list = []
    cur_sort = 0
    r = 0

    for i in range(n):
        #print(b[i], last)
        if last == None or b[i] >= last:
            cur_sort += 1
        else:
            if cur_sort > greatest:
                greatest_list = [r + 1, i]
                greatest = cur_sort
            cur_sort = 0
            r = i
        last = b[i]
    else:
        if greatest == 0:
            greatest_list = [r + 1, n]
    
    print("g", *greatest_list)