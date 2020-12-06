from datetime import date


def d(s):
    # date format transform
    [year, month, day] = map(int, s.split('/'))
    return date(year, month, day)


def days(start, end):
    # day gap calculation
    return abs((d(end) - d(start)).days)


class Dog:
    def __init__(self, name, height, weight, adopted_date):
        self.name = name
        self.height = height
        self.weight = weight
        self.adopted_date = adopted_date
        self.dust = 0
        self.walk_count = 0
        self.longest_duration = 0
        self.last_walk_date = adopted_date
        self.is_small_dog = self.check_if_small_dog()

    def check_if_small_dog(self):
        # 判斷是否為小型犬，回傳 boolean 值
        if self.height > 60 or self.weight > 30:
            return False
        else:
            return True

    def walk(self, walk_date):
        if self.is_small_dog:
            # 依據小型犬的灰塵累積效率更新累積灰塵量
            self.dust += 3
        else:
            # 依據大型犬的灰塵累積效率更新累積灰塵量
            self.dust += 2

        # 更新散步次數、最大散步間隔時間、最近散步日期
        if days(walk_date, self.last_walk_date) > self.longest_duration:
            self.longest_duration = days(walk_date, self.last_walk_date)

        self.last_walk_date = walk_date
        self.walk_count += 1

    def bathe(self):
        # 更新累積灰塵量
        self.dust = 0

    def frequency(self, today):
        # return the frequency
        return self.walk_count / days(today, self.adopted_date)

    def output(self):
        # output
        print(self.name, self.height, self.weight, self.dust, sep=',')


def comparer(dog1, dog2):
    # same spec comparison in order of size, weight, height and name

    # compare if one big one small
    if (not dog1.is_small_dog) and dog2.is_small_dog:
        return dog1
    elif (not dog2.is_small_dog) and dog1.is_small_dog:
        return dog2
    elif dog1.weight > dog2.weight:  # compare their weight
        return dog1
    elif dog1.weight == dog2.weight:
        if dog1.height > dog2.height:  # compare their height
            return dog1
        elif dog1.height == dog2.height:
            if dog1.name < dog2.name:  # compare their names
                return dog1
    return dog2


today = input()  # get today date
task = input().split(',')  # get the task

dogs = []  # list of all of dog
raw_input = input()
while raw_input != "Done":  # loop for the events
    event = raw_input.split('|')

    if event[0] == 'A':
        # adopt new dog
        dogs.append(Dog(event[1], int(event[2]), int(event[3]), event[4]))

    elif event[0] == 'B':
        # wash the specific dog
        for dog in dogs:
            if dog.name == event[1]:
                dog.bathe()

    elif event[0] == 'W':
        # walk the specific dog
        for dog in dogs:
            if dog.name == event[1]:
                dog.walk(event[2])

    elif event[0] == 'L':
        # remove the dog from list
        for dog in dogs:
            if dog.name == event[1]:
                dogs.remove(dog)

    raw_input = input()

out_dog = dogs[0]  # initialize the output dog
if task[0] == "TaskA":
    # get the spec of the assigned dog
    for dog in dogs:
        if dog.name == task[1]:
            out_dog = dog

elif task[0] == "TaskB":
    # find the dog which is walked least frequently
    for dog in dogs:
        if dog.frequency(today) < out_dog.frequency(today):
            out_dog = dog
        elif dog.frequency(today) == out_dog.frequency(today):
            out_dog = comparer(out_dog, dog)

elif task[0] == "TaskC":
    # find the dog which hasn't been walked for the longest time
    for dog in dogs:
        if dog.longest_duration < out_dog.longest_duration:
            out_dog = dog
        elif dog.longest_duration == out_dog.longest_duration:
            out_dog = comparer(out_dog, dog)

elif task[0] == "TaskD":
    # find the dog which has the most dust
    for dog in dogs:
        if dog.dust > out_dog.dust:
            out_dog = dog
        elif dog.dust == out_dog.dust:
            out_dog = comparer(out_dog, dog)

out_dog.output()  # output the dog spec
