n = int(input())

c = []
pair = []
for i in range(n):
    raw = input().split(',')
    temp = []
    for j in range(n):
        temp.append(int(raw[j]))
    c.append(temp)
    pair.append(0)

cost = 0
for k in range(n):
    min_cost = 101
    final_j = 0
    final_i = 0
    for i in range(n):
        for j in range(n):
            if c[i][j] < min_cost:
                min_cost = c[i][j]
                final_i = i
                final_j = j
            elif c[i][j] == min_cost:
                if final_j + final_i > i + j:
                    min_cost = c[i][j]
                    final_i = i
                    final_j = j

    pair[final_i] = str(final_j + 1)
    cost += min_cost

    for i in range(n):
        c[i][final_j] = 101
        c[final_i][i] = 101

print(','.join(pair) + ';' + str(cost))
