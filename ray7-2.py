address = input()
file = open(address, encoding="ISO-8859-1")
items = file.read().split('\n')

address = input()
file = open(address, encoding="ISO-8859-1")
genres = file.read().split('\n')

ID = input()

genres_dict = {}
for genre in genres:
    genre = genre.split("|")
    if genre[0]:
        genres_dict[int(genre[1])] = genre[0]

esc = True
for item in items:
    content = item.split("|")
    if content[0] == ID:
        esc = False
        print(content[1], end=': ')
        genres_include = []
        for i in range(19):
            if content[i+5] == "1":
                genres_include.append(genres_dict[i])
        print(", ".join(genres_include))
if esc:
    print("No movie found.")
