n, s, t = map(int, input().split())
#n, s, t = map(int, "10 2 3".split())

p = list(map(int, input().split()))
#p = list(map(int, "10 1 3 2 9 9 8 9 1 1".split()))

if s * t >= n:
    print(sum(p))
else:
    right = sum(p[n - (s * t):])
    left = 0
    max_sum = 0 + (left + right)
    for i in range(t):
        left += sum(p[i * s: (i + 1) * s])
        right -= sum(p[n - (s * (t - i)):n - (s * (t - (i + 1)))])
        cur_sum = left + right
        if cur_sum > max_sum:
            max_sum = 0 + cur_sum
    print(max_sum)