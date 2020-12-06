mapping = {0: "零", 1: "一", 2: "二", 3: "三", 4: "四", 5: "五", 6: "六", 7: "七",
           8: "八", 9: "九", 10: "十"}

op_map = {"+": "加", "-": "減", "*": "乘以", "/": "除以", "=": "等於"}


def num_to_ch(string):
    if len(string) == 2:
        ch = ""
        if string[0] != "1":
            ch += mapping[int(string[0])]
        ch += mapping[10]
        if string[1] != "0":
            ch += mapping[int(string[1])]
    else:
        ch = mapping[int(string[0])]
    return ch


string = input()
n_str = ""
for s in string:
    if "0" <= s <= "9":
        n_str += s
    else:
        print(num_to_ch(n_str), end='')
        print(op_map[s], end='')
        n_str = ""
print(num_to_ch(n_str), end='')
