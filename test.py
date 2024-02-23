import time
v = [0 for i in range(10 ** 6)]

t_list = []
for k in range(100):
    st_time = time.time()
    i = 0
    for l in v:
        j = l
        i += 1
    t_list.append(time.time() - st_time)
print(sum(t_list) / len(t_list))