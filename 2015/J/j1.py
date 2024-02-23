month = int(input())
day = int(input())

months = [31, 28, 30, 31, 30, 31, 31, 30, 30, 30, 30, 31]

total = sum(months[:month - 1]) + day

if total > 49:
    print('After')
elif total == 49:
    print('Special')
else:
    print('Before')