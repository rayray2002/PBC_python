address = input()
file = open(address, encoding="cp950")
raw = file.read().split("\n")

command = input()

data = []
for line in raw:
    data.append(line.split(","))

if command == "TYPE":
    for i in range(len(data[0])):
        num = 1
        for line in data:
            try:
                float(line[i])
            except:
                num = 0
        if num:
            print(str(i) + ": " + "numerical")
        else:
            print(str(i) + ": " + "categorical")

elif command == "MAXLEN":
    for i in range(len(data[0])):
        m = -1
        for line in data:
            d = line[i].strip()
            m = max(m, len(d))
        print(str(i) + ": " + str(m))

elif command == "MAXNUMLEN":
    for i in range(len(data[0])):
        num = 1
        m = -1
        for line in data:
            try:
                float(line[i])
            except:
                num = 0
        for line in data:
            if num:
                t = len(str(int(float(line[i]))))
            else:
                t = 0
            m = max(m, t)
        print(str(i) + ": " + str(m))

elif command == "MAXDECPLACE":
    for i in range(len(data[0])):
        num = 1
        m = -1
        for line in data:
            try:
                float(line[i])
            except:
                num = 0
        for line in data:
            if num:
                if line[i].find(".") == -1:
                    t = 0
                else:
                    t = len(line[i]) - 1 - line[i].find(".")
                    if t == 0:
                        t = 1
            else:
                t = 0
            m = max(m, t)
        print(str(i) + ": " + str(m))
