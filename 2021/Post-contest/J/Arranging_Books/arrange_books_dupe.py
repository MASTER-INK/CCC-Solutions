import collections
import time
def num_check(list, start):
    j = 0
    d = 0
    for k in list:
        j += k
    for l in range(start, len(list) + start, 1):
        d += l
    return d == j

def sort_books(books):
    arrange = 0
    books_col = collections.defaultdict(list)
    nums_col = {}
    for i in range(len(books)):
        books_col[books[i]] += [i]
        nums_col[i] = books[i]
    start = 0
    before = []
    for letters in sorted(books_col):
        let_pos = 0
        while num_check(books_col[letters], start) == False:
            time.sleep(10)
        start += len(books_col[letters])
        before.append(letters)

    return arrange

books = list(input())
print(sort_books(books))
