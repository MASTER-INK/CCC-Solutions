###Problem J2: Time to Decompress
L = int(input())
chars = []
for i in range(L):
    n, t = input().split()
    chars.append(t * int(n))
for k in chars:
    print(k)
