keyword = input()  # 不用str

S = ""
string = input()  # 用while才不會爆掉
while string != "INPUT_END":
    S += string.strip() + ' '  # 題目要空格分隔
    string = input()
S = S[:-1]  # 去掉尾巴的空格

count = S.count(keyword)  # 數一次就好

if count != 0:  # 只要考慮有沒有等於零
    index = -1  # 後面要加一
    while S.find(keyword, index + 1) != -1:
        index = S.find(keyword, index + 1)  # 加一才不會找到上一個
        if index < 7:
            print(S[0:index] + "**" + keyword + "**" + S[index + len(keyword):index + len(keyword) + 7])
        else:
            print(S[index - 7:index] + "**" + keyword + "**" + S[index + len(keyword):index + len(keyword) + 7])
else:
    print("NO_MATCH")
