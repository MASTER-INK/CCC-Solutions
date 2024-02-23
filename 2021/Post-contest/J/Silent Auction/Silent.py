num = int(input()) * 2
auc = {}
while num > 0:
    if num % 2:
        number = int(input())
        if number not in auc:
            auc[number] = name
    else:
        name = input()
    num -= 1
print(auc[sorted(auc)[-1]])
