P = int(input())
K = int(input())
R = int(input())
num = 0
N = 0
while P > N:
    num += 1
    N += K * (R ** num)
print(num)
