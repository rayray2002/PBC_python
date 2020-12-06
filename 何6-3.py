def str_processor(string):
    output_companies = []
    for companies in target_companies:  # 對有在新聞標題裡出現的想關注的公司，
        if companies in string:  # 依序在一個sublist裡append它們的出現次數、
            sublist = [-string.count(companies),
                       target_companies.index(companies), companies]
            # 在target_companies
            output_companies.append(sublist)  # (想關注的公司集合list)裡的index
    if not output_companies:  # 以及公司名稱，在新聞標題裡
        return 'NO_MATCH'  # 沒有想關注的公司的話就直接結束函數
    output_companies.sort()
    for index in range(len(output_companies)):  # 用.sort()排序完公司之後，
        output_companies[index].pop(0)  # 將output_companies pop到只剩公司名稱，
        output_companies[index].pop(0)  # 並將其type由list轉為string
        output_companies[index] = string(output_companies[index][0])
    output_companies = ','.join(output_companies)
    slash_position = []  # 建立一個裝最終選取的關鍵字的index的空list
    for i in range(len(keywords)):  # 由字數多到少，依序對字數相同的關鍵字進行處理
        if not keywords[i]:  # 如果不存在某個字數的關鍵字，則直接跳出迴圈處理下一個字數的關鍵字
            continue
        start_index = -1
        while start_index < len(string):  # 找出某個字數的關鍵字中，何者在新聞標題裡的位置最前面
            min_keyword = ''
            minima = len(string)
            for keyword in keywords[i]:
                if string.find(keyword, start_index + 1) == -1:
                    continue
                else:
                    if string.find(keyword, start_index + 1) < minima:
                        minima = string.find(keyword, start_index + 1)
                        min_keyword = keyword
            loop_counter = 0
            if minima != len(string):  # 判斷上一個for迴圈找到的關鍵字在不在前面已經找到的關鍵字裡或與其有共用字元
                for k in range(len(slash_position)):  # 沒有的話它才是最終選取的關鍵字，這時會將它裝進
                    if slash_position[k][0] <= \
                            string.find(min_keyword, start_index + 1) \
                            <= slash_position[k][1] or \
                            (slash_position[k][0] <=
                             string.find(min_keyword, start_index + 1) +
                             len(min_keyword) - 1 <= slash_position[k][1]):
                        loop_counter = 1
                        break
                if loop_counter == 0:
                    sublist = [string.find(min_keyword, start_index + 1),
                               string.find(min_keyword,
                                           start_index + 1) + len(
                                   min_keyword) - 1]
                    slash_position.append(sublist)
            start_index = minima
    slash_position.sort()
    for i in range(len(slash_position)):  # 用最終選取的關鍵字的index的list，分別在關鍵字前後加上斜線
        string = string[:slash_position[i][0] + 2 * i] + '/' + \
                 string[slash_position[i][0] +
                        2 * i:slash_position[i][1] + 2 * i + 1]\
                 + '/' + string[slash_position[i][1] + 2 * i + 1:]
    if string[0] == '/':  # 刪除頭尾及中間多餘的斜線
        string = string[1:]
    if string[-1] == '/':
        string = string[:-1]
    for loop in range(string.count('//')):
        string = string.replace('//', '/')
    return output_companies + ';' + string


target_companies = input().split(',')  # 存取想關注的公司集合

input_keywords = input().split(',')  # 將所有關鍵字依字數分類：將字數一樣的裝到一個sublist，
for i in range(len(input_keywords)):  # 再將這些sublist依字數由多到少依序裝進一個list。
    input_keywords[i] = [input_keywords[i]]
    input_keywords[i].insert(0, -len(input_keywords[i][0]))
input_keywords.sort()
for i in range(len(input_keywords)):
    input_keywords[i].pop(0)
    input_keywords[i] = str(input_keywords[i][0])
keywords = []
for i in range(len(input_keywords[0]), 0, -1):
    keywords.append([])
    for j in range(len(input_keywords)):
        if len(input_keywords[j]) == i:
            keywords[len(input_keywords[0]) - i].append(input_keywords[j])

news_title = []  # 將所有新聞標題存成一個list直到遇到INPUT_END，並將其空格去除
input_ = input()
while input_ != 'INPUT_END':
    news_title.append(''.join(input_.split()))
    input_ = input()

for news in news_title:  # 分別將每個新聞標題丟進str_processor處理並輸出其結果
    print(str_processor(news))
