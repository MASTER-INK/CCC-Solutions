import time

n = 10 ** 5

log = {x:"" for x in range(n)}

#log = ["" for i in range(n)]

start = time.process_time()

c = 0

while log[c] != "":
    log.pop(0)

print("End", time.process_time() - start)