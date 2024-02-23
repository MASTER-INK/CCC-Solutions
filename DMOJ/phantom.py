

n = 50
print("2\n" + "\n".join(filter(lambda x: x != "", list(map(lambda x: x + "*" if x != "" and (str(int(x) + 2) in [str(i) if True not in list(map(lambda x: i % x == 0, [x for x in range(2, int((i ** 0.5) + 1))])) else "" for i in range(3, n, 2)]  or str(int(x) - 2) in [str(i) if True not in list(
    map(lambda x: i % x == 0, [x for x in range(2, int((i ** 0.5) + 1))])) else "" for i in range(3, n, 2)]) else x, [str(i) if True not in list(map(lambda x: i % x == 0, [x for x in range(2, int((i ** 0.5) + 1))])) else "" for i in range(3, n, 2)])))))

