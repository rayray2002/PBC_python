raw = input().split(',')

n = int(raw[0])
capacity = int(raw[1])

down = []
raw = input().split(',')
for i in range(n):
    down.append(int(raw[i]))

up = []
raw = input().split(',')
for i in range(n):
    up.append(int(raw[i]))

count = 0
code = 0
for i in range(n):
    if down[i] > count and code == 0:
        code = 1
    count -= down[i]
    count += up[i]
    if count > capacity and code == 0:
        code = 2

print(str(count) + "," + str(code))
