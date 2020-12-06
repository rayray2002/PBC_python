company = input().split(",")  # 公司名稱
key_words = input().split(",")  # 關鍵字
para = []  # 文章段落
string = input()
while string != "INPUT_END":  # 如果碰到INPUT_END 結束輸入
    para.append(string.replace(" ", ""))  # 去掉字串中的空格
    string = input()
key_words.sort(key=len, reverse=True)  # 將關鍵字照長度排列

company_n = []
# for i in range(len(para)):

    # best_num = -1
    # company_name = ""
    # for j in company:
    #     num = para.count(j)
    # print(num)
    # if num > best_num:
    #     best_num = num
    #     company_name = company[i]
    # elif num == best_num:
    #     if i < company.index(company_name):
    #         company_name = company[i]
    # elif num == 0:
    #     print("NO_MATCH")

#     company_n.append(company_name)
#
# for i in company_n:
#     print(i+";")


# while i != -1:
    # for j in range(len(key_words)):
    #     if para[i].find(key_words[j]) != -1:
    #         index = para[i].find(key_words[j], index + 1)
    #         print(str(para[0:index])+"/"+str(key_words[j])+"/"+str(para[index+len(key_words[j]):]))
index = -1
for i in range(len(para)):
    for j in range(len(key_words)):
        while para[i].find(key_words[j], index + 1) != -1:
            index = para[i].find(key_words[j], index + 1) + 1
            para[i] = para[i][0:index]+"/"+key_words[j]+"/"+para[i][index+len(key_words[j]):]
            index += 1
            # print(para)
print(para)