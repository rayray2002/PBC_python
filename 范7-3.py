file_news_title = "inputs/news_title.txt"
file_news_dict = "inputs/news_dict.txt"
file_company_category = "inputs/company_category.txt"
news_title = open(file_news_title,"r",encoding="utf-8")
news_dict = open(file_news_dict,"r",encoding="utf-8")
company_category = open(file_company_category,"r",encoding="utf-8")
list1 = input().split(",")
industry = list1[0]
total_num = list1[1]
num_each_round = list1[2].split(":")

title = []
for i, d in enumerate(news_dict):  # 先將關鍵字照長度排列
    title.append([d[0:-2],d[-2:-1]])
title.sort(key=lambda k:len(k[0]),reverse=True)
# print(title)
company_list=[]
index = -1
for i, d in enumerate(company_category):  # 找出關注的公司
    index = d.find(" ")
    if d[index+1:-1] == industry:
        company_list.append(d[0:index])
# print(company_list)
para = []
for i, d in enumerate(news_title):  # 將新聞標題轉成list
    d = d.replace(" ","")
    d = d.replace("\n","")
    para.append(d)

news = []
index = -1
for i ,d in enumerate(para):  # 建立新的list放要關注的新聞標題
    for j in range(len(company_list)):
        index =  d.find(company_list[j])
        if index != -1:
            news.append(d)
# print(news)
company_times = []  # 計算每個標題中專注的公司與其出現次數
for i,d in enumerate(news):
    for j in range(len(company_list)):
        appear_time = d.count(company_list[j])
        if appear_time != 0:
            company_times.append([company_list[j],appear_time,i])
# print(company_times)

for i in range(len(news)):
    for j in range(len(title)):
        index = -1
        while news[i].find(title[j][0],index+1) != -1:
            index = news[i].find(title[j][0], index + 1)
            print(index)
            news[i] = news[i][0:index-1]+"/"+title[j][0]+"/"+news[i][index+len(title[j][0]):]
            index += 1
print(news)