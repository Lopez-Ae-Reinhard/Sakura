"""
    2048 核心算法
"""
import random
# 练习1:定义函数,将零元素移动到末尾
# 2 0 2 0 --> 2 2 0 0
"""
def list_sort(list01):
    for max01 in range(len(list01) - 1):
        for min01 in range(max01 + 1, len(list01)):
            if list01[min01] != 0:
                list01[min01], list01[max01] = list01[max01], list01[min01]
"""

"""
def list_sort(list01):
    for i in range(len(list01) - 1, -1, -1):
        if list01[i] == 0:
            del list01[i]
            list01.append(0)
"""


def list_sort(list01):
    list02 = []
    for i in list01:
        if i != 0:
            list02.append(i)
    list02 += [0] * list01.count(0)
    list01[:] = list02


# 练习2:定义合并函数
# list01 = [4, 2, 0, 2]


def merge(list01):
    list_sort(list01)
    for i in range(len(list01) - 1):
        if list01[i] == list01[i + 1]:
            list01[i] += list01[i + 1]
            list01[i + 1] = 0
    list_sort(list01)


# merge(list01)
# print(list01)


# 练习三:构建一个二维列表输入到控制台
def print_map(list02):
    for r in range(len(list02)):
        for c in range(len(list02[r])):
            print(list02[r][c], end=" ")
        print()


# 练习4:
list02 = [
    [4, 0, 0, 2],
    [0, 2, 0, 2],
    [2, 0, 2, 0],
    [0, 0, 0, 2]
]


# print_map(list02)


def move_left(list03):
    # for x in list03:
    for x in range(len(list03)):
        merge(list03[x])


def move_right(list03):
    for x in range(len(list03)):
        merge(list03[x])
        list03[x].reverse()
        return list03


def move_up(list02):
    for y in range(len(list02)):
        list03 = []
        for x in range(len(list02)):
            list03.append(list02[x][y])
        merge(list03)
        for x in range(len(list02)):
            list02[x][y] = list03[x]
    return list02


def move_down(list02):
    for y in range(len(list02)):
        list03 = []
        for x in range(len(list02)):
            list03.append(list02[len(list02) - x - 1][y])
        merge(list03)
        for x in range(len(list02)):
            list02[len(list02) - x - 1][y] = list03[x]
    return list02


def found_zero(list02):
    num = 0
    for r in range(len(list02)):
        for c in range(len(list02[r])):
            if list02[r][c] == 0:
                num +=1
    print(num)

def zero_point(list02):
    list01 = []
    for r in range(len(list02)):
        for c in range(len(list02[r])):
            if list02[r][c] == 0:
                list01.append((r,c))
    return list01

def random_num(list01):
    end_num = len(zero_point(list01))
    num = random.randint(0,end_num-1)
    return zero_point(list01)[num]

def probability_random(list02):
    rand_num = random_num(list02)
    list01 = [4,2,2,2,2,2,2,2,2,2]
    end_num = len(list01)
    num = random.randint(0,end_num)
    pro_num = list01[num]
    list02[rand_num[0]][rand_num[1]] = pro_num

print_map(list02)
# print(zero_point(list02))
# random_num(list02)
# print(random_num(list02))
probability_random(list02)
print_map(list02)
probability_random(list02)
print_map(list02)