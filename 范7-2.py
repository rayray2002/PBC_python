file_item = input()
file_genre = input()
codename = int(input())
item = open(file_item, mode='r', encoding='ISO-8859-1')
genre = open(file_genre, mode='r', encoding='ISO-8859-1')
data1 = item.read()
data2 = genre.read()
data1 = data1.split("\n")
data2 = data2.split("\n")

index = -1
idx = 0
para = ''
list1 = []

for i, d in enumerate(data1):
    if codename - 1 == i:
        para = d
if para != "":
    while idx != -1:
        idx = para.find("|", idx + 1)
        list1.append(idx)
    movie_title = para[list1[0] + 1:list1[1]]

    type_list = []
    for i in range(18):
        type_list.append(para[(list1[i + 4] + 1):list1[i + 5]])
    type_list.append(para[list1[22] + 1:])

    type_name = []
    index = -1
    for i, d in enumerate(data2):
        index = d.find('|')
        type_name.append(d[:index])
    types = []
    for i, d in enumerate(type_list):
        if d == "1":
            types.append(type_name[i])
    ans = ""
    ans += movie_title + ": "
    for i in range(len(types)):
        ans += types[i]
        if i != (len(types) - 1):
            ans += ", "
    print(ans)

else:
    print("No movie found.")
