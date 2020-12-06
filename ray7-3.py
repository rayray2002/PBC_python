address = input()
file = open(address)
news_title = file.read().split("\n")

address = input()
file = open(address)
news_dict_raw = file.read().split("\n")

address = input()
file = open(address)
company_category_raw = file.read().split("\n")

companies = []
company_category = {}
for line in company_category_raw:
    companies.append(line.split()[0])
    company_category[line.split()[0]] = line.split()[1]

keys = []
key_dict = {}
for line in news_dict_raw:
    keys.append(line.split()[0])
    key_dict[line.split()[0]] = line.split()[1]

keys.sort(key=len, reverse=True)
key_groups_by_len = []
temp = [keys[0]]
for key in keys[1:]:
    if len(key) == len(temp[0]):
        temp.append(key)
    else:
        key_groups_by_len.append(temp)
        temp = [key]
key_groups_by_len.append(temp)

raw_input = input().split(",")
target_category = raw_input[0]
target_amount = int(raw_input[1])
strategy = raw_input[2].split(":")

score_dict = {}
for company in companies:
    if company_category[company] == target_category:
        score_dict[company] = 0

for title_raw in news_title:
    title = "".join(title_raw.split())
    score = 0
    companies_mention = []
    for company in companies:
        if title.count(company) != 0:
            companies_mention.append(company)

    for key_group in key_groups_by_len:
        index = -1
        while True:
            target = len(key_group)
            pos = len(title)
            for i, key in enumerate(key_group):
                if title.find(key, index + 1) < pos and \
                        title.find(key, index + 1) != -1:
                    target = i
                    pos = title.find(key, index + 1)

            if target != len(key_group):
                index = pos + 1
                if title.count('/', pos) % 2 == 0:
                    title = title[:pos] + "/" + key_group[target] + "/" + \
                            title[pos + len(key_group[target]):]
                    for company in companies_mention:
                        if company_category[company] == target_category:
                            score_dict[company] += \
                                int(key_dict[key_group[target]])
            else:
                break

sorted_score = sorted(score_dict.items(),
                      key=lambda x: (x[1], x[0]), reverse=True)

amount = {}
ordered = []
for i in sorted_score:
    amount[i[0]] = 0
    ordered.append(i[0])

if sorted_score:
    while target_amount:
        for i, quantity in enumerate(strategy):
            if i < len(sorted_score):
                if target_amount > int(quantity):
                    amount[sorted_score[i][0]] += int(quantity)
                    target_amount -= int(quantity)
                else:
                    amount[sorted_score[i][0]] += target_amount
                    target_amount = 0

    for i, j in enumerate(ordered):
        if ordered[i]:
            print(j + "購買" + str(amount[j]) + "張")
else:
    print("NO_MATCH")
