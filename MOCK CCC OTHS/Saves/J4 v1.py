#n, s, t = map(int, input().split())
n, s, t = map(int, "10 2 3".split())

#p = list(map(int, input().split()))
p = list(map(int, "10 1 3 2 9 9 8 9 1 1".split()))

if s * t >= n:
    print(sum(p))
else:
    bot_sum = 0
    bot_i = 0
    top_sum = 0
    top_i = 0
    total_destoryed = 0
    for h in range(t):
        if bot_sum >= top_sum:
            total_destoryed += bot_sum
            bot_i += s
            bot_sum = sum(p[bot_i - 1:(bot_i + s) - 2])
        else:
            total_destoryed += top_sum
            top_i -= s
            top_sum = sum(p[top_i - s + 2:top_i + 1])
    print(total_destoryed)