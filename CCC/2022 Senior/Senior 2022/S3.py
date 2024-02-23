
from math import floor
def arth_seq(n):
    #(n / 2) * (2 + (n - 1))
    return (n / 2) * (n + 1)
def get_good_samples(n, m, k):
    if m >= n:
        total = arth_seq(n)
        if k < n or total < k:
            return -1
        for i in range(n - 1, 0, -1):
            if total - i < k:
                break
            else:
                total -= i
        final = [1 for x in range((n - 1) - i)] + [g for g in range(1, i + 1)]
        ind = int(total - k) * -1
        if ind == -1:
            final.append(1)
        else:
            final.insert(ind + 1, 1)
        return final
    else:
        #fix this part
        """
        total = (arth_seq(m) * floor(n / m)) + arth_seq(n - (floor(n / m) * m)) + ((m - 1) * (floor(n / m) - 1)) + (((n / m) - floor(n / m)) * m)
        print((arth_seq(m) * floor(n / m)), arth_seq(n - (floor(n / m) * m)), (m - 1) * (floor(n / m) - 1), floor(n / m))
        print(total)"""
        total = arth_seq(n) - arth_seq(n - m)
        if k < n or total < k:
            return -1
        left = total - k
        ones = floor(left / (m - 1))
        final = [1 for i in range(ones)]
        left -= (ones * (m - 1))
        final += [((g % m) + 1) for g in range(n - len(final))]
        if left != 0:
            final.pop(-1)
            final.insert(int(left * -1), 1)    
        return final
        

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    l = get_good_samples(n, m , k)
    if l == -1:
        print(-1)
    else:
        print(*l)
    
