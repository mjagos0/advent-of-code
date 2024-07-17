def day_9_p1(input):
    input = input.split('\n')
    sum_extrapolate = 0

    for s in input:
        s = list(map(int, s.split(' ')))
        triangle = [s]
        all_zero = True

        while not all_zero or len(triangle) == 1:
            all_zero = True
            triangle.append([])
            for i in range(1, len(triangle[-2])):
                diff = triangle[-2][i]-triangle[-2][i-1]
                triangle[-1].append(diff)
                if diff != 0:
                    all_zero = False

        cur_sum = 0
        for row in triangle[-2::-1]:
            cur_sum += row[-1]

        sum_extrapolate += cur_sum

    return sum_extrapolate


def day_9_p2(input):
    input = input.split('\n')
    sum_extrapolate = 0

    for s in input:
        s = list(map(int, s.split(' ')))
        triangle = [s]
        all_zero = True

        while not all_zero or len(triangle) == 1:
            all_zero = True
            triangle.append([])
            for i in range(1, len(triangle[-2])):
                diff = triangle[-2][i]-triangle[-2][i-1]
                triangle[-1].append(diff)
                if diff != 0:
                    all_zero = False

        cur_sum = 0
        for row in triangle[-2::-1]:
            cur_sum = row[0] - cur_sum

        sum_extrapolate += cur_sum

    return sum_extrapolate


with open('../input.txt') as f:
    input = f.read()

sample = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''

print(day_9_p1(input))
print(day_9_p2(input))
