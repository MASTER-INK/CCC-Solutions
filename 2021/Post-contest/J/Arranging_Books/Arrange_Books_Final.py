import collections
books = input()
letter_col = collections.defaultdict(int)
for i in books:
    letter_col[i] += 1
sections = {}
last = 0
for k in sorted(letter_col):
    sections[k] = books[last:last + letter_col[k]]
    last += letter_col[k]
arrange = 0
print(sections)
for m in sections:
    while sections[m] != (m * len(sections[m])):
        for l in sections:
            if l != m and m in sections[l]:
                g, h = sorted([l, m])
                for wow in sections[l]:
                    if wow == m:
                        arrange += 1
        sections[m] = m * len(sections[m])


print(arrange)
