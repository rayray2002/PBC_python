def str_processor(strg, key):
    b = -1
    result = []
    for i in range(strg.count(key)):
        b = strg.find(key, b + 1)
        if b == -1:
            break
        if b > 7:
            result.append(strg[b - 7:b] + "**" + key + "**" + strg[b + len(key):b + len(key) + 7])
        else:
            result.append(strg[0:b] + "**" + key + "**" + strg[b + len(key):b + len(key) + 7])
    return result


keyword = input()

main_str = ''
a = input()
while a != 'INPUT_END':
    main_str += a.strip() + ' '
    a = input()
main_str = main_str[:-1]

if str_processor(main_str, keyword):
    for out in str_processor(main_str, keyword):
        print(out)
else:
    print("NO_MATCH")