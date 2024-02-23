import collections
books = list(input())
print(books)
cor_books = sorted(books)
num_of_lets = collections.defaultdict(int)
for l in books:
    num_of_lets[l] += 1
"""books.insert(-2, "he")"""
print(books)
placement = 0
arrange = 0
let = "F"
let_num = 0
while books != cor_books:
    if books[placement] == cor_books[placement]:
        placement += 0
    else:
        if placement > num_of_lets[let]:
            let_num += 1
            let = num_of_lets[let_num]
        books.insert(placement, "L")
        arrange += 1
        placement += 1
print(arrange)
