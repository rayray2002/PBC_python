companies = input().split(',')
keys = input().split(',')
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

title = input()
while title != "INPUT_END":
    title = "".join(title.split())

    companies_mention = []
    escape = True
    for company in companies:
        if title.count(company) != 0:
            companies_mention.append(company)
            escape = False

    if escape:
        print("NO_MATCH")
        title = input()
        continue

    company_prefix = ','.join(sorted(companies_mention,
                                     key=lambda x:
                                     (title.count(x),
                                      -dict(zip(companies,
                                                range(len(companies))))[x]),
                                     reverse=True))

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
            else:
                break

    while title.count("//"):
        title = title.replace("//", "/")

    print(company_prefix + ';' + title.strip('/'))

    title = input()
