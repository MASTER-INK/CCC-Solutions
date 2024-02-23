icon = ["*x*",
" xx", 
"* *"]

k = int(input())

grid = [['' for x in range(len(icon) * k)] for y in range(len(icon[0]) * k)]


for y in range(len(icon)):
    for x in range(len(icon[y])):
        cur_i = icon[y][x]
        for i_x in range(k):
            for i_y in range(k):
                grid[(y * k) + i_y][(x * k) + i_x] = cur_i
                
for line in grid: print(*line)