n, s, t = map(int, input().split())
#n, s, t = map(int, "11 4 2".split())

p = list(map(int, input().split()))
#p = list(map(int, "9 4 1 3 2 1 3 2 9 1 1".split()))

if s * t >= n:
    print(0)
else:
    s_ind = s * t
    bot_sum = sum(p[:s_ind])
    top_sum = 0
    max_sum = bot_sum + top_sum
    for j in range(t):
        bot_sum -= sum(p[s_ind - s: s_ind])
        top_sum += sum(p[n - ((j + 1) * s): n - (j * s)])
        s_sum = bot_sum + top_sum
        if s_sum > max_sum:
            max_sum = 0 + s_sum
        s_ind -= s
    print(max_sum)