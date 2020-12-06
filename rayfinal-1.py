raw = input().split(',')

m = int(raw[0])
n = int(raw[1])

vectors = []
for i in range(m):
    raw = input().split(',')
    temp = []
    for j in range(n):
        temp.append(int(raw[j]))
    vectors.append(temp)

min_d = 10e10
for i in range(m-1):
    for j in range(i+1, m):
        d = 0
        for k in range(n):
            d += (vectors[i][k] - vectors[j][k])**2
        min_d = min(min_d, d)
print(min_d)
