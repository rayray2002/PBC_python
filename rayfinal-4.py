n_map = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
         "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
         "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
         "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
         "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
         "seventy": 70, "eighty": 80, "ninety": 90, "zero": 0}


def en_to_int(string):
    temp = 0
    for n in string.split("-"):
        temp += n_map[n]
    return temp


equation = input().split()
result = en_to_int(equation[0])
for i in range(len(equation) // 2):
    if equation[2 * i + 1] == "plus":
        result += en_to_int(equation[2 * i + 2])
    else:
        result -= en_to_int(equation[2 * i + 2])
print(result)
