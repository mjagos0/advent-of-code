import re
import math


def day_6_p1(input):
    time, distance = input.split('\n')
    time = list(map(int, re.findall('\d+', time)))
    distance = list(map(int, re.findall('\d+', distance)))

    res = 1
    for i in range(len(time)):
        a = 1
        b = time[i]
        c = distance[i]

        root1 = (-b + ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
        root2 = (-b - ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)

        if isinstance(root1, complex) or root1 == root2:
            continue
        else:
            res *= abs(math.ceil(root1) - math.floor(root2)) -1

    return res


def day_6_p2(input):
    time, distance = input.replace(' ', '').replace('Time:', '').replace('Distance:', '').split('\n')
    time = int(time)
    distance = int(distance)

    res = 1
    a = 1
    b = time
    c = distance

    root1 = (-b + ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
    root2 = (-b - ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
    res *= abs(math.ceil(root1) - math.floor(root2)) -1

    return res

with open('../input.txt') as f:
    input = f.read()

sample = '''Time:      7  15   30
Distance:  9  40  200'''

print(day_6_p1(input))
print(day_6_p2(input))
