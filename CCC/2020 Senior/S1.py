n = int(input())

times = {}

for i in range(n):
    t, x = map(int, input().split())
    times[t] = x
    
max_speed = 0
last_time = None
speed = 0
    
for t in sorted(list(times)):
    
    if last_time != None:
        speed = abs((times[t] - last_time[1]) / (t - last_time[0]))
    if last_time == None or speed > max_speed:
        max_speed = speed
    last_time = [t, times[t]]
print(max_speed)