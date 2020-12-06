address = input()
key = input()

file = open(address)
data = file.read().replace("\t", "\n")
data = data.split('\n')
print(data, len(data))
previous = {}
following = {}

for i, d in enumerate(data):
    data[i] = d.strip()
    index = -1
    while True:
        index = d.find(key, index+1)
        if index != -1:
            if index > 0:
                if previous.get(d[index-1]):
                    previous[d[index-1]] += 1
                else:
                    previous[d[index-1]] = 1
            if index < len(d)-len(key):
                if following.get(d[index + len(key)]):
                    following[d[index + len(key)]] += 1
                else:
                    following[d[index + len(key)]] = 1
        else:
            break

sorted_previous = sorted(previous.items(),
                         key=lambda x: (x[1], x[0]), reverse=True)
sorted_next = sorted(following.items(),
                     key=lambda x: (x[1], x[0]), reverse=True)

print("熱門前一個字:")
for i in range(10):
    if i < len(sorted_previous):
        print(sorted_previous[i][0] + "---" + key)

print("熱門下一個字:")
for i in range(10):
    if i < len(sorted_next):
        print(key + "---" + sorted_next[i][0])
