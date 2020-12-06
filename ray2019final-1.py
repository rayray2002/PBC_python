raw = input().split(';')
n = int(raw[0])
w = raw[1].split(',')
raw = input()

highest_i = 0
highest_score = -1
for i in range(n):
    raw = input().split(',')
    s = 0
    for j in range(4):
        s += float(raw[j+1])*float(w[j])
    if s > highest_score:
        highest_i = int(raw[0])
        highest_score = s
    elif s == highest_score:
        if int(raw[0]) < highest_i:
            highest_i = int(raw[0])
print(str(highest_i) + ',' + str(int(highest_score//100)))
